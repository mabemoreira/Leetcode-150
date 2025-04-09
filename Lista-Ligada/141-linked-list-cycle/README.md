# 141 Linked List Cycle

Oi gente! Esse é o primeiro problema que eu tô colocando as explicações das resoluções diretamente online, então pf tenham paciência, com o tempo vou passando as outras explicações pra cá :pray:

Pensei em dar uma mudada de estrutura de dados então decidi fazer de linked list, até pq é a partir de linked-list que eu passo pro c++, então queria ver como era em Python

Não é que nem pilha e fila que tem uma biblioteca amplamente usada, é com uma classe (veja em ambos os códigos)

## O problema :thinking:

Você recebe uma lista ligada e quer descobrir se ela tem um ciclo, isto é, se algum nó é alcançado por mais de um caminho 

De início, pensei em utilizar um map de vistos que nem fizemos no Two Sum. Se o próximo já estivesse visto, ele retornaria false. A chave seria o valor e a pos seria o valor. 

O grande problema dessa approach é que se os valores repetirem, esse map não é mais confiável. Mesmo se você usasse pos de chave, ainda não daria certo

Aí eu me toquei que o parâmetro _pos_ é absolutamente irrelevante, então podemos simplesmente usar um set pra guardar os nós e usar a mesma lógica __veja o código 1__.

Se n é o número de nós, a complexidade de tempo é O(n) (passa por algum múltiplo do número de nós uma vez até encontrar o ciclo e acesso a set é O(1)) e de memória, pelo set, também é O(n)

## A solução ideal :star_struck:

Eu mandei o código 1 no Leetcode e vi que a colocação dele estava bem mais ou menos. Fui ver as outras soluções e vi que todo mundo tinha a mesma solução, usando 2 pointers!

Ela funciona assim: um ponteiro é o lento, ele vai andar um nó de cada vez. O outro é o rápido, ele anda 2 de cada vez. 

Isso porque, se o ciclo tem L nós, temos 0 a L-1 nós de posições. A cada iteração, a velocidade relativa entre eles é 1. Uma hora, o mais rápido acaba indo de L-1 pra 0 e dando a volta, e eles se encontram. Pra saber mais, só pesquisar _Floyd's Cycle-Finding Algorithm_. 

A grande diferença desse __veja código 2__ algoritmo é que, apesar de ainda ser O(n) em tempo, ele é O(1) em memória. [Esse vídeo](https://www.youtube.com/watch?v=S5TcPmTl6ww&ab_channel=Geekific) explica muito bem o problema e porque a distância entre eles vai diminuindo!