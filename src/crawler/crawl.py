# coding:utf-8
import urllib2
from crawler import TaoBao, Tmall, JD


# 注意: 最好不要空格
#  search_data : selenium书
def crawl(search_data):

    tb_search_data = urllib2.quote(search_data.decode('UTF-8').encode('GBK'))
#     TaoBao.crawl(tb_search_data)
    
    tm_search_data = tb_search_data
    Tmall.crawl(tm_search_data)
#     
#     jd_search_data = search_data + '&enc=utf-8'
#     JD.crawl(jd_search_data)




if __name__ == '__main__':
    crawl('selenium书')

















