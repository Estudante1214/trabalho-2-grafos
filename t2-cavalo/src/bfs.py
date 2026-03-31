from collections import deque

class BreadthFirstSearch:
    """
    Calcula a distância mínima entre dois vértices usando Busca em Largura (BFS).
    """
    def __init__(self, graph, start_v):
        self.marked = [False] * graph.V  # Vértices já visitados
        self.dist_to = [-1] * graph.V    # Distância mínima a partir do vértice inicial
        self._bfs(graph, start_v)

    def _bfs(self, graph, s):
        """Busca em largura iterativa."""
        queue = deque([s])
        self.marked[s] = True
        self.dist_to[s] = 0

        while queue:
            v = queue.popleft()
            for w in graph.get_adj(v):
                if not self.marked[w]:
                    self.marked[w] = True
                    self.dist_to[w] = self.dist_to[v] + 1
                    queue.append(w)

    def get_distance(self, v):
        """Retorna a distância mínima até o vértice v."""
        return self.dist_to[v]
