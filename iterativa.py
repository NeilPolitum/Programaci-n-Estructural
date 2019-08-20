print("Este programa imprime los 10 primeros múltiplos del número dado")
print()

a = int(input("Ingrese el número:   "))
print()

for i in range(10):
    res = a*(i+1)
    print(str(a)+" * "+str(i)+" = "+str(res))
