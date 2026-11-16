---
name: investigate-failing-test
description: "Investiga um ou mais testes automatizados que falharam e decide entre corrigir o teste, reportar um bug de produto ou apontar um problema de ambiente. Use quando alguém passar um ID de teste, um link de run ou uma thread dizendo \"esse teste quebrou, vê o que aconteceu\"."
---

<!-- Gerado por scripts/exportar.py; edite skills/ na distribuição. -->

# Investigar teste falhando

A pergunta a responder é sempre a mesma: **o teste está errado, o produto está errado ou o ambiente está fora?** Cada resposta leva a uma saída diferente.

## Ajuste antes de usar

- Comando para rodar um teste só: `<ex.: npx playwright test -g "QA-123">`
- Onde ficam os casos de teste escritos (comportamento esperado): `<ferramenta ou pasta>`
- Repo da aplicação, se você tiver acesso de leitura: `<caminho ou URL>`

## Limites

- Edita arquivos de teste na working tree, mas **não commita, não faz push e não cria ticket**. Devolve um relatório.
- Nunca "conserta" um teste afrouxando a asserção sem explicar por que o comportamento esperado mudou.
- Nunca aumenta timeout como primeira tentativa.

## Passos

1. **Leia a memória primeiro.** `known-red-tests.md` e `known-traps.md` em `.agents/references/test-investigation/`. Se o teste já está lá com a mesma assinatura, diga isso e pare.

2. **Colete a evidência do run original:** mensagem de erro, locator, linha do teste, screenshot ou trace se existir. Anote o commit em que o run aconteceu.

3. **Leia o comportamento esperado.** O caso de teste escrito diz o que deveria acontecer. Sem isso, você não sabe se o teste ou o produto está certo.

4. **Reproduza localmente, sem retry e com um reporter simples.**

   ```bash
   <comando do teste> --retries=0 --reporter=line
   ```

   Retry esconde falha. Rode pelo menos duas vezes: passar uma vez não prova nada.

5. **Compare com o que mudou.** Olhe os commits da aplicação e do repo de testes desde o último run verde. Uma mudança de texto, de seletor ou de ordem de requisição costuma explicar a falha.

6. **Decida:**

   | Achado                                             | Saída                                              |
   | -------------------------------------------------- | -------------------------------------------------- |
   | Seletor, dado de teste ou espera mal escrita       | Corrija o teste e rode de novo duas vezes          |
   | O produto faz diferente do caso de teste escrito   | Não mexa no teste. Descreva como possível bug      |
   | 5xx, credencial, serviço externo, dado de ambiente | Não mexa no teste. Diga quem precisa destravar     |
   | Passa local e falha no CI                          | Compare browser, sistema, paralelismo e dados      |

7. **Se achou uma armadilha nova** (algo que fez você perder tempo indo na direção errada), proponha a entrada para `known-traps.md`.

## Relatório

```
## <ID do teste> · <veredito: teste | bug | ambiente>

**Erro:** <assinatura em uma linha>
**Causa:** <o que de fato aconteceu>
**Evidência:** <trecho de log, commit, screenshot>
**O que eu fiz:** <diff resumido, ou "nada">
**Reexecução:** <2/2 passou | não se aplica>
**Próximo passo:** <quem faz o quê>
```

Para enviar a correção, use `/create-pr`. Para registrar os bugs aprovados, use `/file-qa-bug`.
