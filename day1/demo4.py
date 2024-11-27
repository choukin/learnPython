'''
创建一个程序，定义两个数字类型的变量，并对它们执行各种算术运算。该程序应执行以下任务：

将两个数相加并打印和。
从第二个数中减去第一个数并打印差。
将两个数相乘并打印乘积。
将第一个数除以第二个数并打印商。
计算第一个数除以第二个数的余数并打印结果。
将第一个数的第二个数次幂并打印结果。
将第一个数自增 1 并打印更新后的值。
将第二个数自减 1 并打印更新后的值。
'''

num1 = 10
num2 = 5

# sum 是内置函数，所以避免使用 sum 作为变量名
sum_val = num1 + num2
print("和：", sum_val)

difference = num2 - num1
print("差：", difference)

product = num1 * num2
print("积：", product)

quotient = num1 / num2
print("商：", quotient)

remainder = num1 % num2
print("余数：", remainder)

power = num1 ** num2
print("幂：", power)

num1 += 1
print("num1 自增 1：", num1)

num2 -= 1
print("num2 自减 1：", num2)