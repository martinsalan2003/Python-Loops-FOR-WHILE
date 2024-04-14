'''Escreva um programa que leia uma string do usuário e imprima o número de vogais (a, e, i, o, u) que aparecem na string usando um laço for.
'''

string = input("Digite uma string: ")

num_vogais = 0

for caractere in string:
    if caractere.lower() in 'aeiou':
        num_vogais += 1

print("Número de vogais na string:", num_vogais)