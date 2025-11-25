s = '网络了'
bs1 = s.encode('gbk')
bs2=s.encode('utf-8')

print(bs1)
print(bs2)


# gpk 转 utf-8

s2 = bs1.decode('gbk') # 解码
bs2 = s2.encode('utf-8') # 编码

print(bs2)


s3 = '你好aaa妈妈'

print(s3.encode('utf-8'))