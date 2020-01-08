from selenium import webdriver
import time
import traceback
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser = webdriver.Chrome()
	browser.get(link)
	
	book_btn = browser.find_element(By.ID, "book")
	browser.execute_script("return arguments[0].scrollIntoView(true);", book_btn)
	
	button = WebDriverWait(browser, 15).until(
		EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
	)
	
	#book_btn = browser.find_element(By.ID, "book")
	book_btn.click()

	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = str(math.log(abs(12*math.sin(int(x)))))
	
	answer = browser.find_element_by_id("answer")
	answer.send_keys(y)
	
	submit = browser.find_element_by_css_selector("button[type='submit']")
	submit.click()

except Exception as error:
	print('Ошибка при выполнении теста:\n', traceback.format_exc())
	
finally:
	time.sleep(5)
	browser.quit()
