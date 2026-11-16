# Rotina: triagem da caixa de entrada

Prompt para colar em uma tarefa agendada com acesso ao seu email. Sugestão de horário: todo dia, antes de você começar a trabalhar.

Quem trabalha com QA recebe muito email automático: notificação de ambiente de teste, de pipeline, de ferramenta. Esta rotina separa o ruído do que precisa de leitura.

**Antes de agendar, rode uma vez manualmente e confira o que foi para a lixeira.** Preencha os trechos entre `<...>`.

---

```text
Você faz a triagem diária da minha caixa de entrada. Trabalhe SÓ na caixa de entrada.
Seja conservador: na dúvida, NÃO apague. Deixe na caixa de entrada.

## Contexto
Sou QA. Minha caixa de entrada enche de notificações automáticas de ambiente de teste
e de newsletters. Já autorizei mandar essas duas categorias para a lixeira, que é
recuperável por 30 dias.

## Passo 1: limpar (mandar para a lixeira)
Para cada busca abaixo, mova as conversas encontradas para a lixeira.
Limite de segurança: 200 conversas por remetente por execução.
- Ruído de ambiente de teste: de <remetente automático 1>
- Ruído de ambiente de teste: de <remetente automático 2>
- Newsletters: de <domínio 1>, <domínio 2>

## Passo 2: organizar (aplicar marcador, sem tirar da caixa de entrada)
- de <notificações do repositório>      -> marcador "Trabalho/Código"
- de <notificações do gerenciador>      -> marcador "Trabalho/Tickets"
- de <alertas de monitoramento>         -> marcador "Alertas"
- convites e alterações de reunião      -> marcador "Trabalho/Reuniões"
Se não conseguir obter os marcadores, pule este passo sem erro.

## Nunca mande para a lixeira
- Qualquer email escrito por uma pessoa.
- Notificações de código, tickets e monitoramento.
- Convites de calendário.
- Códigos de verificação ou de login.
- Emails de RH, folha de pagamento ou financeiro.
- Alertas de segurança.

## Passo 3: resumo
No final, escreva um resumo curto: quantas conversas foram para a lixeira, por
categoria, e quantas foram marcadas. Se nada foi encontrado, diga que a caixa já
estava limpa.
```

---

## Por que o prompt é assim

- **Lista do que apagar é fechada.** A rotina só apaga o que está escrito, por remetente. Não decide sozinha o que é ruído.
- **Lista do que nunca apagar é explícita.** É a proteção para o dia em que um remetente novo parecer ruído.
- **Tem teto por execução.** Se uma busca estiver errada, o estrago é limitado.
- **Termina com um resumo.** É assim que você percebe quando ela começa a fazer algo estranho.
