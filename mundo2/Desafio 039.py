from datetime import date
nas = int(input('Digite o ano do seu nascimento:'))
aa = (date.today().year)
alis = 18
f = nas + alis - aa
if aa - nas < alis:
  print(f'Voce ainda vai se alistar. Faltam {f} anos!')
elif aa - nas > alis:
  print(f'Ja passou da hora de se alistar. ja passaram {f*-1} anos')
elif aa - nas == alis:
  print('Chegou a sua hora de se alistar!')
