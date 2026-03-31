# Trabalho Prático 2 - Teoria dos Grafos

Este projeto implementa o grafo do cavalo em um tabuleiro de xadrez 3x3 para a cadeira de Teoria dos Grafos. O objetivo é aplicar conceitos de modelagem, componentes conexas, distância mínima e detecção de ciclos.

## Estrutura do Projeto

- `dados/entrada.txt`: Contém a lista de arestas do grafo do cavalo no formato `algs4`.
- `src/main.py`: Ponto de entrada que executa todas as análises solicitadas.
- `src/graph.py`: Classe `Graph` para representação por lista de adjacência.
- `src/cc.py`: Classe `ConnectedComponents` para identificar componentes conexas via DFS.
- `src/cycle.py`: Classe `CycleDetector` para detecção de ciclos e retorno de um ciclo encontrado.
- `src/bfs.py`: Classe `BreadthFirstSearch` para cálculo de distância mínima entre vértices.

## Modelagem do Tabuleiro 3x3

Os vértices são numerados de 0 a 8 na ordem de leitura (esquerda para direita, cima para baixo):

```text
(0,0) -> 0 | (0,1) -> 1 | (0,2) -> 2
(1,0) -> 3 | (1,1) -> 4 | (1,2) -> 5
(2,0) -> 6 | (2,1) -> 7 | (2,2) -> 8
```

## Como Executar

Para rodar o programa, certifique-se de estar no diretório raiz do projeto (`t2-cavalo`) e execute:

```bash
python3 src/main.py
```

## Respostas Esperadas

O programa gera automaticamente as respostas para as seguintes perguntas:
1. Lista de adjacência do grafo.
2. Componentes conexas e seus vértices.
3. Distância mínima entre (0,0) e (2,2).
4. Existência de ciclos e um exemplo de ciclo encontrado.
5. Análise de complexidade do algoritmo de ciclo.
