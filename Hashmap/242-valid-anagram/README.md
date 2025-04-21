# Valid Anagram

Oi gente! Outro super clássico. Esse eu vou tentar dar uma solução diferente da comum, pq a inicial é muito manjada 

## O problema :thinking:

Você recebe 2 strings s e t e quer descobrir se elas são anagramas. A solução que as pessoas geralmente pensam é sort as 2 strings e comparar, o que nos dá uma complexidade de tempo de O(n log n) pelo sort

Será que não tem uma maneira melhor?

## A solução ideal :star_struck:

Existe sim! Com dicionários! Podemos utilizar dicionários para contar a frequência de aparição de cada letra em s. Depois, para t, vamos subtraindo até que haja uma letra que não está em s, tentemos subtrair mais vezes do que a letra apareceu em s, ou t acabe

Mas se as 2 strings não tem o mesmo tamanho, não precisa nem testar isso, já retornamos falso

Eu geralmente faço maps de frequência inicializando com list comprehension, mas só de trocar isso por esse método .get, o tempo de runtime diminuiu muito (mesmo sendo assintoticamente igual)

Praq quem não conhece esse método, ele recebe uma chave e um valor default. Ele te retorna o valor daquela chave se ela estiver no dict. Caso contrário, te retorna o valor default!

Complexidade de tempo: O(n) pq iteramos 2 vezes pelas strings. Complexidade de memória: O(n) pelo dict auxiliar