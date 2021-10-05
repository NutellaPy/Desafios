Crie um script que some dois numeros 
===
n1=int(input('digite um numero: ')) 
n2=int(input('digite outro numero: ')) 
s=n1+n2 
print('a soma de {} e {} é {}'.format(n1, n2,s)) 
===
Com cores: 
===
n1 = int(input('Digite um numero: ')) 
n2 = int(input('Digite um numero: ')) 
s = n1 + n2 
l = '\033[m' 
a = '\033[33m' 
b = '\033[34m' 
m = '\033[35m' 
print(f'A soma de {a}{n1}{l} e {b}{n2}{l} é {m}{s}{l}') 
