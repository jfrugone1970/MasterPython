# Programa que calcula el movimiento circular uniforme
# Realizado por el Lcdo Jose Fernando Frugone Jaramillo
# realizado el 20/Mayo/2020
va=0
pi=3.141592653589793
# Para el calculo de la velocidad angular
def veloang(f):
    #calculo de la frecuencia
    vang=((2*pi)*f)

    return vang
# Retorna la frecuencia
# Calcula la velocidad
def velo1(frecu,radio):
    #calcula la velocidad
    v=frecu*radio

    return v
# Regresa
# Calcula el tiempo
def tiempo(frecuencia):
    # calcula el tiempo
    t = 1 / frecuencia

    return t
# fin procesole
# calculo de la aceleracion
def acelera(velo,rad):
    #Calculo de la aceleracion Centripeda
    acp=((velo**2)/rad)

    return acp
# fin proceso
print("Programa que calcula el Movimiento circular uniforme\n", end=" ")
print("Realizado por el Lcdo Jose Fernando Frugone Jaramillo\n", end=" ")
print("realizado el 20/Mayo/2020\n", end=" ")
print()
print("Ingrese Frecuencia :\n", end=" ")
frec=float(input('Ingrese frecuencia : '))
velocidad=veloang(frec)
print()
print("Ingrese Radio : ")
radio1=float(input('Ingrese radio : '))
# Para calcular la velocidad angular
print("Velocidad angular es :\n",velocidad, end=" ")
print()
print("Tiempo es :\n", tiempo(frec), end=" ")
print()
print("Velocidad es :\n",velo1(velocidad,radio1), end=" ")
print()
print("La aceleracion centripeda es :\n", acelera(velocidad,radio1), end=" ")


