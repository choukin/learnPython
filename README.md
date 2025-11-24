# learnPython

[学习python](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)

## 简介

1. python 是一种高级语言，解释型语言

- 可以做 网络应用，包括网站、后台服务 等等，日常需要的小工具，包括系统管理员需要的脚本任务等等
- 不可以写操作系统，手机应用，3D 游戏

2.python 优缺点
=====
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

 [] [JavaScript 工程师的 Python 指南](https://luckrnx09.com/python-guide-for-javascript-engineers/zh-cn/about-the-book)

 [] [python文档](https://docs.python.org/zh-cn/3.13/index.html)




## 修改文件为可执行文件

```sh
chmod +x hello_world.py
```


### 查看python 安装位置

```sh
which python3
# /opt/homebrew/bin/python3
```

## 安装项目中依赖多个安装包

```sh
pip3 install -r requirements.txt
```

## 安装某个包时临时制定源

```sh
pip install package_name -i
```

- [清华大学](https://pypi.tuna.tsinghua,edu.cn/simple)
- [阿里云](https://mirrors.aliyun.com/pypi/simple/)
- [中国科学技术大学](https://pypi.mirrors.ustc.edu.cn/simple/)
- [豆瓣](https://pypi.douban.com/simple/)

## anaconda 使用

### 创建新环境

```sh
conda create -n {myenv} python=3.8
```

### 激活环境

```sh
conda activate myenv
```

### 停用环境

```sh
conda deactivate 
```

### 列出所有环境

```sh
conda info -e 
#/ 或者
conda env list
```

### 删除环境

```sh
conda remove --name myenv --all
```

### 包管理

```sh
# 安装
conda install package_name

# 安装制定包
conda install package_name=2.0.1

# 更新包
conda update package_name

# 卸载包
conda remove package_name

# 查看安装的包
conda list

# 搜索包
conda search package_name

```
