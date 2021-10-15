soma = 0
count = 0 
for np in range(1, 501, 2):
  if np % 3 == 0:
    count += 1
    soma += np
print(f'A soma dos {count} números é {soma}')
