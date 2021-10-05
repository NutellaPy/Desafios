Crie um script que leia um número e mostre, o seu dobro, triplo, e raiz quadrada 
===
n1=int(input('Digite um número: ')) 
d=n1*2 
t=n1*3 
rq=n1**(1/2) 
print('O dobro é {}, o triplo é {} e a raiz quadrada é {}'.format(d, t, rq)) 
===
melhorado:
===
from math import sqrt
n = int(input('Digite um numero: ')) 
d = n*2
t = n*3
r = sqrt(n)
print(f'o dobro de {n} é {d} o triplo é {t} e a raiz quadrada é {r:.2f}')
