# Testes vermelhos de propósito

Testes que falham por um motivo conhecido e ainda sem correção. A triagem e a investigação leem este arquivo antes de diagnosticar, para não refazer o mesmo trabalho todo dia.

**Regras:**

- Uma entrada só vale se a **assinatura do erro** for a mesma. Se o teste falhar com outro erro, é uma falha nova.
- Toda entrada tem um ticket ou um dono. Sem isso, não é "conhecido", é "ignorado".
- Quando o teste voltar a passar, remova a entrada no mesmo PR.

| Teste     | Assinatura do erro                          | Motivo                                   | Ticket ou dono | Desde      |
| --------- | ------------------------------------------- | ---------------------------------------- | -------------- | ---------- |
| `<ID>`    | `<mensagem de erro, uma linha>`             | `<bug de produto, ambiente, dependência>`| `<link>`       | AAAA-MM-DD |

<!-- Exemplo:
| QA-123 | `expect(locator).toBeVisible()` no botão "Enviar" | Bug de produto: botão some com filtro ativo | BUG-456 | 2026-01-15 |
-->
