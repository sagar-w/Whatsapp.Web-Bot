from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
 
# path = 'C:/Users/Sagar/Downloads/chromedriver.exe'
path = 'S:/7th_Sem/STQA/2nd/chromedriver.exe'
driver = webdriver.Chrome(path)

# targetUsers = ['Akshay Avcoe', 'Nitin Avcoe', 'Suraj Avcoe', 'Rushi Avcoe',]
targetUsers = ['Akshay Avcoe']

driver.get("https://web.whatsapp.com/")
time.sleep(10)

for users in targetUsers:

    arrow = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/button/div[2]/span")
    arrow.click()
    searchbar = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]")
    searchbar.send_keys(f'{users}', Keys.ENTER)
    sendMessage = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]")
    sendMessage.send_keys('Messages Sent by Bot', Keys.ENTER)
    time.sleep(3)
