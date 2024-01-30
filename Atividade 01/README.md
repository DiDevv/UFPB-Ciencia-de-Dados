
---

# Exercício - Tabela

**Professor:** Yuri Malheiros

## Objetivo:

O objetivo deste exercício é criar um módulo chamado `table` que possui funções para trabalhar com tabelas.

## Detalhes iniciais

Uma tabela possui linhas e colunas. No módulo `table`, as colunas podem ter nomes, mas as linhas são indexadas apenas por números (0 - primeira linha; 1 - segunda linha; 2 - terceira linha, etc). Assim, uma tabela vai ser representada por um dicionário. As chaves são os nomes das colunas e os valores são listas que representam cada linha de uma determinada coluna.

```python
tabela = {'nome': ['joão', 'maria', 'josé'], 'idade': [20, 21, 19]}
```

## Requisitos

O módulo `table` precisa das seguintes funcionalidades:

- **Criar tabela:** dada uma lista de nomes de colunas e uma matriz de valores, criar uma tabela na forma especificada anteriormente.

- **Adicionar linha:** adicionar uma linha na tabela dada uma lista de valores.

- **Remover linha:** remover uma linha dado o seu índice.

- **Adicionar coluna:** adicionar uma coluna dado um nome e uma lista de valores.

- **Remover coluna:** remover uma coluna dado o seu nome.

- **Soma:** somar os valores das colunas da tabela. Deve ser retornada uma soma por coluna. Se a coluna não tiver valores numéricos, essa coluna deve ser ignorada.

- **Média:** calcular média dos valores das colunas. Deve ser retornada uma média por coluna. Se a coluna não tiver valores numéricos, essa coluna deve ser ignorada.

- **Exibir tabela:** imprimir a tabela na tela.

- **Abrir CSV:** dado um arquivo CSV, criar uma nova tabela.

- **Filtrar:** filtrar as linhas que satisfazem uma condição. Dica: passar uma função como parâmetro dessa função que retorna True se a condição for satisfeita e False se não for.

## Observações

- Em diversas funções, a quantidade de elementos passados precisa estar de acordo com as dimensões da tabela. Se as dimensões não forem adequadas, um erro deverá ser retornado.

- Os resultados das funções devem ser retornados pela função, não é para imprimir. A única função que deve usar print é a função de exibir tabela.

## Entrega

Este exercício pode ser feito em dupla ou individualmente. Você deve entregar dois arquivos:

- `table.py` - implementação do módulo.
- `main.py` - arquivo mostrando o uso de cada uma das funções implementadas.

No topo de cada arquivo, coloque um comentário com os nomes de matrículas. Envie os arquivos para o meu e-mail ou pelo Discord.

---
