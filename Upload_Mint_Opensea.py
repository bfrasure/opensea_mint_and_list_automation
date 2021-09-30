import os
from os import name
import subprocess
import tkinter
from tkinter import filedialog
from selenium import webdriver
import time
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ExpectedConditions

##tkinter
root = tkinter.Tk()
root.title("opensea uplode automation")


def open_chrome_profile():
    subprocess.Popen(
        [
            "start",
            "chrome",
            "--remote-debugging-port=8989",
            "--user-data-dir=" + repo_save_path + "/chrome_profile",
        ],
        shell=True,
    )


# tests
def main_program_loop():  # DEBUG ONLY
    print("{0} {1}".format("img folder:", img_folder_path))
    print("{0} {1}".format("repo_save_path:", repo_save_path.name))
    print("{0} {1}".format("Collection link:", collection_link_input.get()))
    print("{0} {1}".format("start num:", int(start_num_input.get())))
    print("{0} {1}".format("uplode amount:", int(uplode_amount.get())))
    print("{0} {1}".format("price:", float(price.get())))
    print("{0} {1}".format("title:", title.get()))
    print("{0} {1}".format("file format:", file_format.get()))

    ###START###
    print("Welcome!!!!")
    print("Please choose your project folder(make sure the chrome driver is in it)")
    project_path = repo_save_path.name
    file_path = img_folder_path
    collection_link = collection_link_input.get()
    start_num = int(start_num_input.get())
    up_amount = int(uplode_amount.get())
    price_ALI = float(price.get())
    title_ALI = title.get()
    file_format_ALI = file_format.get()

    ##chromeoptions
    opt = Options()
    opt.add_experimental_option("debuggerAddress", "localhost:8989")
    driver = webdriver.Chrome(
        executable_path=project_path + "/chromedriver.exe",
        chrome_options=opt,
    )
    wait = WebDriverWait(driver, 60)

    ###wait for methods
    def wait_for(code):
        wait.until(
            ExpectedConditions.presence_of_element_located((By.CSS_SELECTOR, code))
        )

    def wait_xpath(code):
        wait.until(ExpectedConditions.presence_of_element_located((By.XPATH, code)))

    while up_amount != 0:
        print(str(start_num) + " and this many left > " + str(up_amount))
        url = collection_link
        driver.get(url)
        # time.sleep(3)

        wait_for(
            ".styles__StyledLink-sc-l6elh8-0.cnTbOd.Blockreact__Block-sc-1xf18x6-0.Buttonreact__StyledButton-sc-glfma3-0.bhqEJb.gMiESj"
        )
        additem = driver.find_element_by_css_selector(
            ".styles__StyledLink-sc-l6elh8-0.cnTbOd.Blockreact__Block-sc-1xf18x6-0.Buttonreact__StyledButton-sc-glfma3-0.bhqEJb.gMiESj"
        )
        additem.click()
        time.sleep(1)

        wait_xpath('//*[@id="media"]')
        imageUpload = driver.find_element_by_xpath('//*[@id="media"]')
        imagePath = os.path.abspath(
            file_path + "\\" + str(start_num) + "." + file_format_ALI
        )  # change folder here
        imageUpload.send_keys(imagePath)

        name = driver.find_element_by_xpath('//*[@id="name"]')
        name.send_keys(
            title_ALI + str(start_num)
        )  # +1000 for other folders #change name before "#"
        time.sleep(0.5)

        create = driver.find_element_by_css_selector(
            ".Blockreact__Block-sc-1xf18x6-0.Buttonreact__StyledButton-sc-glfma3-0.bhqEJb.gMiESj"
        )
        create.click()
        time.sleep(1)

        wait_for(
            ".Iconreact__Icon-sc-1gugx8q-0.Modalreact__StyledIcon-sc-xyql9f-1.irnoQt.byuytI.material-icons"
        )
        cross = driver.find_element_by_css_selector(
            ".Iconreact__Icon-sc-1gugx8q-0.Modalreact__StyledIcon-sc-xyql9f-1.irnoQt.byuytI.material-icons"
        )
        cross.click()
        time.sleep(1)

        main_page = driver.current_window_handle

        wait_for(
            "a[class='styles__StyledLink-sc-l6elh8-0 cnTbOd Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 jxgnwF gMiESj OrderManager--second-button']"
        )
        sell = driver.find_element_by_css_selector(
            "a[class='styles__StyledLink-sc-l6elh8-0 cnTbOd Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 jxgnwF gMiESj OrderManager--second-button']"
        )
        sell.click()
        # time.sleep(1)

        wait_for("input[placeholder='Amount']")
        amount = driver.find_element_by_css_selector("input[placeholder='Amount']")
        # amount.click()
        amount.send_keys(str(price_ALI))
        # time.sleep(1)

        wait_for(
            "button[class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 bhqEJb gMiESj']"
        )
        listing = driver.find_element_by_css_selector(
            "button[class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 bhqEJb gMiESj']"
        )
        listing.click()
        # time.sleep(1)

        # time.sleep(5)
        wait_for(
            "button[class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 bhqEJb gMiESj']"
        )
        sign = driver.find_element_by_css_selector(
            "button[class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 bhqEJb gMiESj']"
        )
        sign.click()
        time.sleep(2)
        ###login backup location
        # changing the handles to access login page
        for handle in driver.window_handles:
            if handle != main_page:
                login_page = handle
        # change the control to signin page
        driver.switch_to.window(login_page)
        # time.sleep(5)
        wait_xpath('//*[@id="app-content"]/div/div[3]/div/div[3]/button[2]')
        sign = driver.find_element_by_xpath(
            '//*[@id="app-content"]/div/div[3]/div/div[3]/button[2]'
        )
        sign.click()
        time.sleep(1)
        # change control to main page
        driver.switch_to.window(main_page)
        time.sleep(1)

        start_num = start_num + 1
        up_amount = up_amount - 1


# comande for gui inputs
def img_folder_input():
    global img_folder_path
    img_folder_path = filedialog.askdirectory()
    Name_change_img_folder_button(img_folder_path)


def repo_save_loc_input():
    global repo_save_path
    repo_save_path = filedialog.askdirectory()
    Name_change_chromdriver_button(repo_save_path)


# chang gui test
def Name_change_img_folder_button(img_folder_input):
    img_folder_input_button["text"] = img_folder_input


def Name_change_chromdriver_button(repo_save_path):
    repo_save_loc_button["text"] = repo_save_path


# main gui inputs
button_widget = tkinter.Button(root, text="Start!", command=main_program_loop)
open_browser = tkinter.Button(root, text="Open Browser", command=open_chrome_profile)

img_folder_input_button = tkinter.Button(
    root, height=3, width=60, text="Add img folder", command=img_folder_input
)

repo_save_loc_button = tkinter.Button(
    root, height=3, width=60, text="Repo save location:", command=repo_save_loc_input
)

collection_link_label = tkinter.Label(root, text="Collection_link:")
collection_link_input = tkinter.Entry(root)
collection_link_input.insert(0, "")

start_num_input_label = tkinter.Label(root, text="Start num:")
start_num_input = tkinter.Entry(root)
start_num_input.insert(0, "")

uplode_amount_label = tkinter.Label(root, text="Uplode amount:")
uplode_amount = tkinter.Entry(root)
uplode_amount.insert(0, "")

price_label = tkinter.Label(root, text="Set price:")
price = tkinter.Entry(root)
price.insert(0, "")

title_label = tkinter.Label(root, text="Title:")
title = tkinter.Entry(root)
title.insert(0, "")

file_format_label = tkinter.Label(root, text="File format:")
file_format = tkinter.Entry(root)
file_format.insert(0, "")


# Gui fichas posisons
img_folder_input_button.grid(row=0, columnspan=2)

repo_save_loc_button.grid(row=1, columnspan=2)

collection_link_label.grid(row=2, column=0)
collection_link_input.grid(row=2, column=1)

start_num_input_label.grid(row=3, column=0)
start_num_input.grid(row=3, column=1)

uplode_amount_label.grid(row=4, column=0)
uplode_amount.grid(row=4, column=1)

price_label.grid(row=5, column=0)
price.grid(row=5, column=1)

title_label.grid(row=6, column=0)
title.grid(row=6, column=1)

file_format_label.grid(row=7, column=0)
file_format.grid(row=7, column=1)

button_widget.grid(row=100, column=0)
open_browser.grid(row=2, column=2)


# End of script
root.mainloop()
