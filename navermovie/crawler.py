from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

class NaverMovie:
    def __init__(self):
        driver = webdriver.Chrome('chromedriver')
        driver.get(url)
        #한 줄 코딩 driver, 컨트롤 스페이스
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        print(soup)