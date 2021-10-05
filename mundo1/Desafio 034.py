print('==SALARIO==') 
s = int(input('Digite o valor do salario: ')) 
if s <= 1250: 
  a = s*(15/100) 
  sa = s + a 
if s >=1251: 
  a = s*(10/100) 
  sa = s + a 
print(f'O novo salario é \033[37m{sa}\033[m') 
