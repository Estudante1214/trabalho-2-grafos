1. Visão Geral e Modelagem
Bom, a ideia desse projeto foi modelar os movimentos de um cavalo em um tabuleiro 3x3 usando grafos.

Então, o que eu fiz foi transformar cada casa do tabuleiro em um vértice, numerando de 0 até 8, seguindo a ordem normal de leitura.

As conexões entre esses vértices representam os movimentos válidos do cavalo.

Um ponto interessante é que, nesse tabuleiro 3x3, a posição central, que é o vértice 4, acaba ficando isolada. Isso acontece porque o cavalo simplesmente não consegue chegar lá nem sair de lá com movimentos válidos.

E o arquivo de entrada segue o padrão algs4, que já facilita bastante na hora de ler e organizar os dados.

2. Estrutura de Dados e Organização

Sobre a implementação, eu separei o código em partes pra ficar mais organizado e fácil de entender.

A classe principal é a Graph, que usa lista de adjacência. Basicamente, cada vértice guarda uma lista com seus vizinhos.

Escolhi isso porque é mais eficiente, já que o grafo não tem tantas conexões — então não faz sentido usar matriz.

E o main.py funciona como o “orquestrador”: ele lê o arquivo, monta o grafo e chama os algoritmos.

3. Análise de Conectividade e Distância 

Pra analisar a conectividade, usei DFS na classe de componentes conexas.

O algoritmo percorre o grafo e identifica grupos conectados. No final, dá pra ver que existem dois grupos: um com os 8 vértices das bordas e outro só com o vértice central isolado.

Já pra calcular o menor caminho, usei BFS.

A diferença é que a BFS vai por níveis, então ela garante que o primeiro caminho encontrado já é o menor possível.

Nesse caso, ela mostra que o cavalo precisa de 4 movimentos pra sair de um canto e chegar no canto oposto do tabuleiro.

4. Detecção de Ciclos e Complexidade 
Na parte de ciclos, também usei DFS, mas com um detalhe a mais: o algoritmo guarda de onde veio cada vértice.

Assim, se ele encontra um vértice já visitado que não é o “pai”, significa que existe um ciclo.

E pra finalizar, em termos de desempenho, todos os algoritmos rodam em tempo O de V mais E e usam espaço O de V, o que é bem eficiente pra esse tipo de problema.
