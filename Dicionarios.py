#CRIAÇÃO DE DICIONARIOS
estudantes = {"Matheus":25, "Bruno":29}
print(estudantes)
estudantes.clear()#Limpa o dicionario
#del estudantes #deletoa o dicionario
estudantes2 = {"Matheus":29, "Bruno":29}
len(estudantes2) #retorna o tamanho

estudantes.update(estudantes2) #atualizo o dicionario adicionando o primeiro nele

estudantes2["matheusP"]=33
print(estudantes2)