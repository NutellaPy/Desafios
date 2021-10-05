print('\033[35m-=\033[m' * 12) 
print('ANALISADOR DE TRIANGULOS') 
print('\033[35m-=\033[m' * 12) 
s1 = float(input('Digite o primeiro segmento: ')) 
s2 = float(input('Digite o segundo segmento: ')) 
s3 = float(input('Digite o terceiro segmeto: ')) 
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2: 
  print('È possivel formar um triangulo') 
else: 
  print('nao é possivel formar um triangulo') 
