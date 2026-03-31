class CycleDetector:
    """
    Detecta se um grafo possui ciclos e retorna os vértices de um ciclo encontrado.
    """
    def __init__(self, graph):
        self.marked = [False] * graph.V  # Vértices já visitados
        self.edge_to = [None] * graph.V  # Rastro para reconstruir o ciclo
        self.cycle = []                  # Vértices de um ciclo, se houver

        for v in range(graph.V):
            if not self.marked[v]:
                self._dfs(graph, v, v)

    def _dfs(self, graph, v, u):
        """Busca em profundidade recursiva para detecção de ciclo."""
        self.marked[v] = True
        for w in graph.get_adj(v):
            # Se já encontramos um ciclo, para a busca
            if self.cycle:
                return
            
            if not self.marked[w]:
                self.edge_to[w] = v
                self._dfs(graph, w, v)
            # Se w já foi marcado e não é o pai imediato (u), encontramos um ciclo!
            elif w != u:
                self.cycle = []
                x = v
                while x != w:
                    self.cycle.append(x)
                    x = self.edge_to[x]
                self.cycle.append(w)
                self.cycle.append(v)
                # Inverte para que o ciclo seja mostrado na ordem de percurso
                self.cycle.reverse()

    def has_cycle(self):
        """Retorna True se o grafo possuir pelo menos um ciclo."""
        return len(self.cycle) > 0

    def get_cycle(self):
        """Retorna a lista de vértices de um ciclo encontrado."""
        return self.cycle
