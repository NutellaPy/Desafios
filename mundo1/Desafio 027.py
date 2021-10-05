Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. 
===
name = str(input('Digite seu nome completo: ')).strip().split() 
print('Prazer em te conhecer', name[0],name[len(name)-1] ) 
===
Foi utilizado o '-1' pois a funçao len() começar a ler do 1 em diante. 
E a split lê do 0 em diante. Sendo assim para pegar o ultimo nome é nescessario subtrair por 1  
