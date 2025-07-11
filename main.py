from model.cadastro import Cliente
from database.banco import salvar_arquivo

# dados do cliente
print("-----------------")
print()
print("Dados cliente")

nome = input("Nome: ")
cpf = input("CPF: ")

print()
print("-----------------")

#chamando classe que amarzena os valores do cliente
usuario = Cliente(nome, cpf)

#Salvamento dos dados no arquivo
salvar_arquivo(usuario.to_dict())

