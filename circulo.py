# Programa de Python con una funcion
# que calcula el perimitero del circulo
# Elaborado por el Lcdo Jose Fernando Frugone Jaramillo
pi = 3.1415926535897932

def circulo(radio):
   
    per = ((2 * pi) * radio)

    return per

# Para mostrar el permitro del circulo
print('El perimetro del circulo 1 es ',circulo(12))
# Para el perimetro del circulo 2
print('El perimetro del circulo 2 es ',circulo(24))
# Para el perimetro del circulo 3
print('El perimetro del circulo 3 es ',circulo(48))

