
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# driver = webdriver.chrome()
driver = webdriver.Chrome(executable_path='C:\Program Files\webdriver\chromedriver.exe')

driver.get("chrome://settings/content/pdfDocuments") 

value1 = 8419
 

time.sleep(5)
driver.get("chrome://settings/?search=location+") 
time.sleep(25)


for i in range(5000,8500):
    try:
        driver.get(f'http://www.apsranikhet.in/blob/uploads/annualResult201920/{i}.pdf')
        print(i)
    except:
        pass

# driver.get(f'http://www.apsranikhet.in/blob/uploads/annualResult201920/{value1}.pdf')
