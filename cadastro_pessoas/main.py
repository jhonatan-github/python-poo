from classes import  Pessoa, Cadastro

nome = input('nome ')
idade = input('idade ')
cpf = input('CPF ')

registro = Pessoa(nome, idade, cpf)

cadastro = Cadastro()
cadastro.adicionar_cadastro(registro)

cadastro.exibir_cadastro()