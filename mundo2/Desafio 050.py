soma = 0
for c in range (1, 7):
  a=int(input('Digite um numero: '))
  if a % 2 == 0:
    soma += a
print(f'A somade todos os numeros pares é {soma}')
