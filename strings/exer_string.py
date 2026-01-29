#Ex 1
palavra1 = "AABBEFAATT"
palavra2 = "BE"

if(palavra2 in palavra1):
    print(f"{palavra2} econtrado na posição {palavra1.find(palavra2)} de {palavra1}")

#Ex 2

valor1 = set(input("Escreva uma frase:"))
valor2 = set(input("Agora, outra:"))
comum = valor1 & valor2

print(f"letras em comum nas duas frases: {"".join(comum)}")

#Ex 3

valor3 = set(input("Escreva uma frase:"))
valor4 = set(input("Agora, outra:"))
diferenca = valor3 ^ valor4

print(f"letras que só existem em cada uma: {"".join(diferenca)}")