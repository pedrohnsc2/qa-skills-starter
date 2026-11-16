# Compatibilidade, fontes e validação

Documentação consultada em **16/11/2026**. Interfaces, planos e versões podem variar. Se sua instalação não reconhecer uma skill, confira o guia oficial da ferramenta ou use o prompt universal no chat.

| Ferramenta | Base usada para preparar este kit |
|---|---|
| Claude Code | [Skills de projeto e invocação](https://code.claude.com/docs/en/skills) |
| Cursor | [Skills, diretórios e descoberta](https://cursor.com/docs/skills) |
| Antigravity | [Skills por superfície: App, CLI e IDE](https://antigravity.google/docs/skills) |
| Gemini CLI | [Descoberta, aliases e ativação](https://geminicli.com/docs/cli/skills/) |
| Gemini web | [Importar/criar Skills](https://support.google.com/gemini/answer/17094296) e [transição de Gems](https://support.google.com/gemini/answer/18560919) |
| Codex | [Skills locais e nomes duplicados](https://learn.chatgpt.com/docs/build-skills) |
| ChatGPT | [Projetos, arquivos e instruções](https://learn.chatgpt.com/docs/projects) |

## O que foi validado nesta distribuição

- Metadados e nomes dos 8 procedimentos principais.
- Consistência dos 4 pacotes de arquivos para agentes de código.
- Geração dos 3 prompts e das 3 Skills de análise para Gemini web.
- Presença dos arquivos de memória referenciados nos pacotes.
- Links relativos e ausência de alterações manuais divergentes nas saídas geradas.

Não foi feito teste de execução dentro de cada produto. Este é um kit de instruções preparado segundo os formatos documentados. Disponibilidade de conectores, autenticação, agendamento e execução depende da sua conta e ambiente.

## Como atualizar

Edite `skills/` e `references/`, depois rode o gerador e o validador indicados no README. Os exemplos de chat são derivados das mesmas skills, com uma instrução de escopo que limita o trabalho à análise das evidências fornecidas.

Evite instalar todas as variantes no mesmo repo. Algumas ferramentas reconhecem diretórios de outras ferramentas; os mesmos nomes podem aparecer duplicados ou ter precedência diferente. Os guias indicam a variante a copiar.
