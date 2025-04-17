# 66 - Plus One

Oi gente, hoje tem um fácil, bem parecido com um daqui ou do codility sobre soma de binários. Se vc já conhece ele vai achar fácil ele 

# O problema :thinking: 

Você recebe um inteiro em formato de lista e quer saber quanto é esse número +1, nem precisa dar join. Fácil, né? Acho que meu grande erro nesse foi tentar refazer agora depois de uns 5 dias tentando melhorar algo que já passava com a melhor complexidade de tempo possível kkkk

# A solução ideal :star_struck:

Nesse aqui eu já acertei de primeira, e acho que todo mundo que fez circuitos lógicos também. A grande sacada é inverter o vetor ao invés de simplesmente iterar ao contrário, pq caso seja necessário adicionar o 1 no final, append é O(1), mas adicionar no começo seria O(n)

Então a gente começa com um carry de 1 que queremos colocar. Se na iteração a gente encontrar um número != 9 já fazemos a soma, setamos o carry pra 0 e saímos do loop. 

se encontrarmos um 9, setamos o carry pra 1 (na real nem precisava né, se chegamos aqui é pq o carry ainda é 1) e colocamos a posição em 0, sem sair do loop

note que o carry só sai do loop igual a 1 se o 9 for o último número (ou seja, o dígito mais significativo). Então aí, como já tinhamos setado como 0, só dar append no 1 do final

Não esqueça de desinverter no final pra retornar!

Complexidade de tempo: O(n). Complexidade de memória O(1) se o Python inverter in place 