print('===VIAGEM===') 
d = int(input('Digite a distancia da viagem(km): ' )) 
if d <= 200: 
  pv = d*0.50 
else: 
  pv = d*0.45 
  print(f'O preço da viagem é {pv}') 
