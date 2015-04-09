# coding:utf-8
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from protobuf_file.item_pb2 import Item


def crawl(search_data):
    print search_data
    
    list_obj = []
    
    browser = webdriver.Chrome()
    browser.get('http://search.jd.com/Search?keyword=' + search_data + '&psort=4' + '&page=' + str(2*0+1))
    
#     browser.find_element_by_class_name('jumpto').click()
    
    element = browser.find_element_by_xpath('/html/body[@class=\'root61\']/div[@class=\'w main\']/div[@class=\'right-extra\']/div[@class=\'m clearfix\']/div[@class=\'pagin fr\']/span[@class=\'page-skip\']/em')
    
    
    
    
    
#     print repr(element.text)
#     print element.text[3:-7]
#     print len(element.text)
    num_page = int(element.text[3:-7])
#     print type(num_page), num_page, range(num_page)
    element = ''
    
    for i in range(num_page):
        browser.get('http://search.jd.com/Search?keyword=' + search_data + '&psort=4' + '&page=' + str(2*i+1))
        
        
        
        element = browser.find_element_by_xpath('/html/body[@class=\'root61\']/div[@class=\'w main\']/div[@class=\'right-extra\']/div[@class=\'m clearfix\']/div[@class=\'pagin fr\']/span[@class=\'page-skip\']/em')
    
        

        element = browser.find_element_by_xpath('/html/body[@class=\'root61\']')
        element = element.find_element_by_xpath('./div[@class=\'w main\']')
        element = element.find_element_by_xpath('./div[@class=\'right-extra\']')
        element = element.find_element_by_xpath('./div[@id=\'plist\']')
        element = element.find_element_by_xpath('./ul')
        
        list_item = element.find_elements(by=By.XPATH, value='./li')
        
        
        ActionChains(browser).context_click(list_item[29]).perform()
        time.sleep(1)
        list_item = element.find_elements(by=By.XPATH, value='./li')
        
#         print 'len : ' + str(len(list_item))
        for i in range(len(list_item)):
            
            item = list_item[i]
            ActionChains(browser).context_click(item).perform()
#             print i
            obj = Item()
            try:
                row0_element = item.find_element_by_xpath('./div[@class=\'p-img\']')
            except:
                item = item.find_element_by_xpath('./div')
                row0_element = item.find_element_by_xpath('./div[@class=\'p-img\']')
            row0_element = row0_element.find_element_by_xpath('./a')
            obj.item_url = row0_element.get_attribute('href')
            row0_element = row0_element.find_element_by_xpath('./img')
            obj.img_url = row0_element.get_attribute('src')
             
            row1_element = item.find_element_by_xpath('./div[@class=\'p-name\']')
            obj.title = row1_element.text
            
            row3_element = item.find_element_by_xpath('./div[@class=\'p-price\']')
            obj.price = row3_element.find_element_by_xpath('./strong').text[1:]
            
            
            
            row8_element = item.find_element_by_xpath('./div[@class=\'extra\']')
            obj.num_sell = row8_element.find_element_by_xpath('./a').text[3:-3]
            
            list_obj.append(obj)
            print obj
#             break
#         print '*' * 90
        break




    browser.close()
    
    return list_obj

    

if __name__ == '__main__':
# jd_search_data = search_data + '&enc=utf-8'
#     crawl('selenium书' + '&enc=utf-8')
#     crawl('ipad' + '&enc=utf-8')
    crawl('linux' + '&enc=utf-8')

