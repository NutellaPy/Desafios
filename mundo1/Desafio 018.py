Crie um script que leia um ângulo e diga seu seno, cosseno, tangente 
===
from math import radians, sin, cos, tan 
print('===ANGULOS MASTER=== ') 
ang=float(input('Digite o angulo: ')) 
sen=sin(radians(ang)) 
cos=cos(radians(ang)) 
tan=tan(radians(ang)) 
print(f'Angulo: {ang}° \n seno: {sen:.2f} \n cosseno: {cos:.2f} \n tan: {tan:.2f}') 
