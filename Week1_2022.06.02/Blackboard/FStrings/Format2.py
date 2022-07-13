# Demonstrate use of print(f)
num1 = 1
num2 = 5.6897
num3 = 1024.678

print(f'The first number, {num1:d}, the second number {num2:.2f}')
print(f'the third number         {num3:6.2f}')
print(f'                ------------')
print(f'the third number|{num3:>12.2f}|')
print(f'the third number|{num3:<12.2f}|')
print(f'the third number|{num3:^12.2f}|')
print(f'                ------------')
print(f'the third number\t|{num3:10,.2f}|')
print(f'the third number\t$|{num3:,.2f}|')
print(f'the second number\t|{num2:,.2f}%|')
print(f'The total of the second and third numbers is {num2 + num3:.2f}')
