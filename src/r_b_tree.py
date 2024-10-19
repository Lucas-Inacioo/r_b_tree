"""
    Módulo que contém a classe RBTree, que representa uma árvore rubro-negra.

    Feito por Lucas Gomes Inacio.
    Número USP: 12562091
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
            self._root = y
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
            self._root = x
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
        while z.parent.color == RED:
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
        self._root.color = BLACK

    def remove(self, key: int) -> None:
        """
        Remove um nó da árvore rubro-negra.

        Parâmetros:
        key: int - Valor do nó a ser removido.
        """
        z = self._search(key)
        if z == self._nil:
            return
        y = z
        y_original_color = y.color
        if z.left == self._nil:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self._nil:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == BLACK:
            self._remove_fixup(x)

    def _transplant(self, u: Node, v: Node) -> None:
        """
        Substitui um nó por outro na árvore.

        Parâmetros:
        u: Node - Nó a ser substituído.
        v: Node - Nó substituto.
        """
        if u.parent == self._nil:
            self._root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _minimum(self, x: Node) -> Node:
        """
        Retorna o nó com o menor valor na árvore.

        Parâmetros:
        x: Node - Nó a ser verificado.
        """
        while x.left != self._nil:
            x = x.left
        return x

    def _remove_fixup(self, x: Node) -> None:
        """
        Corrige a árvore após a remoção de um nó.

        Parâmetros:
        x: Node - Nó a ser corrigido
        """
        while x != self._root and x.color == BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self._left_rotate(x.parent)
                    x = self._root
            else:
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self._right_rotate(x.parent)
                    x = self._root
        x.color = BLACK

    def _search(self, key: int) -> Node:
        """
        Procura um nó na árvore.

        Parâmetros:
        key: int - Valor do nó a ser procurado.
        """
        x = self._root
        while x != self._nil and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

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
