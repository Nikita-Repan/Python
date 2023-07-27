num = int(input())
x = num % 10
if num%100>=11 and num%100<=14:
    print(f'{num} грибов')
elif x==1:
    print(f'{num} гриб')
elif x > 1 and x <= 4:
    print(f'{num} гриба')
else:
    print(f'{num} грибов')
