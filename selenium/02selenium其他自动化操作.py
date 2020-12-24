from selenium import webdriver
import time

bro = webdriver.Chrome(executable_path='./chromedriver')
bro.get('https://www.taobao.com/')
# 标签定位
search_input = bro.find_element_by_id('q')
#标签的交互
search_input.send_keys('iphone')

# 执行一组js程序
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(2)

# 点击搜索按钮
btn = bro.find_element_by_css_selector('.btn-search')
btn.click()

bro.get('https://www.baidu.com/')
time.sleep(2)
# 回退
bro.back()
time.sleep(2)
# 前进
bro.forward()
time.sleep(5)
bro.quit()