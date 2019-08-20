print("Este programa revisa si un número es par o impar, y si es negativo o positivo")
print()

a = int(input("Ingrese el número a evaluar:   "))
print()

if a%2==0:
    if a>=0:
        print("El número es par y positivo")
    else:
        print("El número es par y negativo")
else:
    if a>=0:
        print("El número es impar y positivo")
    else:
        print("El número es impar y negativo")
        
