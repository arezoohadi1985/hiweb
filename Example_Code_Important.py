from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.options import option
from time import sleep

# TODO : OK Driver
# driver = webdriver.Chrome(executable_path='C:/Users/m.eftekhari/Desktop/Test/ChromeDriver_Hiwebchromedriver.exe')
# options = webdriver.ChromeOptions()
# actions = ActionsChains(driver)
# driver.get("https://www.google.com")
# sleep(10)

# TODO : OK Driver
# service = Service(executable_path= 'C:/Users/m.eftekhari/Desktop/Test/ChromeDriver_Hiwebchromedriver.exe')
# driver = webdriver.Chrome(service = service, option = option)
# actions = ActionsChains(driver)
# driver.maximize_window()
# driver.get("https://www.google.com")
# sleep(10)

# TODO : OK Driver
# service = Service(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
# actions = ActionChains(driver)
# driver.maximize_window()
# driver.get("https://www.imdb.com/chart/top/")

# TODO : OK Driver
# driver = webdriver.Chrome(executable_path='C:/Users/m.eftekhari/Desktop/Test/ChromeDriver_Hiwebchromedriver.exe')
# actions = ActionChains(driver)
# driver.maximize_window()
# # driver.get("https://testportal1.hiweb.ir/main.aspx#208406288")
# driver.get("https://www.imdb.com/chart/top/")

# TODO : Scroll
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# sleep(10)

# TODO : Click
# BtnCreateNew = driver.find_element(By.XPATH, '//li[position()=2 and @id="account|NoRelationship|HomePageGrid|Mscrm.HomepageGrid.account.NewRecord"]/span/a')
# driver.execute_script("arguments[0].click();", BtnCreateNew)

# TODO : Login CRM User-Pass-Address
# driver.get("http://administrator:M@hammadEF8936@192.168.8.128")