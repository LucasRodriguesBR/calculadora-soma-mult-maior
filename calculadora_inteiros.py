import time

#Ler dois valores inteiros
print('*** CALCULADORA DE NÚMEROS ***')
print('**'*20)

numero1 = float(input('Digite o primeiro valor: '))
numero2 = float(input('Digite o segundo valor: '))

menu = True
sleep = 0
opInvalida = 0

#menu de opções
while menu == True and opInvalida < 3:

    if sleep == 0:
        sleep += 1
    else:
        time.sleep(1)

    print('''SELECIONE A OPÇÃO DESEJADA:
    [1] Somar 
    [2] Multiplicar 
    [3] Maior 
    [4] Novos números 
    [5] Sair do programa ''')
    print('**'*20)
    opcao = int(input('Digite a sua opção:'))

    if opcao == 1:
        resultado = numero1 + numero2
        print('A soma é: {}'.format(resultado))

    if opcao == 2:
        resultado = numero1 * numero2
        print('A multiplicação é: {}'.format(resultado))

    if opcao == 3:
        if numero1 > numero2:
            print('Número {} é o maior.'.format(numero1))

        else:
            print('Número {} é o maior'.format(numero2))
    if opcao == 4:
        numero1 = float(input('Digite o primeiro valor: '))
        numero2 = float(input('Digite o segundo valor: '))

    if opcao == 5:
        print('Saindo...')
        for c in range(0, 3):
            print('.')
            time.sleep(0.6)
        menu = False

    if opcao > 5:
        opInvalida += 1

        if opInvalida < 3:
            print('OPÇÃO INVALIDA. TENTE NOVAMENTE')

#Saida
print('\n')
print('Muito obrigado por usar a calculadora. Tenha um bom dia! ')
print('*'*30)
print('Desenvolvido por Lucas Rodrigues')
print('*'*30)
