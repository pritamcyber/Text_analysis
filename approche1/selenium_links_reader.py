# import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def file_creater_using_selenium(url_id:tuple):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    # options.add_argument('log-level=3')
   
    # options.add_argument('--no-sandbox')
    # options.add_argument("--disable-notifications")
# 
    
    driver = webdriver.Chrome(options=options)
    driver.minimize_window()
    driver.get(url_id[1])
    # print(driver)
    driver.implicitly_wait(5)
    # print( driver.find_element(By.XPATH,'//*[@id="post-5274"]/div[1]/div[1]/div[2]/div[2]/header/h1').text)    
    title = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "td-post-title")))
    print(title.find_element(By.TAG_NAME,"h1").text)
    # td-post-content
    text_of_title = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "td-post-content")))
    print(text_of_title.text)
    # titleara = []
    # print(driver)
    count = 0

    # print(title.tag_name)
    # for i in range(len(title)):
    #     try:

    #         titleara.append(title[i].text)
    #         count+=1
    #     except IndexError as e:
    #             print(e)
    #     except Exception as ee :
    #         try:
    #             title = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "p")))
    #             titleara.append(title[i].text)
    #         except Exception as p :
    #             print(p)
    