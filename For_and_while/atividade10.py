'''Escreva um programa que leia duas listas de números do usuário e imprima a lista resultante da concatenação das duas listas usando um laço for.'''

numeros_str_1 = input("Digite os números da primeira lista separados por espaço: ")

numeros_lista_str_1 = numeros_str_1.split()

numeros_str_2 = input("Digite os números da segunda lista separados por espaço: ")

numeros_lista_str_2 = numeros_str_2.split()

lista_concatenada = []

for numero_str in numeros_lista_str_1:
    lista_concatenada.append(int(numero_str))
for numero_str in numeros_lista_str_2:
    lista_concatenada.append(int(numero_str))

print("Lista resultante da concatenação:", lista_concatenada)