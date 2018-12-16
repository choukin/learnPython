# -*- coding: utf-8 -*-
age = 3
if age >= 18:
    print('your age is ', age)
    print ('adult')
elif age> 6:
    print('your age is ', age)
    print('teenager')
else: 
    print('kid')        

birth = input('birth: ')
birth = int(birth)

if birth < 2000 :
    print('00前')
else:
    print('00后')    
##低于18.5：过轻
##18.5-25：正常
##25-28：过重
##28-32：肥胖
##高于32：严重肥胖

height = input('你的身高： ')
weight = input('你的体重（KG）： ')

bmi = float(weight) // (float(height)*float(height))
print(bmi)
if bmi < 18.5:
    print('过轻')
elif bmi <= 25:
    print('正常')
elif bmi <= 28:
    print('过重')
elif bmi <= 32:
    print('肥胖')
else:
    print('严重肥胖')                 