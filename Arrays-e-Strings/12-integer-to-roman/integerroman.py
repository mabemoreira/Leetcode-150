class Solution:
    def intToRoman(self, num: int) -> str:
        listaCorrespondencias = [['I',1],['IV',4],['V',5],['IX',9],
        ['X',10],['XL',40],['L',50],['XC',90],['C',100],['CD',400],['D',500],
        ['CM',900],['M',1000]]

        resp = ""
        for letra, valor in reversed(listaCorrespondencias):
            if num // valor:
                freq = num // valor
                resp += letra * freq 
                num %= valor
        
        return resp