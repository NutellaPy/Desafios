n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2 
print(f'A media foi \033[35m{m}\033[m!')
if m < 5:
  print('ALUNO REPROVADO!')
elif m >= 5 and m < 6.9:
  print('ALUNO DE RECUPERAÇÃO!')
elif m >= 7:
  print('ALUNO APROVADO!')
