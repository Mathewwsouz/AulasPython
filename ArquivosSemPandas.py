
#Abertura de dadaSets
#Abertura de dadaSets
with open("C:/Users/Mateus/Downloads/Receita_2022/Receita_2022.csv", "r", encoding="ISO-8859-1") as arquivo:
  conteudo = arquivo.read()

data = conteudo
rows =  data.split('\n')#Aqui dividimos o arquivo em linhas coma função split, e passamos para ela qual sera o cirterio de divisão
#print(rows)
arquivo.close()

#Dividir o arquivo em colunas
with open("C:/Users/Mateus/Downloads/Receita_2022/Receita_2022.csv", "r", encoding="ISO-8859-1") as arquivo:
  conteudo = arquivo.read()

data = conteudo
rows = data.split('\n')

full_data = []

for row in rows:
  split_row = row.split(',')
  full_data.append(split_row)

#contando o numero de linhas de um arquivo
count = 0

for row in rows:
  count += 1

print(count)


#for line in conteudo:
#  print(line)


