#Aluno: Diogo Dias da Silva
#Nº de matrícula: 20220028795

#Biblioteca padrão do python para lidar com csv
import csv

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
def rem_linha(tabela, indice):
    if indice >= len(next(iter(tabela.values()))):
        raise ValueError("O índice fornecido está fora do intervalo válido.")
    
    for coluna in tabela.values():
        del coluna[indice]


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
    
def soma_col(tabela):
    soma_por_coluna = {}
    
    for nome_coluna, valores_coluna in tabela.items():
        # Verifica se todos os valores na coluna são numéricos
        valores_numericos = [valor for valor in valores_coluna if isinstance(valor, (int, float))]
        if valores_numericos:
            soma_por_coluna[nome_coluna] = sum(valores_numericos)
    return soma_por_coluna

# Função para calcular a média dos valores das colunas numéricas
def media_colunas(tabela):
    media_por_coluna = {}
    for nome_coluna, valores_coluna in tabela.items():
        # Filtra os valores numéricos na coluna
        valores_numericos = [valor for valor in valores_coluna if isinstance(valor, (int, float))]
        if valores_numericos:
            media_por_coluna[nome_coluna] = sum(valores_numericos) / len(valores_numericos)
    return media_por_coluna


# Função para exibir a tabela na tela
def exibir_tabela(tabela):
    # Imprime os nomes das colunas
    colunas = list(tabela.keys())
    print('\t'.join(colunas))

    # Imprime os valores das colunas linha por linha
    num_linhas = len(next(iter(tabela.values())))  # Obtém o número de linhas
    for i in range(num_linhas):
        linha = [str(tabela[coluna][i]) for coluna in colunas]
        print('\t'.join(linha))



# Função para abrir um arquivo CSV e criar uma nova tabela
# Função para abrir um arquivo CSV e criar uma nova tabela
def abrir_csv(nome_arquivo):
    tabela = {}
    with open(nome_arquivo, newline='', encoding='utf-8') as csvfile:  # Adicionando encoding='utf-8'
        leitor_csv = csv.reader(csvfile)
        cabecalho = next(leitor_csv, None)  # Lê o cabeçalho
        if cabecalho is not None:
            for nome_coluna in cabecalho:
                tabela[nome_coluna] = []
            
            for linha in leitor_csv:
                if len(linha) == len(cabecalho):  # Verifica se o número de valores na linha é igual ao número de colunas
                    for i, valor in enumerate(linha):
                        tabela[cabecalho[i]].append(valor)
                else:
                    print(f"Aviso: A linha {linha} tem um número diferente de valores do que o cabeçalho. Ignorando esta linha.")
    return tabela

def filtrar(tabela, condicao):
    linhas_filtradas = {coluna: [] for coluna in tabela}  # Inicializa um dicionário vazio para armazenar as linhas filtradas
    
    for i in range(len(tabela[next(iter(tabela))])):
        linha_atual = {coluna: tabela[coluna][i] for coluna in tabela}  # Obtém a linha atual como um dicionário de coluna: valor
        if condicao(linha_atual):  # Verifica se a condição é satisfeita para a linha atual
            for coluna, valor in linha_atual.items():
                linhas_filtradas[coluna].append(valor)  # Adiciona os valores da linha filtrada ao dicionário
    
    return linhas_filtradas


# Função de condição para filtrar apenas linhas com idade maior que 25
def condicao_idade_maior_que_25(linha):
    return linha['idade'] > 25









