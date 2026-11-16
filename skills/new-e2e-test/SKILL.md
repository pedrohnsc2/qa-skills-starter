---
name: new-e2e-test
description: "Cria um teste E2E novo seguindo o padrão do repo, a partir de um caso de teste escrito. Use quando alguém pedir \"automatiza o caso X\", \"cria o spec para esse cenário\" ou passar um ID de caso de teste para automatizar."
---

# Novo teste E2E

Um teste novo deve parecer que foi escrito pela mesma pessoa que escreveu os vizinhos. Antes de escrever, leia.

## Ajuste antes de usar

- Pasta dos testes: `<ex.: tests/<feature>/>`
- Pasta dos seletores ou page objects: `<caminho>`
- Pasta dos helpers de API para preparar dados: `<caminho>`
- Convenção do título do teste: `<ex.: "QA-123: descrição">`
- Comando para rodar um teste só: `<comando>`

## Pergunte antes de começar

Só o que não der para descobrir sozinho:

1. Qual é o caso de teste (ID ou texto)?
2. Em qual feature ou módulo ele entra?
3. É teste de UI ou de API?

## Passos

1. **Leia o caso de teste inteiro.** Pré-condições, passos e resultado esperado. Se algum resultado esperado for vago ("funciona corretamente"), pergunte.

2. **Leia dois ou três testes vizinhos** da mesma feature. Copie a estrutura deles: fixtures, imports, como criam dados, como limpam.

3. **Prepare os dados por API, não pela tela.** A UI é para o comportamento que o teste verifica. Tudo que é pré-condição vai por helper de API. Se o helper não existe, crie um e diga isso.

4. **Cada teste cria o que precisa.** Não dependa de dado deixado por outro teste nem da ordem de execução.

5. **Seletores:** reaproveite os que existem. Para um novo, prefira papel e nome acessível ou um atributo de teste. Evite XPath longo e seletor por posição.

6. **Esperas:** espere por uma condição (elemento visível, resposta de rede, estado), nunca por tempo fixo.

7. **Asserções:** uma por resultado esperado do caso de teste. Se o caso tem três resultados esperados, o teste tem pelo menos três asserções.

8. **Rode duas vezes, sem retry.**

   ```bash
   <comando do teste> --retries=0
   ```

9. **Rode o lint e o type check** do repo.

## Ao terminar, diga

- O arquivo criado e os helpers ou seletores novos.
- O resultado das duas execuções.
- Qualquer passo do caso de teste que você não conseguiu automatizar, e por quê.

Não abra PR aqui. Para isso, use `/create-pr`.
