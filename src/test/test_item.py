# coding:utf-8

from protobuf_file.item_pb2 import Item


item = Item()
item.title = unicode('中文')
item.price = '123123'
item.num_sell = '199'
item.img_url = 'qwewqeqwewqeqwe'
item.item_url = '564ewqe6wq8e4wqe'

print item

s = item.SerializeToString()
s = item.SerializeToString()
print s
i = Item()
i.ParseFromString(s)
print i
print i.title


