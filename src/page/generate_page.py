# coding:utf-8
from __builtin__ import file
import hashlib
import sys

from jinja2 import Template

from protobuf_file.item_pb2 import Item


reload(sys)   
sys.setdefaultencoding('utf8')

def tb_generate(search_data):
    
    file_name = hashlib.sha224(search_data).hexdigest()
    
    file = open('../data/tb_' + file_name, 'r')
    list_item = []
    for line in file:
        try:
            pb_string = line.strip('\n')
            item = Item()
            item.ParseFromString(pb_string)
            list_item.append(item)
        except Exception as e:
            print e
        
    tmpl = Template(open('./item_template.html').read())

    print len(list_item)
    print list_item[0]
    file = open('./tb_' + file_name + '.html', 'w')
    file.write(tmpl.render(list_item = list_item))
    file.close()

def tm_generate(search_data):
    
    file_name = hashlib.sha224(search_data).hexdigest()
    
    file = open('../data/tm_' + file_name, 'r')
    list_item = []
    for line in file:
        try:
            pb_string = line.strip('\n')
            item = Item()
            item.ParseFromString(pb_string)
            list_item.append(item)
        except Exception as e:
            print e
        
    tmpl = Template(open('./item_template.html').read())

    print len(list_item)
    print list_item[0]
    file = open('./tm_' + file_name + '.html', 'w')
    file.write(tmpl.render(list_item = list_item))
    file.close()

def jd_generate(search_data):
    
    file_name = hashlib.sha224(search_data).hexdigest()
    
    file = open('../data/jd_' + file_name, 'r')
    list_item = []
    for line in file:
        try:
            pb_string = line.strip('\n')
            item = Item()
            item.ParseFromString(pb_string)
            list_item.append(item)
        except Exception as e:
            print e
        
    tmpl = Template(open('./item_template.html').read())

    print len(list_item)
    print list_item[0]
    file = open('./jd_' + file_name + '.html', 'w')
    file.write(tmpl.render(list_item = list_item))
    file.close()

def generate(search_data):
    try:
        tb_generate(search_data)
    except Exception as e:
        print e
        pass
    try:
        tm_generate(search_data)
    except:
        pass
    try:
        jd_generate(search_data)
    except:
        pass

    tmpl = Template(open('./all_template.html').read())

    file_name = hashlib.sha224(search_data).hexdigest()
    file = open('./all_' + file_name + '.html', 'w')
    file.write(tmpl.render(tb = 'tb_'+file_name+'.html', tm = 'tm_'+file_name+'.html', jd = 'jd_'+file_name+'.html'))
    file.close()
    
    
#     print tmpl.render(tb = './tb_'+file_name+'.html', tm = './tm_'+file_name+'.html', jd = './jd_'+file_name+'.html')

    return './all_' + file_name + '.html'




if __name__ == '__main__':
    generate('selenium书')








