'''Escreva um programa que leia uma lista de números do usuário e imprima a soma de todos os números da lista usando um laço for.'''

numeros = input("Digite os números, separados por espaço: ").split()

soma = 0
for numero in numeros:
    soma += float(numero)

print("A soma dos números é:", soma)