print('\033[35m-=\033[m' * 17) 
print('\033[34mCalculador de emprestimo bancário') 
print('\033[35m-=\033[m' * 17) 
preço_da_casa = int(input('Digite o valor da casa: ')) 
salario = int(input('Digite o valor do seu salario: ')) 
anos = int(input('Em quantos anos você deseja parcelar? ')) 
meses = anos * 12 
valorp = preço_da_casa / meses 
if valorp > salario * (30 / 100): 
  print('Nao sera possivel fazer o emprestimo, pois a parcela corresponde a mais de 30 % do seu salario') 
else: 
  print(f'O valor da casa é {preço_da_casa}') 
  print(f'voce vai pagar em {meses} parcelas de {valorp}R$') 
