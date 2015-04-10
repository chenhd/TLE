# coding:utf-8
import urllib2
from crawler import TaoBao, Tmall, JD
import hashlib




def store(pb_list, file_name):
    file = open(file_name, 'w')
    for item in pb_list:
        file.write(item.SerializeToString() + '\n')
    file.close()


# 注意: 最好不要空格
#  search_data : selenium书
def crawl(search_data):
    file_name = hashlib.sha224(search_data).hexdigest()
    
    tb_search_data = urllib2.quote(search_data.decode('UTF-8').encode('GBK'))
    tb_list_obj = TaoBao.crawl(tb_search_data)
    store(tb_list_obj, '../data/tb_' + file_name)
    print 'len(tb_list_obj)',len(tb_list_obj)
    
    tm_search_data = urllib2.quote(search_data.decode('UTF-8').encode('GBK'))
    tm_list_obj = Tmall.crawl(tm_search_data)
    store(tm_list_obj, '../data/tm_' + file_name)
    print 'len(tm_list_obj)', len(tm_list_obj)

    jd_search_data = search_data + '&enc=utf-8'
    jd_list_obj = JD.crawl(jd_search_data)
    store(jd_list_obj, '../data/jd_' + file_name)
    print 'len(jd_list_obj)', len(jd_list_obj)
     
#     print tb_list_obj[0], tm_list_obj[0], jd_list_obj[0]
    


if __name__ == '__main__':
    crawl('selenium书')

















