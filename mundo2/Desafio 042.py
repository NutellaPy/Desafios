print(17*'\033[35m-=\033[m')
print('ANALISADOR AVANÇADO DE TRIANGULOS')
print(17*'\033[35m-=\033[m')
s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2: 
  print('È possivel formar um triangulo', end =' ') 
  if s1 == s2 and s2 == s3:
    print('EQUILÁTERO')
  elif s1 == s2 and s2 != s3:
    print('ISÓSCELES')
  elif s1 != s2 and s2 != s3:
    print('ESCALENO')
else: 
  print('nao é possivel formar um triangulo') 
