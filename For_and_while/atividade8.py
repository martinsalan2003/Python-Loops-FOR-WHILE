'''Escreva um programa que leia um número inteiro positivo n do usuário eimprima se n é primo ou não usando um laço while'''

num = int(input("Digite um número inteiro positivo: "))

divisor = 2

e_primo = True

if num <= 1:
    e_primo = False
else:
    while divisor < num and e_primo:  
        if num % divisor == 0:
            e_primo = False
        divisor += 1

if e_primo:
    print(num, "é um número primo.")
else:
    print(num, "não é um número primo.")