import math
def quadratic(a,b ,c):
    p = b * b - 4 * a * c
    if p >= 0 and a!=0:
        x1 = (-b + math.sqrt(p))/2*a
        x2 = (-b - math.sqrt(p))/2*a
        print(x1,x2)
        return x1, x2
    else :
        return ('wrong number')
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败1')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败2')
else:
    print('测试成功')