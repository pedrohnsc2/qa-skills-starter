# Primeiro exercício: entender uma nightly que falhou

Escolha uma execução encerrada e um workflow conhecido. A primeira rodada deve produzir só um relatório.

## Preparar

1. Escolha o [guia da sua ferramenta](../README.md) e copie somente a variante correspondente para o repo. Mescle os arquivos sem sobrescrever suas configurações. Os caminhos abaixo exemplificam Claude Code; nos outros pacotes, use `.cursor/`, `.agents/` ou `.gemini/` conforme o guia.
2. Em `.claude/skills/triage-nightly/SKILL.md`, preencha workflow e formato dos IDs. Deixe o relatório no chat nesta primeira rodada.
3. Revise os modelos de memória em `.claude/references/test-investigation/`. Os exemplos não são problemas reais do seu projeto.
4. Confira se você tem acesso aos logs e ao run anterior. Não coloque tokens nos arquivos do kit.

## Pedir

```text
/triage-nightly
Analise esta execução: <link do run>.
Compare com a execução agendada anterior do mesmo workflow.
Entregue o relatório aqui no chat. Não altere arquivos, não reexecute testes,
não envie mensagens e não crie tickets.
Se faltar acesso ou evidência, diga o que não foi possível verificar.
```

## Conferir o resultado

- Os links e commits são os runs corretos?
- A comparação usa IDs de teste, não nomes de browsers?
- Falhas agrupadas têm evidência da mesma causa?
- Um teste conhecido só foi tratado como resolvido se realmente executou e passou?
- Dúvidas e limitações de acesso aparecem no relatório?

O objetivo é sair de uma lista de falhas para causas prováveis e próximos passos verificáveis. Você continua responsável por conferir as evidências.

## Depois da primeira rodada

Escolha uma falha para `/investigate-failing-test` ou ajuste a triagem ao seu contexto. Só transforme o fluxo em rotina depois de validar manualmente o resultado, a origem dos dados e o destino do relatório.

Os modelos em `rotinas/` precisam ser configurados e agendados na ferramenta que você usa. O arquivo sozinho não executa a rotina. No modelo de email, substitua qualquer declaração de autorização pelo escopo que você efetivamente aprovou; confira também o prazo de recuperação da lixeira do seu provedor.
