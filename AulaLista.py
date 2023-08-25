num = [3, 6, 9, 7]
num[2] = 8
num.append(4)#insere o elemnto
num.insert(2, 5)#insere um elemento a lista one primeiro passamos a posição e segundo passamos o elemento
num.sort()#Ordena a lista
print(len(num))#retorna o tamanho da lista
num.pop(1)#Retira o item da lista
print(num)
print(f'esta lista tem {len(num)} elementos')
print(max(num))#Retorna o maior termo dentro da lista
print(min(num))#Retorna o menor termo dentro da lista

print(f'O numero 7 aparece {num.count(7)} vez na lista')#retorna quantas vezes o numero aparece na lista

print(f'o indice do elemento 8 e {num.index(8)}')
