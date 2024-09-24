"""
    Testes para a implementação da árvore rubro-negra.
"""
import sys
import os

# Adiciona o caminho do diretório 'src' ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from r_b_tree import RBTree
from node import Node, NodeStructure, RED, BLACK


def test_balanced_insertion():
    """
    Testa uma inserção que não requer rotação.
    """
    tree = RBTree()

    # Inserindo em ordem que não requer rotações
    tree.insert(10)
    tree.insert(20)
    tree.insert(5)

    # Verificar se a raiz é preta
    assert tree.root.color == BLACK

    # Verificar as cores e chaves
    assert tree.root.key == 10
    assert tree.root.left.key == 5
    assert tree.root.right.key == 20

    assert tree.root.left.color == RED
    assert tree.root.right.color == RED


def test_left_rotation():
    """
    Testa uma inserção que requer rotação à esquerda.
    """
    tree = RBTree()

    # Ordem que força uma rotação à esquerda
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)  # Isso deve causar rotação à esquerda

    # Verificar se a nova raiz é 20 após a rotação
    assert tree.root.key == 20
    assert tree.root.left.key == 10
    assert tree.root.right.key == 30

    # Verificar as cores
    assert tree.root.color == BLACK
    assert tree.root.left.color == RED
    assert tree.root.right.color == RED


def test_right_rotation():
    """
    Testa uma inserção que requer rotação à direita.
    """
    tree = RBTree()

    # Ordem que força uma rotação à direita
    tree.insert(30)
    tree.insert(20)
    tree.insert(10)  # Isso deve causar rotação à direita

    # Verificar se a nova raiz é 20 após a rotação
    assert tree.root.key == 20
    assert tree.root.left.key == 10
    assert tree.root.right.key == 30

    # Verificar as cores
    assert tree.root.color == BLACK
    assert tree.root.left.color == RED
    assert tree.root.right.color == RED


def test_color_and_height():
    """
    Verifica as propriedades de cores e altura após múltiplas inserções.
    """
    tree = RBTree()

    # Inserindo múltiplos valores
    keys = [10, 20, 30, 15, 25, 35, 5, 1, 40, 50]
    for key in keys:
        tree.insert(key)

    # Verificar se a raiz é preta
    assert tree.root.color == BLACK

    # Verificar a altura e as cores de alguns nós críticos
    assert tree.root.left.left.left.key == 1
    assert tree.root.left.left.left.color == RED  # Nó 1 deve ser vermelho

    assert tree.root.right.right.key == 40
    assert tree.root.right.right.color == BLACK  # Nó 40 deve ser preto

    assert tree.root.right.left.key == 25
    assert tree.root.right.left.color == BLACK  # Nó 25 deve ser preto


def test_node_structure_initialization():
    """
    Testa a inicialização de NodeStructure.
    """
    # Inicializa um NodeStructure com valores padrão
    node_structure = NodeStructure(key=10)

    assert node_structure.key == 10
    assert node_structure.parent is None
    assert node_structure.left is None
    assert node_structure.right is None
    assert node_structure.color == RED  # Cor padrão é vermelho


def test_node_initialization():
    """
    Testa a inicialização de Node com NodeStructure.
    """
    # Cria um NodeStructure e usa ele para inicializar um Node
    node_structure = NodeStructure(key=10)
    node = Node(node_structure)

    assert node.key == 10
    assert node.parent is None
    assert node.left is None
    assert node.right is None
    assert node.color == RED  # Cor padrão é vermelho


def test_node_color_change():
    """
    Testa a alteração da cor de um Node.
    """
    # Inicializa um nó com cor vermelha (padrão)
    node_structure = NodeStructure(key=10)
    node = Node(node_structure)

    # Verifica se a cor inicial é vermelha
    assert node.color == RED

    # Altera para preto e verifica
    node.color = BLACK
    assert node.color == BLACK


def test_node_relationships():
    """
    Testa a definição de parent, left e right nos nós.
    """
    parent_structure = NodeStructure(key=20)
    left_structure = NodeStructure(key=10)
    right_structure = NodeStructure(key=30)

    parent_node = Node(parent_structure)
    left_node = Node(left_structure)
    right_node = Node(right_structure)

    # Define o relacionamento entre os nós
    parent_node.left = left_node
    parent_node.right = right_node
    left_node.parent = parent_node
    right_node.parent = parent_node

    # Verifica se as relações foram definidas corretamente
    assert parent_node.left.key == 10
    assert parent_node.right.key == 30
    assert left_node.parent.key == 20
    assert right_node.parent.key == 20


def test_node_str_representation():
    """
    Testa a representação de string de um Node.
    """
    node_structure_red = NodeStructure(key=10, color=RED)
    node_structure_black = NodeStructure(key=20, color=BLACK)

    node_red = Node(node_structure_red)
    node_black = Node(node_structure_black)

    # Verifica a representação em string, o nó vermelho deve ser vermelho e o preto, preto
    assert str(node_red) == '\033[91m10\033[0m'  # 91 é o código ANSI para vermelho
    assert str(node_black) == '\033[30m20\033[0m'  # 30 é o código ANSI para preto

if __name__ == "__main__":
    pytest.main()
