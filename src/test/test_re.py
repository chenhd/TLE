# coding:utf-8

import re

s = '正版书籍 基于Selenium 2的自动化测试&middot;从入门到精通 开发项目管理参考用书'

s2 = re.sub('&.*;', '', s)

print s
print s2


s3 = 'tb_00d443ebca729ae8f2754e49445e63ba056535dfcf9e048029ec8cbe.html'
m = re.match('.*html', s3)
if m :
    print m.group()











