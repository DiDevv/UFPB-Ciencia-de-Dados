# Main: #Aluno: Diogo Dias da Silva
# Nº de matrícula: 20220028795

from table import criar_tabela, add_linha, rem_linha, add_col, rem_col, soma_col, media_colunas, exibir_tabela, abrir_csv, condicao_idade_maior_que_25, filtrar

# Criação da Tabela
nomes_colunas = ['nome', 'idade']
valores = [['joão', 'maria', 'josé'], [20, 28, 19]]
minha_tabela = criar_tabela(nomes_colunas, valores)

# Adicionando uma nova coluna
nome_col_nova1 = 'cidade'
valores_col_nova1 = ["São Paulo", "Rio de Janeiro", "Recife"]
add_col(minha_tabela, nome_col_nova1, valores_col_nova1)

# Exibindo a tabela original
print("Tabela Original:")
exibir_tabela(minha_tabela)

# Removendo uma linha
rem_linha(minha_tabela, 2)

# Exibindo a tabela após a remoção da linha
print("\nTabela após a remoção da terceira linha:")
exibir_tabela(minha_tabela)

# Calculando e exibindo a soma das colunas
print("\nSoma das colunas:")
print(soma_col(minha_tabela))

# Calculando e exibindo a média das colunas
print("\nMédia das colunas:")
print(media_colunas(minha_tabela))

# Abrindo um arquivo CSV
nome_arquivo_csv = 'teste.csv'
tabela_csv = abrir_csv(nome_arquivo_csv)

# Exibindo a tabela do CSV
print("\nTabela do arquivo CSV:")
exibir_tabela(tabela_csv)

# Filtrando a tabela
print("\nTabela filtrada (idade maior que 25):")
tabela_filtrada = filtrar(minha_tabela, condicao_idade_maior_que_25)
exibir_tabela(tabela_filtrada)
