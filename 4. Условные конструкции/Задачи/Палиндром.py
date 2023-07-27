num = int(input())
x1=num%10
x4=num//1000
x2=num//10%10
x3=num//100%10
if x4==x1 and x3==x2 :
    print('число Палиндром')
else:
    print('число не Палиндром')