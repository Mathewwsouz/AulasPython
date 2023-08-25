#REVISÂO CONDICIONAIS E ESTRUTURAS DE REPETIÇÃO

nome = input("Qual seu nome? ")
sexo = input("Qual seu sexo")
sexo.upper()
if sexo == "M" or sexo == "m":
    print("Boa tarde Senhor {}".format(nome))
elif sexo == "F" or sexo == "f":
    print("Boa tarde Senhora {}".format(nome))
else:
        print("Boa tarde Senhore {}".format(nome))