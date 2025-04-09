# 104 - Maximum Depth of a Binary Tree

Nessa de passar por pelo menos um problema de cada estrutura de dados, cheguei hoje nas árvores binárias. Esse problema é uma história sobre não julgar livros pela capa e porque lembrar métodos de grafo é importante

## O problema :thinking:

Você recebe uma árvore binária e tem que responder qual a altura máxima dela, isto é, qual a altura da última folha.

Existe a maneira óbvia de se fazer isso: recursão. Árvore binária a gente geralmente pega caso base quando está em uma das folhas e caso contrário vê pros 2 lados. 

Mas tem um problema: essa approach é recursiva. Nós somos treinados a acreditar que soluções recursivas são inerentemente piores, independente de complexidade. Então eu nem pensei na complexidade dela __red flag__

Pensando em soluções iterativas, lembrei que toda árvore é um grafo, e existe uma busca que percorre os grafos por níveis! A BFS! Como eu não lembrava como implementar a BFS, eu peguei [desse vídeo do Neetcode](https://www.youtube.com/watch?v=hTM3phVI6YQ&t=494s&ab_channel=NeetCode). Eu estava tão convencida que a minha solução era a melhor possível que nem vi o resto do vídeo e só peguei o código __red flag__

Eu achei um pouco estranho um problema labeled como fácil de árvores binárias pedir que você soubesse BFS? Sim, mas é como dizem, o mercado está cada vez mais competitivo.

Pra você que não lembra como implementar a BFS, __veja o código 1__ e eu vou escrever a lógica aqui pra lembrar:

Primeiro, inicie uma fila com a raiz. Enquanto essa fila existir, você quer empilhar, para todos os nós da fila, os filhos dele. Não esqueça de tirar o nó atual da fila. 

Note que range(len(fila)) é calculado apenas 1 vez! Na primeira vez que passa por ele, e não é alterado até que saia do for. Isto é, toda vez que sair do for, temos um novo nível.

Se você colocar no leetcode, vai ver que a complexidade de tempo é ideal (O(n) porque vemos n nós) e de memória também(O(n) por conta da fila).

## A solução ideal :star_struck:

Eu já estava quase indo fazer outra coisa, mas nos sugeridos apareceu [esse vídeo](https://www.youtube.com/watch?v=Y0m0v3P1UOw&t=182s&ab_channel=DeeptiTalesra). Pra quem não conhece a Deepti, ela é extremamente talentosa em leetcode, além de ter uma super didática.

Fui assistir o vídeo e me deparo com a solução: exatamente a recursiva que é intuitiva __veja código 2__

Nesse momento eu parei para analisar a complexidade: O(n) no tempo, já que passa por cada nó uma vez e O(n) na memória, por conta da pilha de recursão. Era não só uma solução tão boa como a minha, mas também bem mais fácil de codar

Moral da história: não julguem um algoritmo só por ser recursivo