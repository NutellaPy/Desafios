print(8*'\033[33m-=\033[m')
print('CALCULADORA IMC')
print(8*'\033[33m-=\033[m')
alt = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (alt**2)
print(f'Seu indice de massa corporal é {imc:.0f}!', end = ' ')
if imc < 18.5:
  print('Considerado abaixo do peso!')
elif imc >= 18.5 and imc < 25:
  print('Considerado peso ideal!')
elif imc >= 25 and imc < 30:
  print('Considerado obesidade!')
elif imc >= 30:
  print('Considerado obesidade mórbida!')
