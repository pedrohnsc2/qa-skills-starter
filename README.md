# Kit de IA para QA — prompts, skills e rotinas

Material de apoio da aula **IA no dia a dia de QA: skills, rotinas e agentes na prática**, de Pedro Henrique.

▶️ [Assistir à videoaula](https://youtu.be/lEjRHYNlm7w) · [Baixar o kit em ZIP](https://github.com/pedrohnsc2/qa-skills-starter/archive/refs/heads/main.zip)

Use IA para triagem de falhas, review de testes e status de QA. Comece em um chat com arquivos anexados ou instale as skills no assistente que trabalha no seu repositório. Os exemplos são genéricos e precisam ser adaptados ao seu projeto.

## Escolha sua ferramenta

| Ferramenta | Começar por | O que o kit oferece |
|---|---|---|
| ChatGPT | [Guia](docs/ferramentas/chatgpt.md) | 3 prompts universais e instruções de Projeto |
| Gemini no navegador | [Guia](docs/ferramentas/gemini.md) | 3 prompts e versões para importar como Skills, quando disponíveis |
| Cursor | [Guia](docs/ferramentas/cursor.md) | 8 skills em `.cursor/skills/` |
| Google Antigravity | [Guia](docs/ferramentas/antigravity.md) | 8 skills em `.agents/skills/` |
| Gemini CLI | [Guia](docs/ferramentas/gemini-cli.md) | 8 skills em `.gemini/skills/` |
| Codex | [Guia](docs/ferramentas/codex.md) | 8 skills em `.agents/skills/` |
| Claude Code | [Guia](docs/ferramentas/claude.md) | As 8 skills originais em `.claude/skills/` |
| Outro chat | [Prompts universais](prompts/README.md) | Copiar, colar e fornecer evidências |

Não precisa instalar Python para usar os arquivos prontos. A matriz descreve os pacotes e os formatos documentados, não uma certificação de execução em todas as ferramentas. Consulte [compatibilidade e fontes](docs/compatibilidade.md).

## Experimente em cinco minutos

1. Abra o [prompt de triagem](prompts/triage-nightly.md) e cole em um chat.
2. Envie o [exemplo fictício](docs/exemplo-triagem.md).
3. Confira as causas prováveis e as lacunas apontadas.
4. Depois, use logs reais que você tenha autorização para compartilhar.

Para trabalhar no repositório, siga o [primeiro exercício com uma nightly](docs/primeiro-exercicio.md) e o guia da sua ferramenta. Copie só a variante escolhida e preserve configurações que já existem.

## Os oito procedimentos

| Skill | Resultado |
|---|---|
| [triage-nightly](skills/triage-nightly/SKILL.md) | Compara runs e agrupa falhas por causa provável |
| [investigate-failing-test](skills/investigate-failing-test/SKILL.md) | Investiga e distingue teste, produto e ambiente |
| [new-e2e-test](skills/new-e2e-test/SKILL.md) | Escreve teste seguindo o padrão do projeto |
| [create-pr](skills/create-pr/SKILL.md) | Prepara branch, commit, push e PR |
| [qa-pr-review](skills/qa-pr-review/SKILL.md) | Rascunha revisão com evidências |
| [address-pr-comments](skills/address-pr-comments/SKILL.md) | Trata comentários de review após alinhamento |
| [file-qa-bug](skills/file-qa-bug/SKILL.md) | Prepara bugs reproduzíveis para registro aprovado |
| [qa-status-update](skills/qa-status-update/SKILL.md) | Monta status a partir de resultados registrados |

As versões de chat desta primeira expansão cobrem triagem, review e status. Os demais fluxos dependem de ferramentas e estão nos pacotes para agentes de código.

## Rotinas e memória

- [Triagem da nightly](rotinas/triagem-nightly.md) e [triagem de email](rotinas/triagem-email.md): modelos para configurar em um agendador compatível.
- [Testes conhecidos](references/test-investigation/known-red-tests.md) e [armadilhas](references/test-investigation/known-traps.md): memória editável do projeto.

Clonar o kit não agenda nada e não conecta GitHub, Jira, Slack ou email. Revise escopo, acesso e destino da saída e rode manualmente antes de agendar. No modelo de email, confirme as autorizações e o prazo de recuperação com seu provedor. Falha de acesso não significa caixa limpa ou nightly aprovada.

## Antes de usar no trabalho

Preencha `<...>`, confira convenções e use os comandos apropriados ao seu runner. `gh` e opções como `--retries=0` são exemplos de ferramentas específicas, não exigências de todo projeto. Nunca inclua credenciais nos arquivos.

Leia os limites de cada fluxo: triagem só lê; investigação pode editar testes; criar PR inclui operações no Git. No modo chat, os três prompts entregam somente análises e rascunhos. Verifique as evidências antes de agir.

## Estrutura e manutenção

`skills/` e `references/` são as fontes principais. `.claude/`, os pacotes em `integracoes/` e os três prompts são gerados a partir delas; os guias ficam em `docs/`.

Para contribuir com o kit (Python 3.9+):

```bash
python3 scripts/exportar.py
python3 scripts/exportar.py --check
python3 scripts/validar.py
```

O gerador escreve somente os arquivos distribuídos neste kit. Ele não instala ferramentas, não acessa a rede e não modifica seus outros repositórios. Depois de copiar uma variante para seu projeto, personalize os arquivos instalados e compare o diff quando atualizar.
