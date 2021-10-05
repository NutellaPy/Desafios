Crie um script q leia o nome do aluno, suas duas notas, e diga sua media 
===
print('===Calculador de media===') 
n=str(input('digite o nome do aluno: ')) 
nota1=float(input('digite a 1º nota: ')) 
nota2=float(input('digite a 2º nota: ')) 
m=(nota1+nota2)/2 
print(f'A media de {n} é {m:.1f}') 
