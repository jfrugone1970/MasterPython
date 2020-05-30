# Programa en Python que realiza 3 funciones matematicas
# realizado por el Lcdo. Jose Fernando Frugone Jaramillo
# hecha el 23/Mayo/2020
# *** Primera funcion Funcion x
def func_x(a,b,x):
    # Calcula la funcion de la x
    fx = ((a*x)+b)

    return fx
# Termino de la funcion x
# ** Segunda funcion de la y
def func_y(a,b,x):
    # Calcula la funcion de la y
    fy = ((a*x) + b)

    return fy
# Termino de la funcion y
def func_g(a,b,x):
    #Calcula la funcion de la g
    fg = ((a*x)+b)/(b**x)

    return fg
# termino de la funcion g

print()
print("Programa que calcula el valor de 3 funciones matematicas\n", end="")
print("Realizado por el Lcdo Jose Fernando Frugone Jaramillo\n", end="")
print("Realizado el 23/Mayo/2020\n", end="")
print()
print("Ingrese el valor de las variables :\n", end="")
vara=float(input('Ingrese valor de a : '))
varb=float(input('Ingrese valor de b : '))
varx=float(input('Ingrese valor de x : '))
print()
print("Funcion de la x es : ", func_x(vara,varb,varx), end=" ")
print()
print("Funcion de la y es : ", func_y(vara,varb,varx), end=" ")
print()
print("Funcion de la g es : ", func_g(vara,varb,varx), end=" ")

    
