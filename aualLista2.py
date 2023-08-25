galera = [['joao', 26], ['carlos', 18]]
print(type(galera))
print(galera[0])
nome = galera[0][0]
idade = galera[0][1]
print("nome:",nome,"Idade:",idade)

del galera[1]
print(galera)

#Podemos usar o operador "IN" para consultar se um elemento esta presente em uma lista

print(26 in galera[0])
