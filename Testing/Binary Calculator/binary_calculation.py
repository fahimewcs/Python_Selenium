import os
from selenium import webdriver


os.environ['PATH'] += r"C:\SeleniumDrivers"
driver = webdriver.Chrome()
driver.get("http://www.calculator.net/binary-calculator.html")


driver.implicitly_wait(10)


number1 = driver.find_element_by_id('number1')
number1.clear()
number2 = driver.find_element_by_id('number2')
number2.clear()

number1.send_keys(10010)
number2.send_keys(10101)


calculate = driver.find_element_by_css_selector('input[value="Calculate"]')
calculate.click()

clear = driver.find_element_by_css_selector('img[onclick="clearForm(document.calform);"]')
clear.click()





