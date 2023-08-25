#criando classe
class Funcionario():

  def __init__(self, nome, salario, cargo):
    self.nome = nome
    self.salario = salario
    self.cargo = cargo

  def listafuncionario(self):
    print(f"Funcionario: {self.nome} Salario: {self.salario} cargo:{self.cargo}")
#Dicionario em lista

def MenuInicial():
  print("Menu de opções")
  print('1-cadastrar funcionario')
  print('2-listar funcionario')
  print('0-Encerrar')
  opc = int(input())
  return opc

opc = MenuInicial()
funcionarios = []

def cadastrarFuncioario():
  if opc == 1:
    nome = input('Digite o nome do funcinario')
    salario = float(input('digite o salari:'))
    Cargo = input('qual o carho do funcionario')
    Funcionario = { 'Nome':nome, 'Salario':salario , 'Cargo' : Cargo}
    funcionarios.append(Funcionario)
while True:
    if opc == 1:
      while True:
          cadastrarFuncioario()
          opc2 = input('deseja cadastrar mais um funcionario')
          if opc2 == 's':
            cadastrarFuncioario()
          else:
            print('processo finalizado')
          break

    elif opc == 2:
      for funcionario in funcionarios:
        Funcionario.listafuncionario()
    else:
      print("Operação finalizada")
    break