 
print(14 * '\033[35m-=\033[m') 
print('CONVERSOR DE BASES NUMERICAS') 
print(14 * '\033[35m-=\033[m') 
ni = int(input('Digite um numero inteiro: ')) 
print('Escolha uma das bases para conversão:') 
print('[ 1 ] converter para BINÀRIO') 
print('[ 2 ] converter para OCTAL') 
print('[ 3 ] converter para HEXADECIMAL') 
ce = int(input('Esolha uma das opçoes: ')) 
if ce == 1: 
  print(f'{ni} convertido para BINÀRIO é {bin(ni)[2:]} ') 
elif ce == 2: 
  print(f'{ni} convertido para OCTAL é {oct(ni)[2:]}') 
elif ce == 3: 
  print(f'{ni} convertido para HEXADECIMAl é {hex(ni)[2:]}') 
else: 
  print('Opção \033[31mnão\033[m existe!!') 
