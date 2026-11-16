---
name: create-pr
description: "Leva as mudanças locais até um pull request aberto: nome de branch, commit, push e PR com descrição e plano de teste. Use quando alguém disser \"abre o PR\", \"manda isso para review\" ou \"cria o PR dessa mudança\"."
---

# Criar PR

## Ajuste antes de usar

- Branch base: `<ex.: main>`
- Padrão de nome de branch: `<ex.: iniciais/id-do-ticket-descricao-curta>`
- Padrão de título: `<ex.: "[ID-123] Descrição no imperativo">`
- Labels obrigatórios: `<lista, ou nenhum>`
- PR nasce em draft? `<sim | não>`

## Argumentos opcionais

- Branch base diferente da padrão.
- Link ou ID do ticket.

## Passos

1. **Veja o estado.** `git status` e `git diff`. Se não houver mudança, diga e pare.

2. **Confira o que vai entrar.** Liste os arquivos. Se aparecer algo que não deveria ir (arquivo `.env`, credencial, log, artefato de teste), pare e pergunte.

3. **Branch.** Se estiver na branch base, crie uma no padrão. Se já estiver numa branch de trabalho, use a atual.

4. **Rode o lint e o type check.** Se falhar, corrija antes de commitar.

5. **Commit.** Mensagem curta no imperativo dizendo o que mudou e por quê. Um commit por mudança lógica.

6. **Push** com `-u origin <branch>`.

7. **Abra o PR.** Se o repo tiver template de PR, siga os títulos dele. Senão, use:

   ```markdown
   ## O que muda
   <duas ou três linhas>

   ## Por quê
   <o problema, com o link do ticket>

   ## Plano de teste
   | Commit | O que rodei | Resultado |
   | ------ | ----------- | --------- |
   | <sha>  | <comando ou link do run> | <passou N/N> |

   ## Observações
   <o que o revisor precisa saber: risco, o que ficou de fora>
   ```

8. **Devolva o link do PR.**

## Limites

- Nunca faça force push sem perguntar.
- Nunca faça push direto na branch base.
- O plano de teste só lista o que foi rodado de verdade. Se nada foi rodado, escreva isso.
