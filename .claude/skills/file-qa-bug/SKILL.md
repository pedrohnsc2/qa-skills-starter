---
name: file-qa-bug
description: "Transforma achados de uma sessão de teste em bugs bem escritos no gerenciador de tickets, depois de revisar cada um com a pessoa. Use quando alguém disser \"abre os bugs\", \"registra esses achados\" ou terminar uma rodada de testes com problemas para reportar."
---

<!-- Gerado por scripts/exportar.py; edite skills/ na distribuição. -->

# Registrar bugs de QA

Um bug bom pode ser reproduzido por alguém que nunca viu a tela. O resto é detalhe.

## Ajuste antes de usar

- Gerenciador de tickets: `<ferramenta>`
- Projeto padrão: `<chave>`
- Campos obrigatórios: `<ex.: componente, severidade, ambiente>`
- Labels padrão: `<lista>`

## Passos

1. **Apresente os achados em linguagem simples**, um por linha, numerados. Sem jargão de log.

2. **Para cada achado, dê um veredito de escopo:**

   | Veredito          | Significado                                              |
   | ----------------- | -------------------------------------------------------- |
   | Bug               | O produto faz diferente do que foi especificado          |
   | Fora de escopo    | Comportamento antigo, sem relação com o que foi testado  |
   | Dúvida de spec    | A especificação não diz o que deveria acontecer          |
   | Não reproduzido   | Aconteceu uma vez e não voltou                           |

3. **Procure duplicados** antes de propor um ticket novo. Se existir, proponha um comentário no ticket existente.

4. **Pergunte uma vez:** quais achados registrar, em qual projeto e sob qual épico.

5. **Crie um ticket por vez** e confira se foi criado antes de passar para o próximo.

## Modelo do ticket

**Título:** `<onde> · <o que acontece>`, sem "bug" e sem "erro" no título.

```markdown
## Resumo
<uma frase>

## Ambiente
<ambiente, browser, usuário ou perfil, versão ou commit>

## Passos para reproduzir
1. <passo>
2. <passo>

## Resultado atual
<o que acontece, com a mensagem de erro exata>

## Resultado esperado
<o que deveria acontecer, com a fonte: spec, caso de teste, design>

## Evidência
<screenshot, trecho de log, requisição e resposta>

## Observações
<frequência, impacto, o que já foi descartado>
```

## Limites

- Nenhum ticket é criado sem aprovação explícita daquele achado.
- Não inclua senha, token ou dado pessoal real na evidência. Mascare.
- Severidade é proposta, não decidida. Quem decide é o time.
