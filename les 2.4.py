from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 15).until(	
            EC.text_to_be_present_in_element((By.ID,"price"), '$100') 
        )
but = browser.find_element_by_id('book')

but.click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
print(y)  

op = browser.find_element_by_id('answer')
op.send_keys(y)
button = browser.find_element_by_id("solve")
button.click()
