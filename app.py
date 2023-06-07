class Produto:
    def __init__(self, codigo, nome, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        
    def atualizar_quantidade(self, quantidade):
        self.quantidade += quantidade
        
    def exibir_detalhes(self):
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Quantidade: {self.quantidade}")
        
class Estoque:
    def __init__(self):
        self.produtos = []
        
    def cadastrar_produto(self, produto):
        self.produtos.append(produto)
        print("Produto cadastrado ao estoque")
        
    def remover_produto(self, produto):
        if produto in self.produtos:
            self.produtos.remove(produto)
            print("Produto removido do estoque")
        else:
            print("O produto não está no estoque")
            
    def exibir_estoque(self):
        print("Produtos no estoque")
        for produto in self.produtos:
            produto.exibir_detalhes()
            

produto1 = Produto("001", "Camiseta", 10)


estoque = Estoque()

estoque.cadastrar_produto(produto1)

estoque.exibir_estoque()