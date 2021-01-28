# code copied from edureka  -  https://www.edureka.co/community/64462/how-automatically-download-with-selenium-webdriver-python

value1 = 8419

from selenium import webdriver

download_dir = "C:\\Temp\\Dowmload"  # for linux/*nix, download_dir="/usr/Public"
options = webdriver.ChromeOptions()

profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], # Disable Chrome's PDF Viewer
               "download.default_directory": download_dir , "download.extensions_to_open": "applications/pdf"}
options.add_experimental_option("prefs", profile)
driver = webdriver.Chrome('C:\Program Files\webdriver\chromedriver.exe', chrome_options=options)  # Optional argument, if not specified will search path.

driver.get(f'http://www.apsranikhet.in/blob/uploads/annualResult201920/{value1}.pdf')

