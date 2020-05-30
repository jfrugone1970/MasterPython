# Programa para calcular la serie fibonacci
# Realizado por el Lcdo Jose Frugone
def fib(n):
    # print fibonacci
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
# Llama a la serie fibonacci
fib(3000)
