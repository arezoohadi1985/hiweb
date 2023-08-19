from selenium import  webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver =webdriver.Chrome(executable_path="C:/Users/a.hadi/Documents/web driver/ChromeDriver_Hiweb/chromedriver.exe")
driver.get("http://google.com")
sleep(2)
driver.find_element('id',"APjFqb").send_keys("wikipedia")
sleep(3)