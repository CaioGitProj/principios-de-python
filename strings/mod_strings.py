s = "tigre"

centralizado = "X" + s.center(10, ".") + "X"
print(centralizado)

print("\n")

ajus = s.ljust(20, ".")
ajusr = s.rjust(20, ".")
print(ajus)
print(ajusr)

print("\n")
# Utilizando f strings
print("--------------F strings: ----------------\n")

print(f"{s:^20}")
print(f"{s:.<20}")
print(f"{s:.>20}")

string = "um tigre, dois tigres, três tigres"
linhas = "uma linha\nduas linhas\ntrês linhas"
trocar = "um doido, dois doidos e um doido"

verificaTudoNum = "123456"
verificaAlpha = "oi"
verificaDigito = "537124958712"

emaiusculo = "AAAAAA"
eminusculo = "abcdeeeee"

estaEmBranco = "      "

print(string.split(","))
print(linhas.splitlines())
print(trocar.replace("doido", "gato", 2))

print(verificaTudoNum.isalnum())
print(verificaAlpha.isalpha())
print(verificaDigito.isdigit())

print("\n")

print(emaiusculo.isupper())
print(eminusculo.islower())

print("\n")

print(estaEmBranco.isspace())

print("{0:<10} {1}".format("123456", "podcre"))
print("{0:+7}".format(32))