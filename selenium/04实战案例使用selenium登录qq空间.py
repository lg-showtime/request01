from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path='./chromedriver')
bro.get('https://qzone.qq.com/')

bro.switch_to.frame('login_frame')
a_link = bro.find_element_by_id('switcher_plogin')
a_link.click()
sleep(1)
username = bro.find_element_by_id('u')
password = bro.find_element_by_id('p')
sleep(1)
username.send_keys('1396877852')
sleep(1)
password.send_keys('123456')
sleep(1)
login_btn = bro.find_element_by_id('login_button')
login_btn.click()
sleep(5)

bro.quit()