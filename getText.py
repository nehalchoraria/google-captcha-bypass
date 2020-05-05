
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

delayTime = 10

option = webdriver.ChromeOptions()
option.add_argument('--disable-notifications')
option.add_argument("--mute-audio")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
driver.get('https://speech-to-text-demo.ng.bluemix.net/')

# driver.execute_script('''window.open("","_blank");''')
# driver.switch_to.window(driver.window_handles[1])

driver.get('https://speech-to-text-demo.ng.bluemix.net/')


# Upload file 
time.sleep(1)
root = driver.find_element_by_id('root').find_elements_by_class_name('dropzone _container _container_large')
btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/input')
btn.send_keys('/home/synoriq/Desktop/fiverr/1.wav')
# Audio to text is processing
time.sleep(delayTime)

text = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[6]/div/div/dialog').find_elements_by_tag_name('dd')
result = " ".join( [ each.text for each in text ] )