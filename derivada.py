# Programa que calcula el calculo de las derivadas
# realizado por el Lcdo. Jose Fernando Frugone Jaramillo
# realizado el 26/05/2020
# - Derivada de una potencia
import math
# para para primera derivada
def devpot(u,k):
    # Calculo de la derivada de una
    # potencia
    fx = (((k * (u**(k-1)) * (u**1))))

    return fx
#fin de derivada de una potencia
#para derivada de una raiz cuadrada
def devraiz(u):
    # Calculo de la derivada de la raiz
    fr = ((u**1) / (2 * math.sqrt(u)))

    return fr
#fin de derivada de una raiz cuadrada
#Derivada de un producto
def devpro(k,v):
    # para la derivada
    fx1 = ((-k * (v**1)) / (v**2))
    return fx1
# fin de derivada
print()
print("Programa que calcula las derivadas \n", end="")
print("Realizado por el Lcdo. José Frugone \n", end="")
print("Realizado el 26/05/2020\n", end="")
print()
print("1.- Derivada por potencia \n", end="")
print("2.- Derivada por raiz cuadrada\n", end="")
print("3.- Derivada por producto\n", end="")
print("4.- Salir \n", end="")
print()
op = int(input('Digite una opcion (1/4) : '))
if op==1:
    valor_k = float(input('Ingrese el valor de k : '))
    valor_u = float(input('Ingrese el valor de u : '))
    print("La derivada de una potencia es :", devpot(valor_k,valor_u))
elif op==2:
    valor_u = float(input('Ingrese el valor de u : '))
    print("La derivada de una raiz es :", devraiz(valor_u))
elif op==3:
    valor_k = float(input('Ingrese valor de k '))
    valor_v = float(input('Ingrese valor de v '))
    print("La derivada de un producto es :", devpro(valor_k,valor_v))
elif op==4:
    print("Salir .....")
else:
    print("Opcion Incorrecta....!\n", end="")
    print()
    
