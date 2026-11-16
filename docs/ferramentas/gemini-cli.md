# Gemini CLI

1. Copie `integracoes/gemini-cli/.gemini/` para `.gemini/` na raiz do repo de testes, preservando arquivos existentes.
2. Adapte os campos das skills e a memória em `.gemini/references/test-investigation/`.
3. Inicie uma sessão no repo e confira com `/skills list`.
4. Peça: `Use triage-nightly para comparar <runs>. Só leia e entregue o relatório aqui.` Revise a confirmação de ativação que a ferramenta apresentar.

Gemini CLI descobre skills em `.gemini/skills/` e aceita `.agents/skills/`. Instale só uma variante. Se já usa o pacote compartilhado de Codex/Antigravity, aproveite essa instalação. [Documentação oficial](https://geminicli.com/docs/cli/skills/).

As 8 skills estão disponíveis no pacote. O terminal e os serviços precisam de acesso configurado separadamente. Para o Gemini no navegador, use o [guia web](gemini.md): não é a mesma instalação.
