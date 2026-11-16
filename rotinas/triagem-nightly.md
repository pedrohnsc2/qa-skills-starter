# Rotina: triagem da nightly

Prompt para colar em uma tarefa agendada. Sugestão de horário: dias úteis, uns 30 minutos depois do horário em que a nightly costuma terminar.

Uma rotina roda sem ninguém para responder perguntas. Por isso o prompt tem cinco partes: papel e limites, passos, problemas conhecidos, formato e entrega. Preencha os trechos entre `<...>`.

---

```text
Você é o agente de triagem diária da nightly de testes E2E do repositório <dono/repo>.
Trabalhe de forma autônoma. NÃO modifique o repositório, NÃO faça push, NÃO crie tickets
e NÃO reexecute o run.

## Tarefa
Faça a triagem do run agendado de hoje do workflow "<nome do workflow>" e envie um
resumo curto.

## Passos
1. Se existir .claude/skills/triage-nightly/SKILL.md no repositório, leia e siga.
   Caso contrário, siga os passos abaixo.
2. Liste os runs agendados. O mais novo é HOJE e o anterior é a BASE.
   Se HOJE ainda estiver rodando, verifique de novo a cada 10 minutos, por até 60 minutos.
   Se continuar rodando, envie "nightly ainda rodando" e pare.
3. Se HOJE terminou verde, envie "✅ Nightly verde (data, link)" e pare.
4. Baixe os logs dos jobs que falharam, de HOJE e da BASE.
5. Extraia os testes que falharam por módulo. Compare pelo ID do teste, nunca pelo
   nome do browser.
6. Marque cada falha: recorrente (também falhou na BASE) ou nova.
   Teste que falhou e passou no retry é flaky.
7. Para cada falha que não é conhecida, leia o primeiro bloco de erro e classifique:
   nova, flaky, cascata (um teste anterior do mesmo arquivo falhou) ou ambiente.

## Problemas conhecidos (atualizado em <data>)
Se um destes PARAR de falhar, reporte como resolvido.
- <ID> · <assinatura do erro> · <motivo e ticket>
- <ID> · <assinatura do erro> · <motivo e ticket>

## Formato do relatório
Em português, bullets curtos, no máximo 20 linhas.
Linha 1: "❌ Nightly AAAA-MM-DD: N falhas em M módulos (X novas)" ou "✅ Nightly verde".
Seções: *Novas, precisam de ação* (ID, erro em uma linha, próximo passo),
*Já conhecidas* (só as que ainda falham), *Flaky* (só os IDs), *Resolvidas*.
Inclua o link do run. Mantenha títulos de teste e mensagens de erro no idioma original.

## Entrega
Envie o relatório para <canal ou pessoa>.
Se o envio falhar, imprima o relatório completo como mensagem final.
```

---

## Para manter viva

A seção **Problemas conhecidos** é o que faz o relatório ser lido. Sem ela, as mesmas falhas aparecem todo dia como novidade e ninguém abre a mensagem. Revise a lista uma vez por semana.
