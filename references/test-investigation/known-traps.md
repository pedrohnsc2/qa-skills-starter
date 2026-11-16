# Armadilhas conhecidas

Mecanismos de falha que já fizeram uma investigação ir na direção errada. Não é uma lista de testes: é uma lista de **enganos**.

Acrescente uma entrada sempre que você perder tempo por causa de um sintoma que apontava para a causa errada. Faça isso no mesmo PR da correção.

## Modelo

### <nome curto da armadilha>

- **Parece:** <o sintoma, como aparece no log>
- **Na verdade é:** <a causa real>
- **Como confirmar:** <o comando ou a checagem que distingue>
- **O que fazer:** <a ação certa>

## Exemplos para começar

### Timeout que é dado faltando

- **Parece:** timeout esperando um elemento aparecer.
- **Na verdade é:** a pré-condição não foi criada, porque a chamada de API de setup falhou em silêncio.
- **Como confirmar:** procure a resposta da chamada de setup no log, antes do timeout.
- **O que fazer:** faça o helper de setup falhar alto quando a API não retorna sucesso.

### Passa no retry

- **Parece:** teste flaky.
- **Na verdade é:** dependência de ordem. O teste só passa depois que outro criou o dado.
- **Como confirmar:** rode o teste sozinho, sem retry, num ambiente limpo.
- **O que fazer:** faça o teste criar o próprio dado.

### Erro 5xx no meio do teste

- **Parece:** bug de produto.
- **Na verdade é:** ambiente de teste instável ou em deploy.
- **Como confirmar:** veja se outros testes sem relação falharam no mesmo minuto.
- **O que fazer:** não mexa no teste. Reporte como ambiente e rode de novo depois.

### Falha só em um browser

- **Parece:** bug específico do browser.
- **Na verdade é:** diferença de tempo de renderização que expõe uma espera mal escrita.
- **Como confirmar:** rode nos outros browsers com a rede mais lenta.
- **O que fazer:** troque a espera por tempo por uma espera por condição.
