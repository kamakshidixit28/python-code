from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
username = input("please enter your username")
password = input("plese enter your password")
url = "https://www.facebook.com/"
driver = webdriver.Chrome(r"C:\Users\Lalit Kumar Dixit\Downloads\chromedriver_win32\chromedriver.exe")

driver.get(url)

driver.find_element_by_id("email").send_keys(username)
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_name("login").click()
print("Logged Successfully")
print("plese click allow or block")
sleep(20)
actions = ActionChains(driver)
actions.send_keys('p')
actions.perform()
print("post box opened")
sleep(3)
actions = ActionChains(driver)
actions.send_keys("@#python#@")
actions.send_keys(Keys.TAB * 10)
actions.send_keys(Keys.ENTER)
actions.perform()
print("posted")
print("program ended")