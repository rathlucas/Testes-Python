import random
n1 = input('Escolha um nome: ')
n2 = input('Escolha um nome: ')
n3 = input('Escolha um nome: ')
n4 = input('Escolha um nome: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O sorteado foi {}! '.format(escolhido))