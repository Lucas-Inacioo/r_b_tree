"""
Módulo que contém a classe NodeStructure, 
que representa a estrutura de um nó de uma árvore rubro-negra.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

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

    def __getattribute__(self, name: str) -> Any:
        """
        Retorna o valor de um atributo do nó.

        Parâmetros:
        name: str - Nome do atributo.
        """
        if name in ['_key', '_parent', '_left', '_right', '_color']:
            return object.__getattribute__(self, name)
        raise AttributeError(f"O atributo '{name}' não existe no nó.")
