class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf 
        
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"CPF: {self.cpf}")
    
class Cadastro:
    def __init__(self):
        self.registros = []
        
    def adicionar_cadastro(self, pessoa):
        self.registros.append(pessoa)
        print("Registro realizado")
        
    def exibir_cadastro(self):
        print("Registros encontrados:")
        for pessoa in self.registros:
            pessoa.exibir_dados()
        
