'''
1. 算数运算
+ - * / % 
// 整除
2.比较运算
 > < >= <= == !=
3.赋值运算
 Python 独有互换操作
 a,b = b,a

 = += -= *=
4.逻辑运算
 and 并且
 or 或者
 not 非
 优先级
 括号 > not > and > or
5.成员运算
in
not in
'''


n = 1
sum = 0 
while n <=100:
  sum +=n
  n+=1

print(sum)
n,sum = sum, n
print(sum)


lst = [1,2,3,4]
print(6 in lst)
print(4 in lst)