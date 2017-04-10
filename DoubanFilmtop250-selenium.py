
"""
Created on 2016.12.29(python2.*)    @author:Easstmout

修改:杨药师 2017.03.28(python3.5) .etc
"""


import time, re, sys, codecs, requests
#urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




#爬虫函数
def crawl(url):
    driver.get(url)
    print('爬取信息如下：\n')
    print('豆瓣电影250：序号 \t电影名\t 评分 \t评价人数 \r\n')
    infofile.write('豆瓣电影250： \r\n序号 \t\t影片名 \t\t评分 \t\t评分人数 \r\n')
    content = driver.find_elements_by_xpath("//div[@class='item']")
    for tag in content:
        print(tag.text)
        infofile.writelines(tag.text + "\r\n")



#主函数
if __name__ == '__main__':
    driver = webdriver.Chrome()
    infofile = codecs.open("Result_Douban.txt", 'a', "utf-8")
    url = 'https://movie.douban.com/top250?format=text'
    i = 0
    while i<10:
        print('\r\n页码', (i+1))
        num = i*25
        url = 'https://movie.douban.com/top250?start=' + str(num) + '&filter='
        crawl(url)
        infofile.write("\r\n\r\n")
        i += 1
    infofile.close()

