class Gun:
    def __init__(self, gun_type, bullets_number=0):
        self.gun_type = gun_type
        self.bullets_number = bullets_number

    def add_bullets(self, bullets_num):
        self.bullets_number += bullets_num
        print(
            f'Added {bullets_num} bulltes, Now you have {self.bullets_number} bullets.')

    def shoot(self) -> bool:
        if self.bullets_number <= 0:
            print("shoot failed")
            return False

        self.bullets_number -= 1
        print('shoot successfully')
        return True


# 测试
'''
__name__是 Python 中的一个特殊内置变量，它的值取决于代码是如何被执行的。
基本概念
__name__主要有两种可能的值：
"__main__"​ - 当 Python 文件被直接运行时
模块名​ - 当 Python 文件被作为模块导入时

# 只有直接运行时才执行
'''
if __name__ == "__main__":
    ak47 = Gun("AK47")
    ak47.shoot()

    ak47.add_bullets(10)
    ak47.shoot()
    pass
