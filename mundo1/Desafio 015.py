Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado. 
===
print('===ALUGUEL DE CARROS===') 
d=int(input('Quantos dia voce usou o carro? ')) 
km=int(input('aproximadamente, quantos kms voce andou com o carro? ')) 
ppd=d*60 
ppkm=km*0.15 
pap=ppd+ppkm 
print(f'valor a pagar é {pap}') 
