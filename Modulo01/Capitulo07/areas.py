# Define o valor de PI
PI = 3.141592

# Calcula a área do quadrado
def quadrado(l):
    return l * l

# Calcula a área do triângulo
def triangulo(base,altura):
    return (base * altura) / 2

# Calcula a área de um círculo
def circulo(r):
    return PI * (r**2)

# Calcula a área de uma elipse
def elipse(a,b):
    return PI * a * b

# Calcula a área de um trapézio
def trapezio(B,b,h):
    return ((B+b)*h) / 2