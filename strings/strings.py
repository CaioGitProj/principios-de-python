nome = "João da Silva"

print(nome.startswith("João"))
print(nome.startswith("joão"))

print(nome.endswith("Silva"))

print("da" in nome)

print("\n\n")

frase = "um tigre, dois tigres, três tigres"
print(frase.count("tigre"))
print(frase.count("t"))
print(frase.count("do"))

print("\n")

print(frase.find("dois"))
print(frase.rfind("tigres"))
print(frase.find("tigres"))

print("\n")
print(frase.find("tigres", 0, 10)) # começa em 0 e termina em 10

print("\n")
print(frase.index("tigre")) # mesma coisa do find. No entanto, se não encontrar lança uma exceção