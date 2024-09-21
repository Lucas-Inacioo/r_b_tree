"""
Módulo que contém a classe NodeStructure, 
que representa a estrutura de um nó de uma árvore rubro-negra.
"""

from __future__ import annotations

from dataclasses import dataclass

RED = True
BLACK = False

@dataclass
class NodeStructure:
    """
    Classe que representa a estrutura de um nó de uma árvore rubro-negra.

    Atributos:
    key: int - Valor do nó.
    parent: Node - Nó pai.
    left: Node - Nó filho à esquerda.
    right: Node - Nó filho à direita.
    color: bool - Cor do nó, True para vermelho e False para preto.
    """
    key: int
    parent: Node = None
    left: Node = None
    right: Node = None
    color: bool = RED

class Node:
    """
    Classe que representa um nó de uma árvore rubro-negra.
    """
    def __init__(
            self,
            data: NodeStructure,
            ) -> None:
        """
        Inicializa um nó da árvore rubro-negra.
        """
        self._key = data.key
        self._parent = data.parent
        self._left = data.left
        self._right = data.right
        self._color = data.color

    def __str__(self) -> str:
        """
        Retorna uma representação em string do nó, incluindo chave e cor.
        """
        color = "Red" if self._color else "Black"
        return f'Node({self._key}, {color})'

    @property
    def key(self) -> int:
        """
        Retorna a chave do nó.
        """
        return self._key

    @property
    def parent(self) -> Node:
        """
        Retorna o nó pai.
        """
        return self._parent

    @parent.setter
    def parent(self, parent: Node) -> None:
        """
        Define o nó pai.
        """
        self._parent = parent

    @property
    def left(self) -> Node:
        """
        Retorna o nó filho à esquerda.
        """
        return self._left

    @left.setter
    def left(self, left: Node) -> None:
        """
        Define o nó filho à esquerda.
        """
        self._left = left

    @property
    def right(self) -> Node:
        """
        Retorna o nó filho à direita.
        """
        return self._right

    @right.setter
    def right(self, right: Node) -> None:
        """
        Define o nó filho à direita.
        """
        self._right = right

    @property
    def color(self) -> bool:
        """
        Retorna a cor do nó.
        """
        return self._color

    @color.setter
    def color(self, color: bool) -> None:
        """
        Define a cor do nó.
        """
        self._color = color
