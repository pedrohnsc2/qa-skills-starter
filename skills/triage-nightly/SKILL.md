---
name: triage-nightly
description: "Faz a triagem do run noturno de testes E2E. Compara com o run anterior, classifica cada falha (conhecida, nova, flaky, cascata, ambiente) e entrega um resumo curto. Use quando alguém disser \"a nightly quebrou\", \"triagem do run de hoje\" ou passar o link de um run agendado."
---

# Triagem da nightly

Objetivo: transformar uma lista de testes vermelhos em uma lista curta de causas, dizendo o que precisa de ação hoje.

## Ajuste antes de usar

- Workflow agendado: `<nome do workflow de E2E>`
- Formato do ID de teste nos títulos: `<ex.: QA-123>`
- Onde o resumo é entregue: `<canal ou DM>`

## Limites

Esta skill só lê. Não altera o repo, não faz push, não cria ticket e não reexecuta o run. Se uma correção parecer óbvia, descreva-a no resumo e pare.

## Passos

1. **Ache os dois runs.** Liste os runs agendados do workflow. O mais novo é HOJE, o anterior é a BASE.

   ```bash
   gh run list --workflow "<workflow>" --event schedule --limit 10 --json databaseId,conclusion,createdAt
   ```

   Se HOJE ainda estiver rodando, diga isso e pare.

2. **Run verde?** Diga que está verde, mande o link e pare.

3. **Baixe só os logs que falharam**, dos dois runs.

   ```bash
   gh run view <ID> --log-failed > hoje.log
   ```

4. **Extraia os testes que falharam por módulo.** Compare pelo ID do teste, nunca pelo nome do browser ou do sistema operacional, porque a matriz pode variar de um dia para o outro.

5. **Leia `known-red-tests.md` e `known-traps.md`** em `references/test-investigation/` antes de diagnosticar qualquer coisa.

6. **Classifique cada falha:**

   | Classe    | Critério                                                              |
   | --------- | --------------------------------------------------------------------- |
   | Conhecida | Está em `known-red-tests.md` com a mesma assinatura de erro           |
   | Nova      | Não falhou na BASE e não é conhecida                                  |
   | Recorrente| Falhou na BASE também, e ainda não tem dono                           |
   | Flaky     | Falhou e passou no retry                                              |
   | Cascata   | Um teste anterior do mesmo arquivo falhou e este depende do dado dele |
   | Ambiente  | Erro 5xx, timeout de rede, credencial expirada, serviço fora          |

7. **Para cada falha nova ou recorrente**, leia o primeiro bloco de erro (locator, mensagem, trecho de código) e escreva a assinatura em uma linha.

8. **Agrupe por causa.** Dez testes com o mesmo erro são uma causa, não dez.

## Formato do resumo

No máximo 20 linhas.

```
❌ Nightly AAAA-MM-DD: N falhas em M módulos (X novas)
<link do run>

*Novas, precisam de ação*
- <ID> · <assinatura do erro> · <próximo passo sugerido>

*Já conhecidas* (só as que ainda falham)
- <ID> · <referência>

*Flaky*
- <IDs>

*Resolvidas* (conhecidas que pararam de falhar)
- <ID>
```

Mantenha títulos de teste e mensagens de erro no idioma original.

## Ao terminar

Se uma falha conhecida parou de acontecer, avise: a entrada dela em `known-red-tests.md` pode sair.
