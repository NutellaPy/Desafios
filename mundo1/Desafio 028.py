from random import randint 
print('==JOGO DA ADIVINHAÇAO==') 
d = str(input('Deseja jogar? ')).strip().lower() 
if d == 'sim': 
  ns = randint(1,5) 
  ne = int(input('Digite um numero de 1 á 5: ')) 
  if ns == ne: 
    print('Parabens voce acertou!') 
  else: 
    print('voce errou! o numero certo era', ns) 
else: 
  print('ok, tchau!') 
