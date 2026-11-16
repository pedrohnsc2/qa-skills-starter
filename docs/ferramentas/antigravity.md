# Google Antigravity

1. Abra o workspace do seu repositório de testes.
2. Copie `integracoes/agentes/.agents/` deste kit para `.agents/` na raiz do workspace, preservando arquivos existentes.
3. Adapte as configurações das skills e confira os arquivos em `.agents/references/test-investigation/`.
4. Peça: `Use a skill triage-nightly para comparar estas execuções. Não altere nada; entregue o relatório no chat.`

O pacote contém as 8 skills. A documentação atual usa `.agents/skills/` no workspace do App, CLI e IDE; no IDE, confira as skills em **Customizations**. [Documentação oficial](https://antigravity.google/docs/skills).

A mesma variante atende Codex; se as duas ferramentas usam o mesmo repo, mantenha uma única cópia. Instalar instruções não configura conexões com CI, Jira ou Slack. Teste primeiro com dados de exemplo, e só depois conecte as fontes reais.
