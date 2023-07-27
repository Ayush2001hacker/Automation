import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

timeout = 1


def open_website():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path="C:\\Users\\yagraw\\Downloads\\chromedriver.exe")

    driver.get("http://localhost:3000/")

    return driver


# Function to log in
def login(driver, username, password):
    username_field = driver.find_element(By.ID, "outlined-basic")
    username_field.send_keys(username)
    time.sleep(timeout)
    password_field = driver.find_element(By.XPATH, "(//input[@id='outlined-basic'])[2]")
    password_field.send_keys(password)
    time.sleep(timeout)
    login_button = driver.find_element(By.ID, "login")
    login_button.click()
    time.sleep(timeout)

def search(driver,name):
    search_input=driver.find_element(By.ID,":r5:")
    search_input.send_keys(name)
    time.sleep(timeout)



def store_records(driver):
    records_name=[]
    all_records=[]
    last_ele=""
    while(True):
        
        records=driver.find_elements(By.XPATH,"//div[@data-colindex='0']")
        if len(records)==0:
            break
    
        for i in records:
            all_records.append(i)
            records_name.append(i.text)

        first_ele=records_name[-1]
        if first_ele==last_ele:
            break
        last_ele=records_name[-1]
        driver.execute_script("arguments[0].scrollIntoView();", records[-1])
        time.sleep(2)
    
    records_name=set(records_name)
    
    print(records_name)
    print(len(records_name))
    return records_name

def validate_record(name):
    records_name=store_records(driver)
    

    for x in records_name:
        
        if name in x.lower():
            print(f'{name} is present in {x}')
        else:
            raise Exception(f'{name} is not present in {x}')
        
def validate_sorted_records():

    records_name=store_records(driver)
        
    sorted_record_name=sorted(records_name)
    #store_records(driver)
    print(sorted_record_name)

def sort_ascending(driver):
    sort_list = []
    store_records(driver)
    sort_button = driver.find_element(By.XPATH, '//div/div[text()="Name"]/../../div/button[@title="Sort" and @type="button"]')
    ActionChains(driver).move_to_element(sort_button).click(sort_button).perform()
    action = ActionChains(driver)

    while True:
        for_parent_of_last = driver.find_elements(By.XPATH, "//div[@data-rowindex = '19']")
        res = driver.find_elements(By.XPATH, '//div[@class="MuiDataGrid-row"]/div[@data-field="name"]/div[text()]')
        for i in res:
            if i.text not in sort_list:
                sort_list.append(i.text)
        action.scroll_to_element(res[-1]).perform()
        if for_parent_of_last:
            res = driver.find_element(By.XPATH, '//div[@data-rowindex = "19"]/div[@data-field="name"]/div[text()]')
            sort_list.append(res.text)
            break
        time.sleep(timeout)
    error_raised = False
    for i in range(len(sort_list)-1):
        if sort_list[i] > sort_list[i+1]:
            error_raised = True
    if not error_raised:
        print("Ascending Sort Validated!")
    else:
        print("Error: Ascending Sort Failed!")
    # print(f"sorted-list = {sort_list}")
    time.sleep(timeout)

def sort_descending(driver):
    sort_list = []
    store_records(driver)
    sort_button = driver.find_element(By.XPATH, '//div/div[text()="Name"]/../../div/button[@title="Sort" and @type="button"]')
    ActionChains(driver).move_to_element(sort_button).click(sort_button).perform()
    action = ActionChains(driver)

    while True:
        for_parent_of_last = driver.find_elements(By.XPATH, "//div[@data-rowindex = '19']")
        res = driver.find_elements(By.XPATH, '//div[@class="MuiDataGrid-row"]/div[@data-field="name"]/div[text()]')
        for i in res:
            if i.text not in sort_list:
                sort_list.append(i.text)
        action.scroll_to_element(res[-1]).perform()
        if for_parent_of_last:
            res = driver.find_element(By.XPATH, '//div[@data-rowindex = "19"]/div[@data-field="name"]/div[text()]')
            sort_list.append(res.text)
            break
        time.sleep(timeout)
    error_raised = False
    for i in range(len(sort_list)-1):
        if sort_list[i] < sort_list[i+1]:
            error_raised = True
    if not error_raised:
        print("Descending Sort Validated!")
    else:
        print("Error: Descending Sort Failed!")
    # print(f"sorted-list = {sort_list}")
    time.sleep(timeout)
            


if __name__ == "__main__":
    username = "test@dax.com"
    password = "12345"
    driver = open_website()

    time.sleep(timeout)

    print("website open")
    login(driver, username, password)
    
    print("user is logged in application")

    search(driver,"rick")
    
    validate_record("rick")

    sort_ascending(driver)

    sort_descending(driver)
    
    driver.quit()

