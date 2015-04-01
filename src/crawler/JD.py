# coding:utf-8
from selenium import webdriver





def crawl(search_data):
    print search_data
    
    browser = webdriver.Chrome()
    browser.get('http://search.jd.com/Search?keyword=' + search_data)

    element = browser.find_element_by_xpath('/html/body[@class=\'root61\']/div[@class=\'w main\']/div[@class=\'right-extra\']/div[@class=\'m clearfix\']/div[@class=\'pagin fr\']/span[@class=\'page-skip\']/em')
    
#     print repr(element.text)
#     print element.text[3:-7]
#     print len(element.text)
    num_page = int(element.text[3:-7])
    print type(num_page), num_page, range(num_page)
    element = None
    
    for i in range(num_page):
        browser.get('http://search.jd.com/Search?keyword=' + search_data + '&psort=4' + '&page=' + str(2*i+1))
#         print i
        element = browser.find_element_by_xpath('/html/body[@class=\'root61\']')
        element = element.find_element_by_xpath('./div[@class=\'w main\']')
        element = element.find_element_by_xpath('./div[@class=\'right-extra\']')
        element = element.find_element_by_xpath('./div[@class=\'m psearch \']')
        
        
        





    browser.close()




if __name__ == '__main__':
# jd_search_data = search_data + '&enc=utf-8'
    crawl('selenium书' + '&enc=utf-8')
#     crawl('ipad' + '&enc=utf-8')

