from datetime import datetime

from Entities.Cliente import Cliente
from Entities.Pedido import Pedido
from Entities.PedidoProduto import PedidoProduto
from Entities.Produto import Produto
from Repositories.ClienteRepository import ClienteRepository
from Repositories.ProdutoRepository import ProdutoRepository


def test_new_order_with_product_total_price():
    # Arrange
    cliente = Cliente(1, "Jefté")
    cliente_repository = ClienteRepository()
    cliente_repository.adicionar_cliente(cliente)

    product1 = Produto(1, "Milk", 50, 10)
    product_repository = ProdutoRepository()
    product_repository.adicionar_produto(product1)

    pedido = Pedido(1, cliente, datetime.today)
    order_product1 = PedidoProduto()
    order_product1.adicionar_produto(product1, 5)
    pedido.adicionar_produto_pedido(order_product1)

    # Act
    pedido.atualizar_preco_total()

    # Assert
    assert pedido.valor_total == 250


def test_new_order_without_product():
    # Arrange
    cliente = Cliente(1, "Jefté")
    cliente_repository = ClienteRepository()
    cliente_repository.adicionar_cliente(cliente)

    product1 = Produto(1, "Milk", 50, 10)
    produto_repository = ProdutoRepository()
    produto_repository.adicionar_produto(product1)

    pedido = Pedido(1, cliente, datetime.today)
    pedido_produto = PedidoProduto()
    pedido_produto.adicionar_produto(product1, 15)
    pedido.adicionar_produto_pedido(pedido_produto)

    # Act
    pedido.atualizar_preco_total()

    # Assert
    assert pedido.valor_total == 0

def test_unitario_baixar_estoque():
    # Arrange
    pedido = Produto(1, "Teste", 12, 10)

    # Act
    pedido.baixar_estoque(5)

    # Assert
    assert type(pedido.estoque) == int

def test_integracao_baixar_estoque():
    # Arrange
    pedido = Produto(1, "Teste", 12, 17)

    # Act
    pedido.baixar_estoque(5)

    #A ssert
    assert pedido.estoque == 12

def test_integracao_processar_pedido():
    # Arrange
    produto = Produto(1, "Teste", 12, 20)
    pedido = PedidoProduto()

    # Act
    pedido.processar_pedido(produto, 3)

    # Assert
    assert pedido.valor_item == 36
