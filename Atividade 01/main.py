#Aluno: Diogo Dias da Silva
#Nº de matrícula: 20220028795

from table import criar_tabela, add_linha, rem_linha, add_col, rem_col


#Criação da Tabela
nomes_colunas = ['nome', 'idade']
valores = [['joão', 'maria', 'josé'], [20, 21, 19]]

minha_tabela = criar_tabela(nomes_colunas, valores)

print(minha_tabela, "Tabela Criada!")

#Adicionando Linha
nova_linha = ['diogo', 19]
add_linha(minha_tabela, nova_linha)
print(minha_tabela, "Linha adicionada")

#Removendo Linha
remover_linha = ['maria', 21]
rem_linha(minha_tabela, remover_linha )
print(minha_tabela, "Linha removida")

#Adicionando Coluna
nome_col_nova = 'cidade'
valores_nova_col = ['São Paulo', 'Rio de Janeiro', 'Goiana']
add_col(minha_tabela, nome_col_nova, valores_nova_col)
print(minha_tabela, f"coluna {nome_col_nova} adicionada")

#Removendo Coluna
nome_col = 'cidade'
rem_col(minha_tabela, nome_col)
print(minha_tabela, f"coluna {nome_col} removida")
