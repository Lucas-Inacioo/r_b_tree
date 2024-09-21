"""
Módulo que contém a classe RBTree, que representa uma árvore rubro-negra.
"""

from node import Node, NodeStructure, RED, BLACK

class RBTree:
    """
    Classe que representa uma árvore rubro-negra.

    Atributos:
    """
    def __init__(self) -> None:
        """
        Inicializa a árvore rubro-negra.
        """
        self._nil = Node(NodeStructure(None, None, None, None, BLACK))
        self._root = self._nil

    def insert(self, key: int) -> None:
        """
        Insere um nó na árvore rubro-negra.

        Parâmetros:
        key: int - Valor do nó a ser inserido.
        """

    def _left_rotate(self, x: Node) -> None:
        """
        Rotaciona a árvore à esquerda.

        Parâmetros:
        x: Node - Nó a ser rotacionado.
        """

    def _right_rotate(self, x: Node) -> None:
        """
        Rotaciona a árvore à direita.

        Parâmetros:
        x: Node - Nó a ser rotacionado.
        """

    def _insert_fixup(self, z: Node) -> None:
        """
        Corrige a árvore após a inserção de um nó.

        Parâmetros:
        z: Node - Nó a ser corrigido.
        """

    def _traverse_in_order(self, x: Node, alt: int = 0) -> None:
        """
        Percorre a árvore em ordem.

        Parâmetros:
        x: Node - Nó atual.
        alt: int - Altura atual.
        """
