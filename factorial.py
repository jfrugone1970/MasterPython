# Programa para el calculo del factorial
def factorial(n):
    # calculo del factorial
    if n==0 or n==1:
        resultado=1
    elif n>1:
        resultado=n*factorial(n-1)
    return resultado

        
# fin de factorial
print("Programa que realiza el factorial de un numero :\n", end="")
print("Realizado por el Lcdo Jose Frugone Jaramillo\n", end="")
print("el 23/Mayo/2020\n", end="")
print()
numero=int(input('Ingrese un numero n : '))
print()
print("Factorial de un numero es : ", factorial(numero))

        
         
