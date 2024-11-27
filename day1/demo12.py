def greet(name, age ,gender="保密"):
  print(f"你好，我叫{name}，今年{age}岁，性别{gender}")

 # 传入位置参数
greet("小明", 18)
greet("小红", 20,"女")
greet(*["韶瑾",6,"男"])

# 传入关键字参数
greet(age=0.2,gender="男", name="韶珩")
greet("韶珩",age=0.2,gender="男")

def diyGreet(arg, *arg1, **arg2):
  print(arg)
  print(arg1)
  print(arg2)

diyGreet(1,2,3,'4','test',True,7,8,9,a=10,b=20,c=30)
diyGreet(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,a=10,b=20,c=30)
