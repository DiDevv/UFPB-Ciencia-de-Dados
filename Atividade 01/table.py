#Aluno: Diogo Dias da Silva
#Nº de matrícula: 20220028795

#Função para a criação de tabela
def criar_tabela(nomes_colunas, valores):
    if len(nomes_colunas) != len(valores):
        raise ValueError("O número de colunas não corresponde ao número de valores fornecidos.")
    
    tabela = {}
    for nome_coluna, valores_coluna in zip(nomes_colunas, valores):
        tabela[nome_coluna] = valores_coluna
    
    return tabela

#Função para a adição de linhas
def add_linha(tabela, valores):
    if len(tabela) != len(valores):
        raise ValueError("O número de colunas da tabela não corresponde ao número de valores fornecidos.")
    
    for coluna, valor in zip(tabela.values(), valores):
        coluna.append(valor)

#Função para a remoção de linhas
def rem_linha(tabela, valores):
    if len(tabela) != len(valores):
        raise ValueError("O número de colunas da tabela não corresponde ao número de valores fornecidos.")
    
    for coluna, valor in zip(tabela.values(), valores):
        coluna.remove(valor)

# Função para adicionar colunas
def add_col(tabela, nome_coluna, valores):
    if len(valores) != len(next(iter(tabela.values()))):
        raise ValueError("O número de valores fornecidos não corresponde ao número de linhas na tabela.")
    
    tabela[nome_coluna] = valores

# Função para remover colunas
def rem_col(tabela, nome_coluna):
    if nome_coluna not in tabela:
        raise ValueError("A coluna especificada não existe na tabela.")
    
    tabela.pop(nome_coluna)
    






