# 219 - Contains Duplicate

Oi gente! Tô tentando fazer todos os fáceis antes de partir pros médios e esse é um que faltava. Acho que hoje foi um dia sobre retenção de conhecimento.

## O problema :thinking:

Você recebe um vetor de números. Você quer saber se há 2 índices i e j distintos que tenham o mesmo número e que estejam distantes de, no máximo, k posições

Eu não sei se é porque logo antes disso eu lembrei do 2sum, mas pra mim esse claramente poderia ser resolvido da mesma maneira 

## A solução ideal :star_struck:

Vamos usar um map de vistos! Isso é ideal pois, para o nosso problema, precisamos ligar o índice ao valor, não basta só ter o valor como geralmente é com 2 pointers.

No início, ele está vazio. Para um i, se nums[i] já está no vetor, checamos se a diferença entre os índices é menor que k, se sim, retornamos True

Caso não esteja em vistos, o coloque

E é isso! Complexidade de tempo: O(n) pq iteramos em nums. Complexidade de espaço: O(n) pelo dicionário