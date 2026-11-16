# Claude Code

A instalação original da aula continua funcionando:

1. Copie `.claude/` da raiz do kit para a raiz do seu repo de testes. Mescle com o conteúdo existente.
2. Adapte os campos **Ajuste antes de usar**.
3. Abra o repo no Claude Code e chame `/triage-nightly`, `/qa-pr-review` ou outra skill pelo nome.

O pacote traz 8 skills e dois arquivos de memória. [Documentação oficial](https://code.claude.com/docs/en/skills).

Para contribuir com este kit, edite `skills/` e `references/` na raiz da distribuição e execute `python3 scripts/exportar.py`. A pasta `.claude/` distribuída é gerada dessas fontes. Depois de instalar no seu projeto, personalize normalmente os arquivos instalados; ao atualizar, compare as mudanças para preservar suas adaptações.
