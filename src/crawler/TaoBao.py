# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# search_data : selenium%CA%E9
def crawl(search_data):
    print search_data
    
    browser = webdriver.Chrome()
    browser.get('http://s.taobao.com/search?q=' + search_data)
    
    element = browser.find_element_by_xpath('/html/body/div[@id=\'page\']/div[@id=\'main\']/div[@class=\'grid-total\']/div[@class=\'grid-left\']/div[@id=\'mainsrp-pager\']/div[@class=\'m-page g-clearfix\']/div[@class=\'wraper\']/div[@class=\'inner clearfix\']/div[@class=\'total\']')
#     print element.get_attribute('outerHTML')
#     print element.text
#     print len(element.text)
    num_page = int(element.text[2:-3])
    print type(num_page), num_page, range(num_page)
#     一页有44个物品，第一页48？
    element = None
    

    
    for i in range(num_page):
        browser.get('http://s.taobao.com/search?q=' + search_data + '&s=' + str(i*44) + '&sort=price-asc')
        
        element = browser.find_element_by_xpath('/html/body')
        element = element.find_element_by_xpath('./div[@id=\'page\']')
        element = element.find_element_by_xpath('./div[@id=\'main\']')
        element = element.find_element_by_xpath('./div[@class=\'grid-total\']/div[@class=\'grid-left\']/div[@id=\'mainsrp-itemlist\']')
        element = element.find_element_by_xpath('./div[@class=\'m-itemlist\']')
        element = element.find_element_by_xpath('./div[@class=\'grid\']')
        element = element.find_element_by_xpath('./div[@id=\'J_itemlistCont\']')
        
        list_item = element.find_elements(by=By.XPATH, value='./div[@class=\'item  \']')
        
        print list_item[0].text
        print 
        for item in list_item:

            pass
        

    
#     print '*'
#     element = browser.find_element(by=By.XPATH, value='/html')
#     element = element.find_element(by=By.XPATH, value='./body')
#     element = element.find_element(by=By.XPATH, value='./div[@id=\'page\']') 
#     element = element.find_element(by=By.XPATH, value='./div[@id=\'main\']')
#     element = element.find_element(by=By.XPATH, value='./div[@class=\'grid-total\']/div[@class=\'grid-left\']/div[@id=\'mainsrp-itemlist\']')
#     element = element.find_element(by=By.XPATH, value='./div[@class=\'m-itemlist\']')
#     element = element.find_element(by=By.XPATH, value='./div[@class=\'grid\']')
#     element = element.find_element(by=By.XPATH, value='./div[@id=\'J_itemlistCont\']')
#     elements = element.find_elements(by=By.XPATH, value='./div[@class=\'item  \']')
#     
#     for item in elements:
#         
#         
#         pass
#     
#     
#     
#     html = elements[0].get_attribute('outerHTML')
#     print html




    browser.close()
#     browser.quit()


if __name__ == '__main__':
    crawl('selenium%CA%E9')
#     crawl('书')


