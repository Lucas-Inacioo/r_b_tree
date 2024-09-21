"""
Módulo que contém a classe RBTree, que representa uma árvore rubro-negra.
"""

from node import Node, NodeStructure, RED, BLACK

from typing import Any

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
        new_node = Node(NodeStructure(key, self._nil, self._nil, self._nil, RED))
        parent = self._nil
        actual = self._root

        while actual != self._nil:
            parent = actual
            if new_node.key < actual.key:
                actual = actual.left
            else:
                actual = actual.right

        new_node.parent = parent

        if parent == self._nil:
            self._root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        self._insert_fixup(new_node)

    def _left_rotate(self, x: Node) -> None:
        """
        Rotaciona a árvore à esquerda.

        Parâmetros:
        x: Node - Nó a ser rotacionado.
        """
        y = x._right
        x._right = y._left

        if y._left != self._nil:
            y._left._parent = x

        y._parent = x._parent

        if x._parent == self._nil:
            self._root = y
        elif x == x._parent._left:
            x._parent._left = y
        else:
            x._parent._right = y

        y._left = x
        x._parent = y


    def _right_rotate(self, y: Node) -> None:
        """
        Rotaciona a árvore à direita.

        Parâmetros:
        y: Node - Nó a ser rotacionado.
        """
        x = y._left
        y._left = x._right

        if x._right != self._nil:
            x._right._parent = y

        x._parent = y._parent

        if y._parent == self._nil:
            self._root = x
        elif y == y._parent._right:
            y._parent._right = x
        else:
            y._parent._left = x

        x._right = y
        y._parent = x

    def _insert_fixup(self, z: Node) -> None:
        """
        Corrige a árvore após a inserção de um nó.

        Parâmetros:
        z: Node - Nó a ser corrigido.
        """
        while z._parent._color == RED and z._parent != self._nil:
            if z._parent == z._parent._parent._left:
                y = z._parent._parent._right
                if y._color == RED:
                    z._parent._color = BLACK
                    y._color = BLACK
                    z._parent._parent._color = RED
                    z = z._parent._parent
                else:
                    if z == z._parent._right:
                        z = z._parent
                        self._left_rotate(z)
                    z._parent._color = BLACK
                    z._parent._parent._color = RED
                    self._right_rotate(z._parent._parent)
            else:
                y = z._parent._parent._left
                if y._color == RED:
                    z._parent._color = BLACK
                    y._color = BLACK
                    z._parent._parent._color = RED
                    z = z._parent._parent
                else:
                    if z == z._parent._left:
                        z = z._parent
                        self._right_rotate(z)
                    z._parent._color = BLACK
                    z._parent._parent._color = RED
                    self._left_rotate(z._parent._parent)
        self._root._color = BLACK

    def traverse_in_order(self, x: Node, alt: int = 0) -> None:
        """
        Percorre a árvore em ordem.

        Parâmetros:
        x: Node - Nó atual.
        alt: int - Altura atual.
        """
        if x != self._nil:
            self.traverse_in_order(x._right, alt + 1)
            print(f'{3 * alt * " "}{x}')
            self.traverse_in_order(x._left, alt + 1)
