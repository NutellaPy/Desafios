print(10*'\033[35m-=\033[m')
print('\033[33mTabuada maluca 2.0!\033[m')
print(10*'\033[35m-=\033[m')
num = int(input('Digite um número: '))
for c in range(1, 11):
    print(f'{num} x {c} = {num * c}')
