# Gemini no navegador

O caminho mais simples é colar um [prompt universal](../../prompts/README.md) no chat e anexar os logs, diff ou registros pedidos. Essa opção funciona sem instalar os pacotes de terminal.

## Se sua conta mostrar Skills

Disponibilizamos três pastas em `integracoes/gemini-web/`: `triage-nightly`, `qa-pr-review` e `qa-status-update`. Cada uma contém `SKILL.md` na raiz e referências; são versões de análise no chat, sem execução de comandos.

Na área **Skills**, escolha criar por upload e envie uma dessas pastas, ou um ZIP contendo o conteúdo dela. Revise as instruções antes de criar. Não envie o ZIP do repositório inteiro como se fosse uma única skill. [Instruções oficiais de importação](https://support.google.com/gemini/answer/17094296).

## Se sua conta ainda mostrar Gems

Use o conteúdo do prompt universal escolhido como instruções de um Gem e adicione as fontes necessárias. O Google documenta uma transição de Gems para Skills, cuja disponibilidade varia por conta. [Guia oficial da transição](https://support.google.com/gemini/answer/18560919).

Nenhuma dessas opções concede acesso ao seu terminal ou ao repo local. Para executar tarefas no projeto, veja [Gemini CLI](gemini-cli.md).
