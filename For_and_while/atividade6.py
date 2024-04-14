'''Escreva um programa que leia um número inteiro positivo n do usuário eimprima a tabuada de n (de 1 a 10) usando um laço for'''

numeros = int(input("Digite um Número"))

for numero in range(1, 10):
    print(f"{numeros} X {numero} = {numeros*numero}")