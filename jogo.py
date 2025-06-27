from random import randrange

num1 = randrange(0, 100)
num2 = randrange(0, 100)

def adiçao(): #função de adiçao
    resposta = int(input(f'{num1} + {num2}\n=> '))

    while True:
        if num1 + num2 == resposta:
            print('parabens vc acertou')
            break

        else:
            print('tente novamente')
            resposta = int(input(f'{num1} - {num2}\n=> '))

def subtração(): #função de subtração
    resposta = int(input(f'{num1} - {num2}\n=> '))

    while True:
        if num1 - num2 == resposta:
            print('parabens vc acertou')
            break

        else:
            print('tente novamente')
            resposta = int(input(f'{num1} - {num2}=\n=> '))

def mutiplicão(): #funçao de mutiplicação
    resposta = int(input(f'{num1} x {num2}\n=> '))

    while True:
        if num1 * num2 == resposta:
            print('parabens vc acertou')
            break

        else:
            print('tente novamente')
            resposta = int(input(f'{num1} x {num2}=\n=> '))

def divisão(): #funçao de divisão
    resposta = float(input(f'{num1} / {num2}=\n=> '))
    div = num1 / num2
    formatado = int(div * 10) /10 #faz o resutado da divisão ficar com uma casa antes da virgula ex: 10.233434 = 10.2
    
    while True:
        if abs(resposta - formatado) < 0.01: #faz ter uma toleracia de erro de 0.01 assim
            print('parabens vc acertou')
            break

        else:
            print('tente novamente')
            resposta = float(input(f'{num1} / {num2}=\n=> '))

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