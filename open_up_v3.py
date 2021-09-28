import itertools
import os
import tkinter as tk
from tkinter import filedialog

import pandas
from selenium import webdriver
import time
import selenium

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support import expected_conditions as ExpectedConditions


##tkinter
root = tk.Tk()
root.withdraw()

##chromeoptions
opt=Options()
opt.add_experimental_option("debuggerAddress","localhost:8989")
driver=webdriver.Chrome(executable_path="K:\\2021 Backups\\Coding\\Python projects\\chromedriver.exe", chrome_options=opt)
wait = WebDriverWait(driver, 60)  


###wait for methods
def wait_for(code):
    wait.until(ExpectedConditions.presence_of_element_located(
        (By.CSS_SELECTOR, code)))

def wait_xpath(code):
    wait.until(ExpectedConditions.presence_of_element_located(
        (By.XPATH, code)))



###START###
print("Welcome!!!!")
file_path = filedialog.askdirectory()
collection_link = input('collection link: ')
start_num = int(input('Start number: '))
up_amount = int(input('How many would you liek to upload: '))
price = input('Price: ')
title = input('Title: ')
file_format = input('File foramt: ')

while up_amount != 0:
    print(str(start_num) + " and this many left > " + str(up_amount))
    url = collection_link
    driver.get(url)
    #time.sleep(3)

    
    wait_for('.styles__StyledLink-sc-l6elh8-0.cnTbOd.Blockreact__Block-sc-1xf18x6-0.Buttonreact__StyledButton-sc-glfma3-0.bhqEJb.gMiESj')
    additem = driver.find_element_by_css_selector('.styles__StyledLink-sc-l6elh8-0.cnTbOd.Blockreact__Block-sc-1xf18x6-0.Buttonreact__StyledButton-sc-glfma3-0.bhqEJb.gMiESj')
    additem.click()
    time.sleep(1)

    
    wait_xpath('//*[@id="media"]')
    imageUpload = driver.find_element_by_xpath('//*[@id="media"]')
    imagePath = os.path.abspath(file_path + "\\" + str(start_num) + "." + file_format) #change folder here
    imageUpload.send_keys(imagePath)


    name = driver.find_element_by_xpath('//*[@id="name"]')
    name.send_keys(title + str(start_num)) #+1000 for other folders #change name before "#" 
    time.sleep(0.5)

    create = driver.find_element_by_css_selector('.Blockreact__Block-sc-1xf18x6-0.Buttonreact__StyledButton-sc-glfma3-0.bhqEJb.gMiESj')
    create.click()
    time.sleep(1)

    
    
    wait_for('.Iconreact__Icon-sc-1gugx8q-0.Modalreact__StyledIcon-sc-xyql9f-1.irnoQt.byuytI.material-icons')
    cross = driver.find_element_by_css_selector('.Iconreact__Icon-sc-1gugx8q-0.Modalreact__StyledIcon-sc-xyql9f-1.irnoQt.byuytI.material-icons')
    cross.click()
    time.sleep(1)

    main_page = driver.current_window_handle

    wait_for("a[class='styles__StyledLink-sc-l6elh8-0 cnTbOd Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 jxgnwF gMiESj OrderManager--second-button']")
    sell = driver.find_element_by_css_selector("a[class='styles__StyledLink-sc-l6elh8-0 cnTbOd Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 jxgnwF gMiESj OrderManager--second-button']")
    sell.click()
    #time.sleep(1)

    wait_for("input[placeholder='Amount']")
    amount = driver.find_element_by_css_selector("input[placeholder='Amount']")
    #amount.click()
    amount.send_keys(price)
    #time.sleep(1)

    wait_for("button[class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 bhqEJb gMiESj']")
    listing = driver.find_element_by_css_selector("button[class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 bhqEJb gMiESj']")
    listing.click()
    #time.sleep(1)


    #time.sleep(5) 
    wait_for("button[class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 bhqEJb gMiESj']")
    sign = driver.find_element_by_css_selector("button[class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 bhqEJb gMiESj']")
    sign.click()
    time.sleep(2)
    ###login backup location
    # changing the handles to access login page
    for handle in driver.window_handles:
        if handle != main_page:
            login_page = handle
    # change the control to signin page       
    driver.switch_to.window(login_page)
    #time.sleep(5)
    wait_xpath('//*[@id="app-content"]/div/div[3]/div/div[3]/button[2]')
    sign = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[3]/button[2]')
    sign.click()
    time.sleep(1)  
    # change control to main page
    driver.switch_to.window(main_page)
    time.sleep(1)

    start_num = start_num + 1
    up_amount = up_amount - 1

print("Finished!!!!")