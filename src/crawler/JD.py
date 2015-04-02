# coding:utf-8
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from protobuf_file.item_pb2 import Item


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
        

        element = browser.find_element_by_xpath('/html/body[@class=\'root61\']')
        element = element.find_element_by_xpath('./div[@class=\'w main\']')
        element = element.find_element_by_xpath('./div[@class=\'right-extra\']')
        element = element.find_element_by_xpath('./div[@class=\'m psearch \']')
        element = element.find_element_by_xpath('./ul')
        
        list_item = element.find_elements(by=By.XPATH, value='./li')
        
        i = 1
        for item in list_item:
            print i
            i += 1
            
            obj = Item()

            item.click()

                

            row0_element = item.find_element_by_xpath('./div[@class=\'p-img\']')
            row0_element = row0_element.find_element_by_xpath('./a')
            obj.item_url = row0_element.get_attribute('href')
            row0_element = row0_element.find_element_by_xpath('./img')
            obj.img_url = row0_element.get_attribute('src')
            
            row1_element = item.find_element_by_xpath('./div[@class=\'p-name\']')
            obj.title = row1_element.text
            print obj
            
            
            
#             break
        break



    browser.close()




if __name__ == '__main__':
# jd_search_data = search_data + '&enc=utf-8'
    crawl('selenium书' + '&enc=utf-8')
#     crawl('ipad' + '&enc=utf-8')

