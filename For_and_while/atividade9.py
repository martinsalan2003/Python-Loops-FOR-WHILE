'''Escreva um programa que leia uma lista de números do usuário eimprima o maior e o menor número da lista usando um laço while.'''


numeros_str = input("Digite uma lista de números separados por espaço: ")

numeros_lista_str = numeros_str.split()

maior = float("-inf")  
menor = float("inf")   

indice = 0

while indice < len(numeros_lista_str):
    numero = float(numeros_lista_str[indice])
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    indice += 1

print("O maior número é:", maior)
print("O menor número é:", menor)