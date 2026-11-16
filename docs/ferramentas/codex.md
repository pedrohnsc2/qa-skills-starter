# Codex

1. Copie `integracoes/agentes/.agents/` para `.agents/` no seu repositório de testes, mesclando arquivos existentes.
2. Preencha as configurações das skills que vai usar.
3. Abra o repo no Codex. Na CLI/extensão, use `/skills` ou `$` para localizar a skill. Se não aparecer após a cópia, reinicie a sessão.
4. Experimente: `Use a skill triage-nightly para analisar <run>. Só leitura e relatório no chat.`

Codex descobre skills locais em `.agents/skills/`. Evite cópias com o mesmo nome em múltiplos escopos. [Documentação oficial](https://learn.chatgpt.com/docs/build-skills).

O pacote inclui as 8 skills e a memória. Comandos e conectores precisam estar disponíveis no ambiente: este kit não instala CLI, não autentica contas e não concede permissões. Para análise de arquivos anexados no ChatGPT, veja o [outro guia](chatgpt.md).
