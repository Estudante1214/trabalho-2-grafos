class Graph:
    """
    Representação de um grafo não direcionado usando lista de adjacência.
    """
    def __init__(self, V):
        self.V = V  # Número de vértices
        self.E = 0  # Número de arestas
        self.adj = [[] for _ in range(V)]  # Lista de adjacência

    def add_edge(self, v, w):
        """Adiciona uma aresta entre os vértices v e w."""
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1

    def get_adj(self, v):
        """Retorna os vizinhos do vértice v."""
        return self.adj[v]

    def __str__(self):
        """Formata a lista de adjacência para exibição."""
        res = ""
        for v in range(self.V):
            res += f"{v}: {' '.join(map(str, sorted(self.adj[v])))}\n"
        return res
