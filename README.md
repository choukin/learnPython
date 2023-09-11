# learnPython

[学习python](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)

## 简介

1. python 是一种高级语言，解释型语言

- 可以做 网络应用，包括网站、后台服务 等等，日常需要的小工具，包括系统管理员需要的脚本任务等等
- 不可以写操作系统，手机应用，3D 游戏

2.python 优缺点

- 优点：
  - 有完善的基础代码库和第三方库
  - 简单优雅
- 缺点  
  - 运行速度慢， 代码执行时会一行一行翻译成 CPU能理解的机器码
  - 代码不能加密，只能开源，和 javascipt 一样

3.安装  
   python 是跨平台的， 目前python 有两个不兼容的版本，2.x 3.x

- 命令行进入python python 交互式环境

```
    python
```

- 退出交互式命令

   ```
    exit()
   ```

4.python 解释器

    代码文件扩展名 `.py`
    - CPython

      官方解释器

    - IPython

       是基于CPython 之上的一个交互式解释器
       CPython用 `>>>` 作为提示符， 而 IPython 用 `In [序号]：`作为提示符

    - PyPy

        以执行速度为目标，采用 `JIT`技术，对Python进行动态编译，可以显著提高Python的执行速。

    - JyPthon

        是运行在Java 平台上的Python解析器，可以直接把Python 代码编译成 JAVA 字节码执行

    - IronPython

      IronPython 和 JyPhon类似只不过 IronPython是运行在微软 .Net 平台上的 Python解释器，可以把Python代码编译成 .Net 的字节码

5. 运行 python

- 在 Python 交互式模式下，可以直接输入代码然后执行，并立即都得到结果；
- 在命令行模式下，可以直接运行 `.py` 文件

6. 直接运行 py 文件

      window 上不能直接运行`.py`文件，但是 mac 和 linux 上可以，在第一行上加特殊注释

      ```shell
       #!/usr/bin/env python3
       print('hello, world')
      ```

      然后 通过命令给 文件执行权限

      ```bash
      chmod a+x hello.py
      ```

7.python 代码运行助手
   [learning.py](https://raw.githubusercontent.com/michaelliao/learn-python3/master/teach/learning.py)
   
   运行

   ```
   python learnning.py
   ```

8.输入输出
   `input()` 和 `print()` 是命令行下最基本的输入输出。

# Python 学习资料

-[Python入门教程](https://m.runoob.com/python3/python3-tutorial.html)

# 学习计划

 [] 争取每天学习一节
 [] [python 的数字](https://m.runoob.com/python3/python3-number.html)