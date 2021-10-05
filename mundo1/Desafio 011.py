Crie um script que calcule a área de uma parede ( em m²) e quanto de tinta são necessário para pintar a parede, considerando que 1l de tinta pintam 2m² 
===
print('===PROGRAMA DO PINTOR===') 
lar=float(input('digite a largura(em metros): ')) 
com=float(input('digite o comprimento(em metros): ')) 
area=lar*com 
tg=0.5*area 
print(f'A parede tem {area}m²') 
print(f'Para pintar {area}m² sao necessarios {tg}lts de tinta') 
