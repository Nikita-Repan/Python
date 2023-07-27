num= int(input())
x1=num%10
x2=num//10%10
x3=num//100%10
x4=num//1000
renum=x1*1000+x2*100+x3*10+x4
print(renum)
