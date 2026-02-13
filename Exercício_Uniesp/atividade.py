height_men      = []
height_woman    = []

def analise_altura():
    for x in range(0, 4):
        sex = input("digite se você é homem ou mulher: ")

        if(sex.lower() == "homem"):
            try:
                height_m = float(input("Digite sua altura: "))
                height_men.append(height_m)
            except(ValueError):
                print("Você não digitou um número")
                teste = False
                while(teste != True):
                    height_m = input("Digite novamente: ")
                    teste = height_m.isnumeric()
                convert_height = float(height_m)
                height_men.append(convert_height)
        elif(sex.lower() == "mulher"):
            try:
                height_w = float(input("Digite sua altura: "))
                height_woman.append(height_w)
            except(ValueError):
                print("Você não digitou um número")
                teste = False
                while(teste != True):
                    height_w = input("Digite novamente: ")
                    teste = height_w.isnumeric()
                convert_height = float(height_w)
                height_woman.append(convert_height)        
        else:
            print("Digite um sexo válido")

    print(f"número de mulheres: {len(height_woman)}")
    print(f"Número de homens: {len(height_men)}")

    print(f"Maior altura dos homens: {max(height_men):.2f}. Agora, a menor: {min(height_men):.2f}")
    print(f"Maior altura das mulheres: {max(height_woman):.2f}. Agora, a menor: {min(height_woman):.2f}")

    sum_men = sum(height_men)
    sum_woman = sum(height_woman)

    quantity_men = len(height_men)
    quantity_woman = len(height_woman)
    try:
        media = sum_men + sum_woman / quantity_men + quantity_woman
    except(ZeroDivisionError):
        media = sum_men + sum_woman / 1

    print(f"Média de todos: {media:.2f}")


analise_altura()