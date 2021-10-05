Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas. 
- Quantas letras ao todo (sem considerar espaços). 
- Quantas letras tem o primeiro nome. 
===
print('===CRAZY_NAMES===') 
n=str(input('Digite o nome: ')).strip() 
name_upper=n.upper() 
name_lower=n.lower() 
print(f'Nome com os caracteres captalizados: {name_upper}') 
print(f'Nome com os caracteres diminuidos: {name_lower}') 
print(f'{n} tem',len(n)-n.count(' '),'caracteres!') 
print(f'Seu primeiro nome tem', n.find(' '),' caracteres!') 
