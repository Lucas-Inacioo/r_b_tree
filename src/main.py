"""
    Implementação de uma árvore rubro-negra em Python.
    Feito por Lucas Gomes Inacio.
    Número USP: 12562091
    
    Usando extensão Pylint (ms-python.pylint) no Visual Studio Code.
    https://pylint.readthedocs.io/en/latest/index.html

    Usando Github Copilot para auxiliar na escrita do código.

    Histórico de versões e código melhor formatado em arquivos distintos:
    https://github.com/Lucas-Inacioo/r_b_tree
"""

from r_b_tree import RBTree

def main() -> None:
    """
    Função principal.
    """
    # Inicializa a árvore rubro-negra.
    tree = RBTree()

    # Insere os valores 10, 20, 30, 15, 25, 35, 5, 1, 40, 50.
    values = [10, 20, 30, 15, 25, 35, 5, 1, 40, 50]
    for value in values:
        tree.insert(value)

    # Imprime a árvore.
    tree.traverse_in_order(tree.root)

if __name__ == '__main__':
    main()
