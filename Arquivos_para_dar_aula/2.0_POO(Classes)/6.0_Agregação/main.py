from classe import CarrinhoDeCompras, Produto


carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 60)
p2 = Produto('Celular', 1500)
p3 = Produto('Caneca', 20)

carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p1)

carrinho.lista_produtos()
carrinho.soma_total()
