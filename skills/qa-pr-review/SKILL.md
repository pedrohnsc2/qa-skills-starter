---
name: qa-pr-review
description: "Revisa um pull request de testes automatizados e rascunha o review no chat, separando o que bloqueia do que é opcional. Use quando alguém disser \"revisa o PR 123\", \"dá uma olhada nesse PR de teste\" ou passar um link de PR para avaliar."
---

# Review de PR de testes

O review responde a duas perguntas: **o teste verifica o que o caso de teste pede?** e **ele vai continuar passando daqui a um mês?**

## Ajuste antes de usar

- Onde ficam os casos de teste escritos: `<ferramenta ou pasta>`
- Regras do repo que o review deve cobrar: `<arquivo de convenções>`

## Limites

**Nada é postado sem autorização.** O review é escrito no chat. Só depois de um "pode postar" ele vai para o PR, e vai como comentário, nunca como aprovação ou pedido de mudança em nome de alguém.

## Passos

1. **Leia o PR inteiro:** descrição, diff, comentários já feitos. Não repita o que outro revisor já apontou.

2. **Leia o caso de teste escrito** de cada teste novo ou alterado.

3. **Para cada teste, confira:**

   | Pergunta                                                     | Se não            |
   | ------------------------------------------------------------ | ----------------- |
   | Cada resultado esperado do caso tem uma asserção?            | Bloqueia          |
   | A asserção falharia se o bug voltasse?                       | Bloqueia          |
   | O teste cria os próprios dados?                              | Bloqueia          |
   | Depende de ordem de execução ou de outro teste?              | Bloqueia          |
   | Tem espera por tempo fixo?                                   | Bloqueia          |
   | Seletor frágil (posição, XPath longo, texto que muda)?       | Opcional, sugira  |
   | Helper duplicado de um que já existe?                        | Opcional, sugira  |
   | Nome e título seguem a convenção?                            | Opcional          |

4. **Confira o plano de teste do PR.** Há evidência de que o teste rodou e passou? Sem retry?

5. **Verifique cada achado antes de escrever.** Abra o arquivo e confirme a linha. Um comentário errado custa mais do que um comentário a menos.

## Formato do rascunho

```
## PR #<n> · <título>

**Veredito:** <pronto | precisa de ajuste>

### Bloqueia
- `<arquivo>:<linha>` · <o problema> · <o que fazer>

### Opcional
- `<arquivo>:<linha>` · <sugestão>

### O que está bom
- <uma ou duas linhas, só se for verdade>
```

Se não houver nada que bloqueie, diga isso com clareza. Não invente achado para o review parecer completo.
