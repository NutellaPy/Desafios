Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez. 
===
name=str(input('Digite uma frase: ')).strip() 
name_m=name.lower() 
xa=str(name_m.replace('á','a').replace('ã','a').replace('â','a').count('a')) 
print(f"A letra 'a' aparece {xa} vezes") 
print("A primeira letra 'a' esta em ", name_m.replace('á','a').replace('ã','a').replace('â','a').find('a')+1 ) 
print("a ultima letra 'a'esta em ",name.replace('á','a').replace('ã','a').replace('â','a').rfind('a')+1) 
