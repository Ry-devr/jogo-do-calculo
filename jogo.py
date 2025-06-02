import random

num1 = random.randrange(0, 100)
num2 = random.randrange(0, 100)

def adiçao():
    resposta = int(input('{} + {}\n=> '.format(num1, num2)))

    while True:
        if num1 + num2 == resposta:
            print('parabens vc acertou')
            break

        else:
            print('tente novamente')
            resposta = int(input('{} - {}\n=> '.format(num1, num2)))

def subtração():
    resposta = int(input('{} - {}\n=> '.format(num1, num2)))

    while True:
        if num1 - num2 == resposta:
            print('parabens vc acertou')
            break

        else:
            print('tente novamente')
            resposta = int(input('{} - {}=\n=> '.format(num1, num2)))

def mutiplicão():
    resposta = int(input('{} x {}\n=> '.format(num1, num2)))

    while True:
        if num1 * num2 == resposta:
            print('parabens vc acertou')
            break

        else:
            print('tente novamente')
            resposta = int(input('{} x {}=\n=> '.format(num1, num2)))

def divisão():
    resposta = int(input('{} / {}=\n=> '.format(num1, num2)))

    while True:
        if num1 / num2 == resposta:
            print('parabens vc acertou')
            break

        else:
            print('tente novamente')
            resposta = int(input('{} / {}=\n=> '.format(num1, num2)))

print('-='*20)
print('bem vindo ao jodo')
print('-='*20)

while True:
    n = input('vc que mutiplicar[*], somar[+], subtrair[-], dividir[/]\n=> ')
    
    if n not in ['/','+','-','*']:
        n = input('vc que mutiplicar[*], somar[+], subtrair[-], dividir[/]\n=>')
    
    if n == '+':
        adiçao()
        break
    elif n =='-':
        subtração()
        break
    elif n == '*':
        mutiplicão()
        break
    else:
        divisão()
        break