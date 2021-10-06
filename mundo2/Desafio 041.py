from datetime import date
aa = date.today().year
nas = int(input('Digite o ano do seu nascimento: '))
idade = aa - nas
if idade <= 9:
  print('Voce é um nadador MIRIM!')
elif idade > 9 and idade <= 14:
  print('Voce é um nadador INFANTIL!')
elif idade > 14 and idade <= 19:
  print('Voce é um nadador JUNIOR!')
elif idade == 20:
  print('Voce é um nadador SENIOR!') 
else:
  print('Voce é um nadador MASTER!')
