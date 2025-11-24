# 定义URL模板并插入城市代码
url_template = "https://www.dianping.com/search/keyword/%s/0_$s"
url = url_template % 'code'
print(url)

a = {'a':1,'b':2}

c = {'c':3,'d':4}

print({'m':5,**c})