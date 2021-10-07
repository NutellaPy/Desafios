from random import choice
print(12*'\033[35m-_\033[m')
jogadas = [0, 1, 2]
print('PEDRA, PAPEL OU TESOURA?')
print('[ 0 ] PEDRA \n[ 1 ] PAPEL \n[ 2 ] TESOURA' )
jdm = choice(jogadas)
if jdm == 0:
  jepm = 'PEDRA'
elif jdm == 1:
  jepm = 'PAPEL'
else:
  jepm = 'TESOURA'
jdp = int(input('Escolha:'))
if jdm == jdp: #empate
  print(f'A MAQUINA TAMBEM ESCOLHEU {jepm}, EMPATE!')
#maquina ganha
elif jdm == 0 and jdp == 2:
  print(f'A MAQUINA JOGOU {jepm}, VOCE PERDEU!')
elif jdm == 1 and jdp == 0:
  print(f'A MAQUINA JOGOU {jepm}, VOCE PERDEU!')
elif jdm == 2 and jdp == 1:
  print(f'A MAQUINA JOGOU {jepm}, VOCE PERDEU!')
#jogador ganha
if jdp == 0 and jdm == 2:
  print(f'A MAQUINA JOGOU {jepm}, VOCE GANHOU!')
elif jdp == 1 and jdm == 0:
  print(f'A MAQUINA JOGOU {jepm}, VOCE GANHOU!')
elif jdp == 2 and jdm == 1:
  print(f'A MAQUINA JOGOU {jepm}, VOCE GANHOU!')
