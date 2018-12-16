# -*- coding: utf-8 -*-
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

s1 = 72
s2 = 85

r = '{0} 成绩提升了 {1:.1f} %'

s3 = (s2-s1)%s1

print(r.format('小明',s3))

print('%s 成绩提升了 %.1f %%'%('小明', s3))

ch = '中文'
chencode = ch.encode('utf-8')
print(chencode)
chdecode = chencode.decode('utf-8')
print(chdecode)