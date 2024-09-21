"""
    Implementação de uma árvore rubro-negra em Python.
    Feito por Lucas Gomes Inacio.
    Número USP: 12562091
    
    Usando extensão Pylint (ms-python.pylint) no Visual Studio Code.
    https://pylint.readthedocs.io/en/latest/index.html
    
    Usando Github Copilot para auxiliar na escrita do código.

    Histórico de versões:
    https://github.com/Lucas-Inacioo/r_b_tree
"""

from __future__ import annotations
import dataclasses

@dataclasses.dataclass
class Node:
    """
    Classe que representa um nó de uma árvore rubro-negra.
    Utilizado dataclasses por não precisar de métodos especiais.
    """
    key: int
    color: bool
    parent: Node
    left: Node
    right: Node

def main():
    """
    Função principal, deve testar a implementação da árvore rubro-negra.
    """

if __name__ == '__main__':
    main()
