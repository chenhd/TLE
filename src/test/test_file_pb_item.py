from protobuf_file.item_pb2 import Item

print 'hello'
file = open('../data/jd_00d443ebca729ae8f2754e49445e63ba056535dfcf9e048029ec8cbe', 'r')
print 'hello'
list_item = []
for line in file:
    pb_string = line.strip('\n')
    item = Item()
    item.ParseFromString(pb_string)
    list_item.append(item)

for item in list_item:
    print item










