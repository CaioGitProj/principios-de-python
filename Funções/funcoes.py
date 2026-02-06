num = 2

def mudando_global():
    global num
    num = 5

    print(num)



def maiorValor(a,b):
    if(a > b):
        return (f"{a} maior que {b}")
    
    elif(a == b):
        return ("Números entregues são iguais")
    
    return (f"{b} maior que {a}")


def fatorial_recursivo(n):
    if(n == 0 or n == 1):
        print(f"aqui terminou a recursão {n}")
        return 1
    
    fat = n * (fatorial_recursivo(n-1))
    print(f"Realizando conta fatorial: {n}, fat-> {fat}")

    return fat


def fibonacci(n): # Trabalho desnecessário
    print(f"calculando fibonacci {n}")

    if(n <= 1):
        return 1
    
    fibo = fibonacci(n-1) + fibonacci(n-2)
    print(f"fibonacci de {n} = fibonacci de {n -1} + fibonacci de {n - 2}")

    return fibo

print(maiorValor(1, 1))

print(num)
mudando_global()

fatorial_recursivo(4)
fibonacci(4)