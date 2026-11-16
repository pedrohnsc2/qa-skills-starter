# Prompts universais para QA

Escolha um arquivo, copie seu conteúdo para ChatGPT, Gemini, Claude ou outro chat e forneça as evidências. São procedimentos de análise; não prometem acesso ao repo, execução de testes ou integração com serviços.

| Tarefa | Prompt | O que fornecer |
|---|---|---|
| Triar falhas | [triage-nightly](triage-nightly.md) | Run atual/anterior, logs, retries e problemas conhecidos |
| Revisar testes | [qa-pr-review](qa-pr-review.md) | Diff, arquivos, casos de teste e evidências de execução |
| Preparar status | [qa-status-update](qa-status-update.md) | Período, PRs, tickets, runs e bloqueios |

Comece com o [exemplo fictício](../docs/exemplo-triagem.md), sem conectar nenhuma conta. Campos `<...>` devem ser preenchidos ou marcados como não aplicáveis. Se não puder anexar Markdown na sua interface, cole o texto.

Os prompts incluem o mesmo procedimento das skills e uma camada que troca ações de ferramentas pela análise das evidências fornecidas. Referências como `known-red-tests.md` são arquivos a fornecer, não fontes que o chat acessa automaticamente.
