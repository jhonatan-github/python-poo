from classes import Produto, Estoque

codigo = input('Código: ')
nome = input('Nome: ')
qtd = input('Quantidade: ')

produto = Produto(codigo, nome, qtd)

estoque = Estoque()
estoque.cadastrar_produto(produto)


