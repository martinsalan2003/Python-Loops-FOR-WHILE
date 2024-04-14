'''
Escreva um programa que leia uma string do usuário e imprima a string ao contrário usando um laço while'''

text_user = input("Digite um texto")

txt_user_inver = ""

indice = len(text_user) - 1


while indice >= 0:
    txt_user_inver += text_user[indice]
   
    indice -= 1

print(" texto invertido:", txt_user_inver)


    