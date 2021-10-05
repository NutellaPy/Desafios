Crie um script que calcule a hipotenusa 
===
from math import hypot 
print('==CALCULADORA DE HIPOTENUSA==') 
ca=float(input('Digite o cateto adjacente: ')) 
co=float(input('Digite o cateto oposto: ')) 
hi=hypot(ca, co) 
print(f'A hipotenusa é {hi:.2f}') 
