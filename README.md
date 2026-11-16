# IA no dia a dia de QA — kit de skills

Um ponto de partida para usar o Claude Code no dia a dia de QA: skills, modelos de rotina e arquivos de memória. Nada aqui depende de uma empresa ou produto específico. Tudo foi escrito para ser adaptado.

Material de apoio da videoaula **IA no dia a dia de QA: skills, rotinas e agentes na prática**, de Pedro Henrique.

▶️ [Assistir à videoaula no YouTube](https://youtu.be/lEjRHYNlm7w)

> O vídeo pode ainda estar privado enquanto a publicação é preparada.

## Comece aqui

1. [Baixe o kit em ZIP](https://github.com/pedrohnsc2/qa-skills-starter/archive/refs/heads/main.zip) ou clone este repositório.
2. Siga a instalação abaixo e adapte os campos da skill escolhida.
3. Faça o [primeiro exercício](docs/primeiro-exercicio.md): triagem de uma execução sem alterar código.

## Pré-requisitos

- Claude Code, para carregar a estrutura `.claude/skills/` fornecida neste kit.
- Um repositório de testes e acesso aos logs das execuções.
- GitHub CLI (`gh`) autenticado, quando a skill usar os exemplos de GitHub Actions ou PRs.
- Conectores de tickets, email ou chat apenas nos fluxos que precisarem dessas ferramentas.

Os arquivos são modelos em Markdown, não um serviço instalado: clonar o kit não agenda tarefas nem conecta ferramentas. Em outro assistente, adapte o formato de instalação e os comandos.

## O que tem aqui

```
.claude/
├── skills/
│   ├── triage-nightly/           # Triagem do run noturno de E2E
│   ├── investigate-failing-test/ # Descobre por que um teste falhou e corrige ou reporta
│   ├── new-e2e-test/             # Cria um teste novo no padrão do repo
│   ├── create-pr/                # Branch, commit, push e PR de uma vez
│   ├── qa-pr-review/             # Rascunha o review de um PR de testes
│   ├── address-pr-comments/      # Responde e resolve comentários de review
│   ├── file-qa-bug/              # Transforma achados em bugs bem escritos
│   └── qa-status-update/         # Monta o update para a daily ou a semanal
└── references/
    └── test-investigation/
        ├── known-red-tests.md    # Testes vermelhos de propósito
        └── known-traps.md        # Armadilhas que já enganaram uma investigação
rotinas/
├── triagem-nightly.md            # Prompt pronto para agendar
└── triagem-email.md              # Prompt pronto para agendar
```

## Como instalar

1. Copie a pasta `.claude/` para a raiz do seu repo de testes (ou junte com a que já existe).
2. Abra os `SKILL.md` que tiverem campos de configuração e preencha a seção **Ajuste antes de usar**. Os trechos entre `<...>` são seus.
3. Faça commit. Quem clonar o repo já recebe as skills.
4. Chame pelo nome: `/create-pr`, `/triage-nightly`, e assim por diante.

As rotinas em `rotinas/` não são skills. São prompts completos para colar em uma tarefa agendada. Leia os dois antes de agendar: eles dizem o que a rotina pode e não pode fazer.

## Regra, skill, agente ou rotina?

| Peça   | Quando usar                                                        |
| ------ | ------------------------------------------------------------------ |
| Regra  | Deve valer toda vez que alguém mexe em certo tipo de arquivo       |
| Skill  | Um fluxo que você chama quando quer                                |
| Agente | Trabalho pesado de leitura, que merece um contexto só dele         |
| Rotina | Um prompt completo que roda com horário, sem ninguém do outro lado |

## Três conselhos

- **Comece pelo que você repete.** Triagem de falha, update de status e review de PR costumam ser os primeiros.
- **Faça uma vez conversando, depois transforme em skill.** A skill boa nasce de uma conversa que deu certo, não de uma folha em branco.
- **Escreva os limites.** Leia os limites do fluxo escolhido. A triagem só lê; a investigação pode editar testes; `/create-pr` inclui commit, push e abertura de PR quando você pede esse fluxo. Publicação de reviews, tickets e updates tem suas próprias etapas de confirmação.

## Memória

O agente não lembra da conversa de ontem. O que foi aprendido precisa virar arquivo. Por isso existem `known-red-tests.md` e `known-traps.md`: atualize os dois no mesmo PR em que você descobriu a coisa.
