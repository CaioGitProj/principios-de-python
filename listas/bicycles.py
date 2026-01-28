#parte de listas fo livro

bicycles = ['trek', 'cannondale','redline','specialized']
numbers = list(range(6)) #list() é um método que cria uma lista


squares = [value**2 for value in range(1,11)] #list comprehensions


message = f"My first bicycle was a {bicycles[0].title()}"


print(f"{bicycles}\n")
print(f"{message}\n")


bicycles.append('minha bicicleta')#insere elemento no final da lista

bicycles.insert(1, 'monark') #insere em uma posição específica
bicycles.insert(0, 'python')


del bicycles[-1]#Removendo elementos da lista

exemploPop = bicycles.pop(0)#remove o elemento, mas você ainda pode armazenar em outro lugar
print(exemploPop)

bicycles.remove('monark')#remove o elemento por valor(também da pra reutilizar o valor)

print(f"{bicycles}\n")

bicycles.sort() #bota em ordem alfabética
print(bicycles)

bicycles.reverse()#deixa a lista ao contrário
print(f"\n{bicycles}\n")

tamanhoLista = len(bicycles)
print(f"tamanho de bicycles é: {tamanhoLista}\n\n")

for by in bicycles:
    print(by)

print(numbers)

print(squares)
print(min(squares))#pega valor min
print(max(squares))#pega valor máximo
print(sum(squares))#soma todos os valores
print(squares[0:4])

#--------------TUPLAS---------------------
dimensions = (200,50)