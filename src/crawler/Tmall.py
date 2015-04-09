# coding:utf-8
import re

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from protobuf_file.item_pb2 import Item


def crawl(search_data):
# search_data : selenium%CA%E9
    print search_data
    
    list_obj = []
    
    browser = webdriver.Chrome()
    browser.get('http://list.tmall.com/search_product.htm?q=' + search_data + '&s=' + str(0*60) + '&sort=p')
    
    element = browser.find_element_by_xpath('/html/body/div[@class=\'page\']/div[@id=\'mallPage\']/div[@id=\'content\']/div/div[@class=\'ui-page\']/div[@class=\'ui-page-wrap\']/b[@class=\'ui-page-skip\']/form[@name=\'filterPageForm\']')
    
#     print element.get_attribute('outerHTML')
#     print type(element.text), len(element.text)
#     print element.text[1:-8]
    num_page = int(element.text[1:-8])
    print num_page
    element = None
    
    

    for i in range(num_page):
#     一页有60个物品
        browser.get('http://list.tmall.com/search_product.htm?q=' + search_data + '&s=' + str(i*60) + '&sort=p')
        
        
#         element = browser.find_element_by_xpath('/html/body[@class=\'pg\']')
#         element = element.find_element_by_xpath('./div[@class=\'page\']')
#         element = element.find_element_by_xpath('./div[@id=\'mallPage\']')
#         element = element.find_element_by_xpath('./div[@id=\'content\']')
#         element = element.find_elements_by_xpath('./div[@class=\'main       \']')
#         element = element.find_element_by_xpath('./div[@id=\'J_ItemList\']')
        
        list_item = browser.find_elements(by=By.CLASS_NAME, value='product')
        
        for item in list_item:
            try:
                obj = Item()
                
    #             print item.get_attribute('outerHTML')
                ActionChains(browser).context_click(item).perform()
                
                item = item.find_element_by_xpath('./div[@class=\'product-iWrap\']')
                row0_element = item.find_element_by_xpath('./div[@class=\'productImg-wrap\']')
                row0_element = row0_element.find_element_by_xpath('./a[@class=\'productImg\']')
                obj.item_url = row0_element.get_attribute('href')
                obj.img_url = row0_element.find_element_by_xpath('./img').get_attribute('src')
    
                row1_element = item.find_element_by_xpath('./p[@class=\'productPrice\']')
                obj.price = row1_element.find_element_by_xpath('./em').get_attribute('title')
                
    #             print obj
                
    #             row2_element = item.find_element_by_xpath('./p[@class=\'productTitle\']')
                row2_element = item.find_elements_by_xpath('./div')[1]
                obj.title = row2_element.find_element_by_xpath('./a').get_attribute('title')
                obj.title = re.sub('&.*;', '', obj.title)
                
                row4_element = item.find_element_by_xpath('./p[@class=\'productStatus\']')
                obj.num_sell = row4_element.find_element_by_xpath('./span/em').text[:-1]
                
                list_obj.append(obj)
                print obj
            except:
                pass
            
#             break
        break
        

    browser.close()

    return list_obj


if __name__ == '__main__':
#     crawl('selenium%CA%E9')
#     crawl('%CA%E9')
    crawl('food')