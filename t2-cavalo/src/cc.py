class ConnectedComponents:
    """
    Identifica as componentes conexas de um grafo usando Busca em Profundidade (DFS).
    """
    def __init__(self, graph):
        self.marked = [False] * graph.V  # Vértices já visitados
        self.id = [0] * graph.V          # Identificador da componente para cada vértice
        self.count = 0                   # Número total de componentes conexas

        for v in range(graph.V):
            if not self.marked[v]:
                self._dfs(graph, v)
                self.count += 1

    def _dfs(self, graph, v):
        """Busca em profundidade recursiva."""
        self.marked[v] = True
        self.id[v] = self.count
        for w in graph.get_adj(v):
            if not self.marked[w]:
                self._dfs(graph, w)

    def get_count(self):
        """Retorna o número de componentes conexas."""
        return self.count

    def get_components(self):
        """Retorna os vértices agrupados por componente."""
        components = [[] for _ in range(self.count)]
        for v in range(len(self.id)):
            components[self.id[v]].append(v)
        return components
