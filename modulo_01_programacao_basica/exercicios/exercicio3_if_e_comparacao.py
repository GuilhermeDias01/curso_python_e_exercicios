primeiro_valor = int(input('Digite um valor: '))
segundo_valor = int(input('Digite outro valor: '))

if primeiro_valor > segundo_valor:
    print(f'O primeiro valor {primeiro_valor} é maior que o segundo valor {segundo_valor}')
elif segundo_valor > primeiro_valor:
    print(f'O segundo valor {segundo_valor} é maior que o primeiro valor {primeiro_valor}')
else:
    print(f'O primeiro valor {primeiro_valor} é igual ao segundo valor {segundo_valor}')