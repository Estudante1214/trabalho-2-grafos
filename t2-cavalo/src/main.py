import sys
import os

# Adiciona o diretório src ao caminho de busca do Python para facilitar importações
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from graph import Graph
from cc import ConnectedComponents
from cycle import CycleDetector
from bfs import BreadthFirstSearch

def read_graph(file_path):
    """Lê o grafo a partir de um arquivo no formato algs4."""
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            if not lines:
                return None
            
            V = int(lines[0].strip())
            E = int(lines[1].strip())
            g = Graph(V)
            
            for i in range(2, 2 + E):
                v, w = map(int, lines[i].split())
                g.add_edge(v, w)
            return g
    except FileNotFoundError:
        print(f"Erro: Arquivo {file_path} não encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None

def main():
    # Caminho do arquivo de entrada
    input_file = os.path.join(os.path.dirname(__file__), '..', 'dados', 'entrada.txt')
    
    # 1. Carregar o Grafo
    g = read_graph(input_file)
    if not g:
        return

    # 2. Exibir Lista de Adjacência
    print("--- Lista de Adjacência ---")
    print(g)

    # 3. Identificar Componentes Conexas
    cc = ConnectedComponents(g)
    print("--- Componentes Conexas ---")
    print(f"Número de componentes conexas: {cc.get_count()}")
    components = cc.get_components()
    for i, vertices in enumerate(components):
        print(f"Vértices da componente {i}: {' '.join(map(str, vertices))}")
    print()

    # 4. Calcular Distância Mínima entre (0,0) e (2,2)
    # (0,0) -> 0 e (2,2) -> 8
    bfs = BreadthFirstSearch(g, 0)
    dist = bfs.get_distance(8)
    print("--- Distância Mínima ---")
    print(f"Distância mínima entre (0,0) [Vértice 0] e (2,2) [Vértice 8]: {dist if dist != -1 else 'Inalcançável'}")
    print()

    # 5. Detecção de Ciclos
    cycle_det = CycleDetector(g)
    print("--- Análise de Ciclo ---")
    if cycle_det.has_cycle():
        print("O grafo possui ciclo: Sim")
        print(f"Um ciclo encontrado: {' '.join(map(str, cycle_det.get_cycle()))}")
    else:
        print("O grafo possui ciclo: Não")
    
    # Análise de complexidade (exigido no enunciado)
    print("\n--- Análise de Complexidade (Ciclo) ---")
    print("Complexidade de Tempo: O(V + E) - Percorre cada vértice e aresta uma vez via DFS.")
    print("Complexidade de Espaço: O(V) - Armazena arrays para marcação e rastro de arestas.")

if __name__ == "__main__":
    main()
