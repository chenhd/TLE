# coding:utf-8
import md5
import hashlib









print hashlib.sha1('selenium书').hexdigest()
print hashlib.sha224('selenium书').hexdigest()
print hashlib.sha256('selenium书').hexdigest()
print hashlib.sha224('selenium书').hexdigest()

f = open(hashlib.sha224('selenium书').hexdigest(), 'w')
f.close()
