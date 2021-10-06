print(10*'\033[35m-=\033[m')
print('Forma de pagamento!')
print(10*'\033[35m-=\033[m')
valor = float(input('Digite o valor do produto: '))
dinheiro_cheque = valor * (90/100)
cartao = valor * (95/100)
cartao2x = valor / 2
print('OPÇOES: \n[ 1 ] Dinheiro/Cheque 10% de desconto \n[ 2 ] Cartão')
escolha1 = int(input('Escolha uma opção: '))
if escolha1 == 1:
  print(f'Total a pagar: R${dinheiro_cheque:.2f}')
elif escolha1 == 2:
  print('Cartão: \n[ 1 ] A vista 5% de desconto \n[ 2 ] 2x sem juros \n[ 3 ] 3x ou mais. 20% de juros')
  escolha2 = int(input('Escolha uma opção: '))
  if escolha2 == 1:
    print(f'Total a pagar: R${cartao:.2f}')
  elif escolha2 == 2:
    print(f'Total a pagar: 2x de R${cartao2x:.2f}')
  elif escolha2 == 3:
    vp = int(input('Quantidade de parcelas: '))
    valorpar = (valor / vp)
    aumento = valorpar + (valorpar * (20/100))
    print(f'Total a pagar {vp}x de R${aumento:.2f}')
