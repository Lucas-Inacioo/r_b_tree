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
        y = x.right
        x.right = y.left

        if y.left != self._nil:
            y.left.parent = x

        y.parent = x.parent

        if x.parent == self._nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y


    def _right_rotate(self, y: Node) -> None:
        """
        Rotaciona a árvore à direita.

        Parâmetros:
        y: Node - Nó a ser rotacionado.
        """
        x = y.left
        y.left = x.right

        if x.right != self._nil:
            x.right.parent = y

        x.parent = y.parent

        if y.parent == self._nil:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x

    def _insert_fixup(self, z: Node) -> None:
        """
        Corrige a árvore após a inserção de um nó.

        Parâmetros:
        z: Node - Nó a ser corrigido.
        """
        while z.parent.color == RED and z.parent != self._nil:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self._left_rotate(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._left_rotate(z.parent.parent)
        self.root.color = BLACK

    def traverse_in_order(self, x: Node, alt: int = 0) -> None:
        """
        Percorre a árvore em ordem.

        Parâmetros:
        x: Node - Nó atual.
        alt: int - Altura atual.
        """
        if x != self._nil:
            self.traverse_in_order(x.right, alt + 1)
            print(f'{3 * alt * " "}{x}')
            self.traverse_in_order(x.left, alt + 1)

    @property
    def root(self) -> Node:
        """
        Retorna a raiz da árvore.
        """
        return self._root

    @root.setter
    def root(self, root: Node) -> None:
        """
        Define a raiz da árvore.
        """
        self._root = root

    @property
    def nil(self) -> Node:
        """
        Retorna o nó nulo.
        """
        return self._nil
