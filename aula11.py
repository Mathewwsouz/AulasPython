print('\033[7::47m -----------SIMULAÇÃO DE EMPRESTIMO----------')
nome = input(' DIGITE SEU NOME: ')
valorCasa = float (input('DIGITE O VALOR DA CASA: '))
salario = float(input('qual a sua media salarial Srª {} :' .format(nome)))
anos = int(input('EM QUANTOS ANOS PRETENDE PAGAR O FINANCIAMENTO: '))
parcelas = anos * 12
porctSalario = (salario*30)/100
valorParcela = valorCasa/parcelas

float(valorParcela)
float(porctSalario)

if valorParcela > porctSalario:
    print('EMPRESIMO NEGADO POIS O VALOR DA PARCELA NO TOTAL DE {:.5f}, EXCEDE O VALOR  DE 30% DO SEU SALARIO QUE NO CASO É {:.5f}. ' .format(float(valorParcela), float(porctSalario)))
else:
    print('ANALISE DE EMPRESTIMO APROVADA!! PROCURE UMA AGÊNCIA CREDENCIADA.')