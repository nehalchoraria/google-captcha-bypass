
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time
from bs4 import BeautifulSoup

delayTime = 3
audioToTextDelay = 10

option = webdriver.ChromeOptions()
option.add_argument('--disable-notifications')
option.add_argument("--mute-audio")
option.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.14 Safari/537.36")

# option.add_experimental_option("debuggerAddress", "127.0.0.1:9567")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)


def audioToText(mp3Path):
    delayTime = 10

    driver.execute_script('''window.open("","_blank");''')
    driver.switch_to.window(driver.window_handles[1])

    driver.get('https://speech-to-text-demo.ng.bluemix.net/')

    # Upload file 
    time.sleep(1)
    root = driver.find_element_by_id('root').find_elements_by_class_name('dropzone _container _container_large')
    btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/input')
    btn.send_keys(mp3Path)

    # Audio to text is processing
    time.sleep(audioToTextDelay)

    text = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[6]/div/div/dialog').find_elements_by_tag_name('dd')
    result = " ".join( [ each.text for each in text ] )

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    return result


driver.get('https://www.google.com/recaptcha/api2/demo')

googleClass = driver.find_elements_by_class_name('g-recaptcha')[0]
outeriframe = googleClass.find_element_by_tag_name('iframe')
outeriframe.click()

allIframesLen = driver.find_elements_by_tag_name('iframe')
audioBtnFound = False
for index in range(len(allIframesLen)):
    driver.switch_to_default_content()
    iframe = driver.find_elements_by_tag_name('iframe')[index]
    driver.switch_to.frame(iframe)
    driver.implicitly_wait(delayTime)
    try:
        audioBtn = driver.find_element_by_id('recaptcha-audio-button') 
        audioBtn.click()
        audioBtnFound = True
        break
    except Exception as e:
        pass

if audioBtnFound:
    pass


response = audioToText('/home/synoriq/Desktop/fiverr/1.wav')
# driver.switch_to.default_content()

# html = driver.page_source
# soup = BeautifulSoup(html,"html.parser")

# iframe = soup.find('div',{'class':'g-'}).find('iframe')
# time.sleep(3)
# print(element)
