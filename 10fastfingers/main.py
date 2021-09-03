from selenium import webdriver
import time
PATH = 'C:\\Program Files (x86)\\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://10fastfingers.com/typing-test/english')
time.sleep(5)
driver.set_window_size(1024, 600)
driver.maximize_window()

for i in range(1,301):
    var1 = driver.find_element_by_xpath('//*[@id="row1"]/span[' + str(i) + ']').text
    input_text = driver.find_element_by_id("inputfield")
    input_text.send_keys(var1 + " ")

