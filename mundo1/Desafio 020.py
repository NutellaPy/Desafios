Faça um script que leia o nome dos quatro alunos e mostre a ordem sorteada. 
===
from random import shuffle 
n1=str(input('Digite o 1° aluno: ')) 
n2=str(input('Digite o 2° aluno: ')) 
n3=str(input('Digite o 3° aluno: ')) 
n4=str(input('Digite o 4° aluno: ')) 
l=[n1, n2, n3, n4] 
shuffle(l) 
print(f'A ordem embaralhada é: \n {l}') 
