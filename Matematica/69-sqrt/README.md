# 69 - Sqrt

Oi gente, problema 69! Bem básico, é como implementar uma raiz quadrada

## O problema :thinking: 

Você quer calcular a raiz quadrada de um número. Literalmente só isso. Se a raiz não for inteira, retorne o inteiro com o quadrado mais próximo. 

De primeira, eu pensei em ir testando os números até encontrar qual é o que chega mais perto __veja código 1__ mas isso é O(n)


## A solução ideal :star_struck: 

Note que o conjunto dos números inteiros é enumerável. Então, pela diagonalização de Cantor, eles tem alguma ordem. E é a ordem numérica mesmo que chegamos neles. 

Sendo assim, temos um conjunto de números ordenados e queremos encontrar o valor mais próximo de um x. Isso é busca binária!

Note que, caso não achemos o número, só saímos do loop quando max < min, então max que guarda o valor do menor inteiro cujo quadrado não passa de x 