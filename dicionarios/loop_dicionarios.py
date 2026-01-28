favorite_languages = {'sarah': 'Javascript', 'waldemir' : 'C', 'enzo' : 'python', 'waderdison': 'java'}

#apenas as keys:
for names in favorite_languages.keys():
    print(names.title())


print("\n\n\n")


#O loop sozinho também armazena só as chaves
for loop_value in favorite_languages:
    print(loop_value)


print("\n\n\n")


#todos os valores(precisa de duas variáveis). O método items agrupa cada chave com seu valor
for names, languages in favorite_languages.items():
    print(f"{names.title()}: {languages.title()}\n")



print("\n\n\n")


#verificando valores
if 'erin' not in favorite_languages.keys():
    print("Erin não veio de novo")


print("\n\n\n")


#mostrando dicionário ordenado
for names in sorted(favorite_languages.keys()):
    print(f"Hello, {names.title()}!")


print("\n\n\n")


#Excluindo valores repetidos
for language in set(favorite_languages.values()):
    print(language.title())