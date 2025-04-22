# 12 - Integer to Roman 

Oi gente! Hoje é o primeiro problema médio que eu faço, então de início fiquei um pouco assustada, mas deu tudo certo.

## O problema :thinking:

Você recebe um número inteiro e quer transformá-lo em número romano. A versão inversa desse é bem manjada, mas note que não é só ver se o número que vem depois é maior que ele pra subtrair, tem outra lógica por trás

## A solução ideal :star_struck: 

Note que você precisa de uma tabela, que nem a gente fazia com a versão original, mas aqui, você pode simplesmente tabelar também os valores 'críticos', como 9, 4, etc.

Vamos percorrer o número do dígito mais significativo pro menos, o que quer dizer que nossa tabela tem que ser percorrida ordenada, então não pode ser um dict. Você pode usar simplesmente uma lista de tuplas (ou de listas de 2 itens, como eu fiz).

Agora, para todo valor da tabela, pegamos a divisão inteira do número por ele. Se for > 0, temos que adicionar a letra correspondente, além de 'descartar' essa parte do número com %

