numero_1 = int(input('Digite um valor: '))
numero_2 = int(input('Digite outro valor: '))

if numero_1 > numero_2:
    print(f'O primeiro valor {numero_1=} é maior que o segundo valor {numero_2=}')
elif numero_2 > numero_1:
    print(f'O segundo valor {numero_2=} é maior que o primeiro valor {numero_1=}')
else:
    print(f'O primeiro valor {numero_1=} e o segundo valor {numero_2=} são iguais')