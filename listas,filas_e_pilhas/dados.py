L = list(range(101)) #uma lista de números de 0 até 100



#--------------Uma FILA em python------------------------
ultimo = 10
condicao = True
fila = list(range(1,11))
texto = """Digite F para adicionar um cliente ao fim da fila, ou
A para realizar o atendimento. S para sair."""

while(condicao):
    print(f"\nexistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print(texto)

    operacao = input("Operação(F,A ou S): ").upper()

    if(operacao == "A"):
        if(len(fila) > 0):
            atendido = fila.pop(0)
            print(f"cliente {atendido} atendido")
        else:
            print("Fila vazia! Ninguém para atender")
    elif(operacao == "F"):
        ultimo += 1
        fila.append(ultimo)
    elif(operacao == "S"):
        condicao = False
    else:
        print("Operação inválida")
#----------------------------------------------------------



#------------Uma PILHA em python---------------------------
prato = 5
escolha = True
pilha = list(range(1,6))
frase = """Digite E para empilhar um novo prato, ou
D para desempilhar. S para sair"""

while(escolha):
    print(f"\nExitem {len(pilha)} pratos na pilha")
    print(f"pilha atual {pilha}")
    print(frase)

    user = input("Operção (E,D ou S): ").upper()

    if(user == "D"):
        if(len(pilha) > 0):
            lavado = pilha.pop(-1)
            print(f"Prato {lavado} lavado")
        else:
            print("Pilha vazia!")
    elif(user == "E"):
        prato += 1
        pilha.append(prato)
    elif(user == "S"):
        escolha = False
    else:
        print("Operação inválida!")
#--------------------------------------------------------