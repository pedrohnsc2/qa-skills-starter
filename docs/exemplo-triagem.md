# Exercício sem ferramentas: triagem de dois runs fictícios

Copie o prompt [triage-nightly](../prompts/triage-nightly.md) em um chat e envie os dados abaixo. Todos os IDs, resultados e erros são inventados para o exercício.

```text
Workflow: E2E. Módulo: checkout. IDs: QA-NNN. Saída: neste chat.
BASE: 2026-11-10, commit exemplo-a, concluído.
ATUAL: 2026-11-11, commit exemplo-b, concluído.

Teste | BASE | ATUAL | Evidência atual
QA-101 | falhou | falhou | API de preparação de dados retornou HTTP 502
QA-102 | passou | falhou | A mesma API de preparação retornou HTTP 502
QA-103 | passou | passou no retry | Timeout ao esperar botão; passou na segunda tentativa
QA-104 | falhou | passou na primeira tentativa | Executou e passou

Conhecidos:
QA-101: HTTP 502 na API de preparação, dono: time do ambiente.
QA-104: filtro ausente, ticket fictício BUG-104.
Não há outros logs, traces ou histórico disponíveis.
Não existem links reais para estes runs.
```

## O que conferir na resposta

- QA-101 é conhecido pela assinatura; QA-102 é novo e pode compartilhar a causa. HTTP 502 sozinho não prova a causa raiz.
- QA-103 apresenta instabilidade observada, mas o retry não explica a origem.
- QA-104 tem evidência de execução aprovada, portanto pode ser listado como conhecido resolvido.
- A resposta não inventa links, tickets reais, reexecuções ou consultas.
- Não confunda dois testes com uma única causa provável.

Não há uma resposta textual única. Avalie as evidências, os limites e a utilidade dos próximos passos.
