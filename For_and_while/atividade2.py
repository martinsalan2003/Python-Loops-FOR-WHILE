'''Escreva um programa que leia um número inteiro positivo n do usuário eimprima os n primeiros números naturais (de 1 a n) usando um laço for.'''

num_user = int(input("Digite o número limite para a contagem"))

for contador in range(0, num_user):
    print(contador)
