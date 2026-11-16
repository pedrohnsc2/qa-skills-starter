---
name: qa-status-update
description: "Monta o update de status de QA a partir do que de fato aconteceu: PRs mergeados, tickets movidos e resultado dos runs. Use quando alguém pedir \"update para a daily\", \"resumo da semana\", \"o que eu fiz ontem\" ou \"status para a reunião\"."
---

# Update de status de QA

O update sai de fontes, não da memória. Se não há registro de que algo aconteceu, não entra.

## Ajuste antes de usar

- Repositórios a consultar: `<lista>`
- Projeto no gerenciador de tickets: `<chave>`
- Onde o update é publicado: `<chat, página, documento>`
- Idioma do update: `<pt-BR | en>`

## Argumentos

- Período: `daily` (desde o último dia útil) ou `semanal` (últimos 7 dias). Padrão: `daily`.

## Passos

1. **PRs:** liste os que a pessoa abriu, mergeou ou revisou no período.

   ```bash
   gh pr list --author @me --state all --search "updated:>=<data>" --json number,title,state,mergedAt,url
   ```

2. **Tickets:** os que mudaram de status no período e os que estão em andamento.

3. **Runs:** o resultado do último run agendado e a tendência (melhorou, piorou, igual).

4. **Bloqueios:** o que está parado esperando outra pessoa, e desde quando.

5. **Agrupe por resultado, não por atividade.** "12 casos automatizados no módulo X" diz mais que "trabalhei em automação".

## Formato

Para a daily, no máximo 8 linhas:

```
*Feito*
- <resultado> (<link>)

*Em andamento*
- <o que> · <quanto falta>

*Bloqueado*
- <o que> · esperando <quem> desde <quando>
```

Para a semanal, acrescente no topo uma linha de números: testes automatizados, bugs registrados, estado da nightly.

## Limites

- Mostre o rascunho no chat. Só publique depois de um ok.
- Não arredonde para cima. Um PR aberto não é "entregue".
- Se uma fonte não respondeu, diga qual ficou de fora.
