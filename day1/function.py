def my_abs(x):
    if not isinstance(x,(int, float)):
        raise TypeError('bad operand type')
    if x > 0 :
        return x
    else:
       return -x

# print(my_abs(-3))

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L    

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum    

def product(*x):
    productnum = 1
    for n in x:
        productnum = productnum * n
    return productnum    

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')