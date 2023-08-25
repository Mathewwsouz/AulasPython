lanche = 'hamburguer', 'suco', 'pizza'
Pessoas = ('carlos', 'pietro', 'Bruna')
#For
for cont in range (0, len(lanche)):
    print(f'hoje vou comer {lanche[cont]}')

#For aninhado
for i in Pessoas:
    for j in lanche:
        print("{} comera {}".format(i, j))

lista1= [1,2,3,4,5]
lista2 = [6,7,8,9]
soma = 0

for num in lista1 + lista2:
    if num % 2 == 0:
        soma += num
        print(soma)

print("a soma total dos pares é: {}".format(soma))

#WHILE COM PASS, BREAK E CONTINUES
valor = 0

while valor < 6:
    if valor ==3:
        print("Ja foi metade do laco")
        break
    else:
        pass
    print(valor)
    valor += 1
print("--------------------------------------------------")
#Gerar valores em intervalos com ranger

for i in range(1, 11):#Na declaração do range o segundo termo ser a marca de parada ou seja, nesse caso ele só ira até o 10
    if i % 2 == 0:
        print("> {} e par".format(i))
    else:
        print("> {} e impar".format(i))
