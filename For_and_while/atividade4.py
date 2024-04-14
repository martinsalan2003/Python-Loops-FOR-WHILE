'''Escreva um programa que leia uma lista de palavras do usuário e imprima a palavra mais longa da lista usando um laço for.'''


palavras = input("Digite uma lista de palavras separadas por espaços: ").split()
palavra_mais_longa = ''

for palavra in palavras:
    if len(palavra) > len(palavra_mais_longa):
        palavra_mais_longa = palavra


print("A palavra mais longa é:", palavra_mais_longa)

