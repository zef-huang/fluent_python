# coding=utf8

# 滑动点击破解：
import json
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


class Crack():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36")

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

        self.driver.get('https://adv.mintegral.com/cn')
        # driver.page_source
        self.driver.switch_to.frame(0)

    def move_to_element(self):
        # 移动到点击位置
        driver = self.driver
        webdriver.ActionChains(driver).move_to_element(ele).perform()
        # 记录模拟点击的文件，并使用该文件进行移动
        self.move()
        webdriver.ActionChains(driver).click().perform()

    def move(self):
        """ Move mouse by using given track """ 
        self.track = []                                                                                        
        with open('track.txt','r') as f:                                                                
            self.track = json.load(f)                                                          
        for offset, sleeptime in self.track:                                                                   
            x, y = offset                                                                                      
            ActionChains(self.driver).move_by_offset(x,y).perform()                                            
            time.sleep(sleeptime)                                                                              
        ActionChains(self.driver).click().perform()  

if __name__ == '__main__':
    client = Crack()
    client.move()
    