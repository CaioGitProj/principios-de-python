# message = input("Tell me something and i will repeat it back to you: ")
# print(message)

# preco = 0
# encerrar = False
# pergunta = "Digite a sua idade para saber quanto vai pagar" \
#             "de ingresso no cinema"

# while encerrar == False:
#     resposta = float(input(pergunta))
#     if(resposta):
#         if(resposta < 3.0):
#             print("Ingresso é gratuito")
#         elif(resposta >=3 and resposta <= 12):
#             print("Ingresso custa 10 dólares")
#         elif(resposta > 12):
#             print("Ingresso custa 15 dólares")
#     else:
#         print("Você não digitou um número, tente de novo")
#         encerrar = True

# contagem = 10
# while(contagem > -2):
#     if(contagem == -1):
#         print("Fogo!")
#     else:
#         print(contagem)
#     contagem -= 1


#--------------------------------------------------------------------------------------------------------------------------


# numeros = [0,0,0,0,0]
# x = 0

# while(x < 5):
#     numeros[x] = int(input(f"Número {x + 1}: "))
#     x += 1

# while(True):
#     escolhido = int(input("que posição você quer?"))
#     if(escolhido == 0):
#         break
#     print(f"Você escolheu o número: { numeros[escolhido -1]}")