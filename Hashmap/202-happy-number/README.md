# 202 - Happy Number 

Oi gente! Hoje o problema é sobre não se prender às categorias do leetcode! 

## O problema :thinking:

Você recebe um número e quer descobrir se ele é feliz. Ele é feliz se, repetindo sempre o algoritmo de somar os quadrados dos dígitos, você chega em um alguma hora. Se nunca chegar, é triste

Apesar de ser fácil, eu fiquei com bastante dúvidas iniciais sobre esse problema: como saber se entrou em loop infinito sem entrar em loop infinito? E principalmente,o que isso tem a ver com dicionários?

Ao invés de escrever o caso que não dá certo no papel __grande erro__ eu simplesmente fui ver a resolução do neetcode __veja código 1__

Note que, se eu tivesse testado o número 2, eu veria que ele entra em loop infinito não pq encontra sempre números novos, mas pq REPETE NÚMEROS QUE JÁ VIU! 

Sendo assim, basta usar um set pra ver se já vimos o número atual.

Apesar dessa solução ser O(n) em memória e melhor 99.82% nesse quesito, ela não é tão boa em tempo. E eu valorizo mais tempo, já que memória a gente compra, mas não tem dinheiro que compre tempo. 

## A solução ideal :star_struck:

Que nem eu falei, isso só dá errado se tem ciclo. Peraí, é um grafo de 1 caminho só, mas que dá errado se tem ciclo? Isso é resolvível com aquele algoritmo da lebre e da tartaruga!  __veja código 2__


Para saber mais sobre, pesquise sobre fast and slow pointers (ou veja a resolução do problema 141 aqui). Apesar de ser exatamente o mesmo problema que o 141 olhando assim, queria comentar que não precisa ser usado só em ciclos

Se você quiser por exemplo, encontrar o meio de uma lista, você pode usar também (afinal, se a lebre é 2x mais rápida que a tartaruga, se a lebre chega no final a tartaruga chegou no meio)

Até agora nas minhas pesquisas só encontrei evidências da velocidade da lebre sendo 2x a da tartaruga, mas se eu ver algum outro algoritmo legal coloco aqui