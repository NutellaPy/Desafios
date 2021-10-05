Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
===
print('===ANALISADOR DE NUMEROS===') 
num=int(input('informe um numero(de 0 á 9999): ')) 
print('Analisando...') 
if num > 9999:
  print('Numero invalido! Digite um numero INTEIRO de 1 á 9999')
else:
  u=num // 1 % 10 
  d=num // 10 % 10 
  c=num // 100 % 10 
  m=num // 1000 % 10 
  print(f'Unidade: {u} \n Dezena: {d} \n Centena: {c} \n Milhar: {m} ') 
