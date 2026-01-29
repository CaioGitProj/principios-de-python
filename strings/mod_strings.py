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