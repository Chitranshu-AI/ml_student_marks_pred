# importing libraries and modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import numpy as np

driver = webdriver.Chrome(executable_path='C:\Program Files\webdriver\chromedriver.exe')


driver.get("chrome://settings/?search=location+") 
time.sleep(15)


# login to pdf2go
def login_pdf2go():
    driver.get('https://www.pdf2go.com/login') 
    driver.find_element_by_xpath('//*[@id="username"]').send_keys('chitranshuharbola2@gmail.com')
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('12345678')
    driver.find_element_by_xpath('//*[@id="functional-submit-btn"]').click()  
    time.sleep(5)
login_pdf2go()



# fill adm_no with admission number
adm_no = []
def append_adm_no():
    path="F:/programming projects/web scrapper/pdf/"
    # iterating every pdf file in pdf folder and adding it to list
    for filename in os.listdir(path):
        adm_no.append(filename)
        # print(filename)
append_adm_no()


def reshape_list(list_to_split,num,sub_num):
    # convert list to numpy array
    arr = np.array(list_to_split)
    # size of list
    size = arr.size
    # gives second value to reshape 
    mult = num * sub_num
    division = int(size/mult)
    # reshaping - 10:87 
    reshaped_list = arr.reshape((division,num,sub_num))
    return reshaped_list
pdf_string = reshape_list(adm_no,20,5)


# pdf2go_page = driver.get(f'https://www.pdf2go.com/pdf-to-text')

path_txt_file = "F:/programming projects/web scrapper/text_automated_files/"


errored_pdfs = []
tens = 10
for first_block in pdf_string[7:]:
    num = 1
    for first_line in first_block:
        try:
            # open and switch to new tab
            driver.execute_script("window.open('https://www.pdf2go.com/pdf-to-text');")
        except Exception as e:
            print('error in opening new tab')
        try:
            driver.switch_to.window(driver.window_handles[num])
            # click url button
            driver.find_element_by_xpath('//*[@id="externalUrlButton"]').click()
        except:
            print('error in switching or finding url button')

        
        for i in first_line:
            # url for input field
            url = f'http://www.apsranikhet.in/blob/uploads/annualResult201920/{i}'
            print(url)
            try:
                # type link in input feild
                inputElement = driver.find_element_by_xpath('//*[@id="remoteUrlInput"]')
                inputElement.send_keys(url)
                # click on add button
                add_button = driver.find_element_by_xpath('//*[@id="addRemoteUrlButton"]')
                add_button.click()
            except:
                errored_pdfs.append(i)
                print('error in first line for loop')
        time.sleep(5)
        # click on start button
        start_button =  driver.find_element_by_xpath('//*[@id="page_function_container"]/div[1]/button/strong')
        start_button.click()

        

        num = num+1

    # wait until all file downlaods    
    time.sleep(20)
    try:
        num_down = 1
        for i in range(25):
            driver.switch_to.window(driver.window_handles[num_down])
            try:
                download_1 = driver.find_element_by_xpath('//*[@id="page_function_container"]/div/div[1]/div/div[1]/div[6]/div[2]/div/div/div[2]/div[3]/a')
                download_1.click()
                download_2 = driver.find_element_by_xpath('//*[@id="page_function_container"]/div/div[1]/div/div[1]/div[6]/div[2]/div/div/div[3]/div[3]/a')
                download_2.click()
                download_3 = driver.find_element_by_xpath('//*[@id="page_function_container"]/div/div[1]/div/div[1]/div[6]/div[2]/div/div/div[4]/div[3]/a')
                download_3.click()
                download_4 = driver.find_element_by_xpath('//*[@id="page_function_container"]/div/div[1]/div/div[1]/div[6]/div[2]/div/div/div[5]/div[3]/a')
                download_4.click()
                download_5 = driver.find_element_by_xpath('//*[@id="page_function_container"]/div/div[1]/div/div[1]/div[6]/div[2]/div/div/div[6]/div[3]/a')
                download_5.click()
            except Exception as e:
                print(e)
                print('error in xpath finding')
            num_down = num_down + 1
    except Exception as e:
        print(e)
        print('error in closing tab')
    time.sleep(2)        
    
    try:
        for i in range(25):
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
    except:
        print('error in closing')

    print('first loop success.... NOW ANOTHER LOOP OF 10')
    print('here you gooo.....')
    tens = tens + 10
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    

# # driver.get(f'http://www.apsranikhet.in/blob/uploads/annualResult201920/{value1}.pdf')







