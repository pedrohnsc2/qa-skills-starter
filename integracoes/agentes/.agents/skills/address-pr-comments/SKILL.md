---
name: address-pr-comments
description: "Trata os comentários de review de um pull request. Lista as threads abertas, dá um veredito para cada uma e, depois da aprovação, corrige o código ou responde. Use quando alguém disser \"responde os comentários do PR\", \"o revisor pediu mudanças\" ou passar o link de um PR com review pendente."
---

<!-- Gerado por scripts/exportar.py; edite skills/ na distribuição. -->

# Tratar comentários de PR

## Passos

1. **Confirme a branch.** A branch local é a do PR? Está atualizada com o remoto? Se não, pare e avise.

2. **Liste as threads não resolvidas.** Ignore as resolvidas e as desatualizadas pelo diff.

3. **Para cada thread, leia o código citado** e dê um veredito:

   | Veredito      | Quando                                                        |
   | ------------- | ------------------------------------------------------------- |
   | Corrigir      | O revisor tem razão                                           |
   | Já resolvido  | Um commit posterior já tratou. Cite o commit                  |
   | Responder     | É uma pergunta, ou a abordagem atual tem um motivo            |
   | Discordar     | A mudança pedida quebraria algo. Explique com evidência       |
   | Precisa de você | Decisão de produto ou de escopo, que não é técnica          |

4. **Mostre a tabela e pare.** Espere a aprovação antes de mexer em qualquer coisa.

   ```
   | # | Arquivo:linha | Pedido resumido | Veredito | O que vou fazer |
   ```

5. **Depois do ok:**
   - Faça as correções.
   - Rode os testes afetados, sem retry.
   - Um commit com as correções. Push normal, sem force.
   - Responda cada thread em uma ou duas linhas: o que mudou e em qual commit, ou o motivo de não mudar.

6. **Peça nova revisão** só se você pedir.

## Limites

- Não marque thread como resolvida. Quem resolve é o revisor.
- Não responda "feito" sem o commit já estar no remoto.
- Ao discordar, seja direto e curto. Sem defensiva e sem texto longo.
