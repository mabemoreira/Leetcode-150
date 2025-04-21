# 50 - Pow 

Oi gente! Hoje é mais um problema de matemática, eu fiz esse porque já sabia do algoritmo mas ainda não tinha decorado ele

## O problema :thinking:

Você recebe x e n e quer calcular x^n. Note que tanto x quanto n podem ser 0, além de poderem ser negativos.

## A solução ideal :star_struck: 

Esse é o momento de mostrar o binpow, a minha descoberta favorita da ICPC Summer School. É a maneira mais rápida de calcular potência, tendo complexidade de O(log(n))

Imagine n como um número binário. Note que n é a soma de todos os bits setados na representação dele. 

Então, vamos fazer o seguinte: Se x for 0, já retorne 0, não tem o que fazer. Se não for, inicie resposta com 1, o mínimo que ela pode ser.

Enquanto o expoente não for 0, veja se o último bit do expoente está setado (isto é, se n&1 = 1), se sim, 'adicione' esse bit multiplicando resposta por x

Agora, multiplique x por x, pra ir pra próxima potência de x, que veremos na próxima iteração se será adicionada ou não 

De um right shift em x pra analisarmos o próximo bit e pronto!

Só precisa ter cuidado com expoente negativo. Nesse caso, coloque o x como 1/x e troque o expoente para positivo __veja o código__

Complexidade de tempo: O(log(n)) - pq iteramos só na quantidade de bits de n, complexidade de memória, 0(1) - não usamos estruturas de dados adicionais