# Encontra e retorna o maior número impar presente na lista
def maior_impar(lista):
    maior_numero = lista[0]
    for item in lista:
        if item % 2 != 0:
            if item > maior_numero:
                maior_numero = item
    return maior_numero
    
# Encontra e retorna o menor número impar presente na lista
def menor_impar(lista):
    menor_numero = lista[0]
    for item in lista:
        if item % 2 != 0:
            if item < menor_numero:
              menor_numero = item
    return menor_numero
    
# Encontra e retorna o maior e o menor número ímpar presentes na lista
def menor_maior_impar(lista):
    maior = maior_impar(lista)
    menor = menor_impar(lista)
    return (maior, menor)

print(maior_impar([1,3,-9,21,25,48]))
print(menor_impar([1,3,5,21,25,48]))
print(menor_maior_impar([1,3,5,21,25,48]))
