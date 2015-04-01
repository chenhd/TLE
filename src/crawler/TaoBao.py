# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
# import time
from protobuf_file.item_pb2 import Item


def crawl(search_data):
# search_data : selenium%CA%E9
    print search_data
    
    browser = webdriver.Chrome()
    browser.get('http://s.taobao.com/search?q=' + search_data)
    
    element = browser.find_element_by_xpath('/html/body/div[@id=\'page\']/div[@id=\'main\']/div[@class=\'grid-total\']/div[@class=\'grid-left\']/div[@id=\'mainsrp-pager\']/div[@class=\'m-page g-clearfix\']/div[@class=\'wraper\']/div[@class=\'inner clearfix\']/div[@class=\'total\']')
#     print element.get_attribute('outerHTML')
#     print element.text
#     print len(element.text)
    num_page = int(element.text[2:-3])
    print type(num_page), num_page, range(num_page)
    element = None
    

    
    for i in range(num_page):
#     一页有44个物品，第一页48？
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
            obj = Item()
            
            row0_element = item.find_element_by_xpath('./div[@class=\'pic-box J_MouseEneterLeave J_PicBox\']')
            row0_element = row0_element.find_element_by_xpath('./div[@class=\'pic-box-inner\']')
            row0_element = row0_element.find_element_by_xpath('./div[@class=\'pic\']')
            row0_element = row0_element.find_element_by_xpath('./a[@class=\'pic-link J_U2IStat J_ItemPicA\']')
            obj.item_url = row0_element.get_attribute('href')
            row0_element = row0_element.find_element_by_xpath('./img[@class=\'J_ItemPic img\']')
            obj.img_url = row0_element.get_attribute('data-src')
            obj.title = row0_element.get_attribute('alt')

            row1_element = item.find_element_by_xpath('./div[@class=\'row row-1 g-clearfix\']')
            obj.price = row1_element.find_element_by_xpath('./div[@class=\'price g_price g_price-highlight\']').find_element_by_xpath('./strong').text
            obj.num_sell = row1_element.find_element_by_xpath('./div[@class=\'deal-cnt\']').text[:-3]


            
            print obj
                
            break
        break






    browser.close()
#     browser.quit()


if __name__ == '__main__':
    crawl('selenium%CA%E9')
#     crawl('书')


