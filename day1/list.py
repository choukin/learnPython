# -*- coding: utf-8 -*-

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])

sum = 0
for x in range(101):
    sum = sum + x

print(sum)    

sum1 = 0
n = 99
while n>0:
    sum1 = sum1 + n
    n = n -2
print(sum1)    

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello , %s !'%(name))


n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))    