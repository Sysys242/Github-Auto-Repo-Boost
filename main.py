from selenium import webdriver
import time
from selenium.webdriver.common.by import By

username = "" # github name
password = '' # github pass

repos = [
	#link to the edit liscence page
	#It's array so u can add more than 1 repos ;)
	'https://github.com/ExempleUser/ExempleProject/edit/main/LICENSE',
	]

def autoUpdate(driver):
	while True:
		for url in repos:
			driver.get(url)
			time.sleep(3)
			driver.find_element(By.XPATH, '//*[@id="code-editor"]/div[22]/pre/span').send_keys(" ")
			time.sleep(2)
			driver.find_element(By.XPATH, '//*[@id="submit-file"]').click()
			time.sleep(5)
		time.sleep(120)


if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path='driver.exe', chrome_options=chrome_options)
    driver.get("https://github.com/session")
    time.sleep(2)
    usernames = driver.find_element(By.XPATH, "//*[@id=\"login_field\"]")
    passwords = driver.find_element(By.XPATH, "//*[@id=\"password\"]")
    time.sleep(2)
    usernames.send_keys(username)
    time.sleep(1)
    passwords.send_keys(password)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[11]').click()
    time.sleep(3)
    autoUpdate(driver)