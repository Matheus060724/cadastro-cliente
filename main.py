from model.cadastro import Cliente
from database.banco import salvar_arquivo


nome = input("Nome: ")
cpf = input("CPF: ")

usuario = Cliente(nome, cpf)

salvar_arquivo(usuario.to_dict())

