x = int(input())
y = int(input())
if x < 0 and y > 0:
    print('II четверть')
if x < 0 and y < 0:
    print('III четверть')
if x > 0 and y > 0:
    print('I четверть')
if x > 0 and y < 0:
    print('IV четверть')
if x==0 or y==0:
    print('НА ОСИ!')

