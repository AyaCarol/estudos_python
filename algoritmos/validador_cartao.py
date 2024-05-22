soma_impar = 0
soma_par = 0
total = 0

cartao = input('Insira um número de cartão de crédito: ')
cartao = cartao.replace('-', '')
cartao = cartao.replace(' ', '')
cartao = cartao[::-1]

for x in cartao[::2]:
    soma_impar += int(x)

for x in cartao[1::2]:
    x = int(x) * 2
    if x >= 10:
        soma_par += (1 + (x % 10))
    else:
        soma_par += x

total = soma_impar + soma_par

if total % 10 == 0:
    print('Cartão de crédito válido!')
else:
    print('Número de cartão de crédito inválido!')
