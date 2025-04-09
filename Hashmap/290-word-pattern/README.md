# 290 - Word Pattern

Oi gente! desculpa não estar postando todos os que eu tô fazendo, a vida tá bem corrida.

De qualquer jeito, o problema de hoje só serviu pra reforçar a importância de ler o enunciado com cuidado e sem pressa, além de pensar nos corner cases.

## O problema :thinking:

Você recebe uma string de uma palavra (pattern) e uma string de n palavras (s). Você quer saber se há uma BIJEÇÃO entre pattern e s, isto é, se exatamente 1 de s mapeia em pattern e vice-versa.

De início parece fácil, fazer um map e quando passar por outra palavra, ver se ela mapeia pra uma letra já existente. Contudo, apesar de isso passar nos casos de teste, você não pode fazer só isso (dá WA). Isso porque somente testamos se há uma injeção entre ambas, não uma bijeção

Por mais que gaste mais memória, uma bijeção tem que ser testada com 2 maps (ou 2 sets, ou 2 listas, enfim).

## A solução ideal :star_struck:

__veja o código 1__ isso aí galera! O primeiro accepted já deu ideal em tempo! O(n), pq vc tá olhando 1 vez pra cada posição

Não deu ideal em memória em runtime pq os nomes das variáveis são mt grandes, além de eu ter colocado esse if a mais pra gastar menos tempo. Se você for ver o sample do leetcode ele também usa 2 maps (O(n)).

Voltando pro algoritmo: você só precisa testar se a palavra e a letra atuais já estão nos maps. Se sim, caso elas não correspondam uma a outra, já retorna falso.

Se você chegou até o final da palavra e não achou falso, é pq tudo mapeia certo, pode retornar verdadeiro