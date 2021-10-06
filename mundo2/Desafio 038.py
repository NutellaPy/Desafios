n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
if n1 > n2:
  print(f'O numero {n1} é o maior!')
elif n2 > n1:
  print(f'O numero {n2} é o maior!')
elif n1 == n2:
  print(f'Os numeros {n1} e {n2} tem o mesmo valor')
