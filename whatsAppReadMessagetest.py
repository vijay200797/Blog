from selenium import webdriver
from time import sleep



def ReadWhatsAppMessage(driver):
    # get element through text
    # find_today_element = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[2]/div[2]/div[1]/div/span')
    print("Findinding Element")
    # find_today_element = driver.find_element("xpath", '//*[@id="main"]/div[2]/div/div[2]/div[2]/div[1]/div/span')
    #find_today_element = driver.find_element("xpath", "//span[text()='TODAY']")

    find_today_elements = driver.find_elements("xpath", "//span[text()='TODAY']/following::div[@class='_21Ahp']")
    
    print(len(find_today_elements))
    print("Element Found")
    # print(find_today_element.innerHTML)
    for find_today_element in find_today_elements:
        print(find_today_element.text)
        print(find_today_element.tag_name)
        print(find_today_element.parent)
        print(find_today_element.location)
        print(find_today_element.size)
        print("-------------------------------------")

    driver.execute_script("return alert('Script Executed');")
    # sleep for some time
    sleep(1500)

def initiateDriver():
    # create webdriver object
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\YV165NL\\Downloads\\chromedriver_win32\\chromedriver.exe")
    
    # get the website
    driver.get("https://web.whatsapp.com/")
    
    # sleep for some time
    sleep(60)

    a = int(input("Enter 1 to continuee if whatsApp Ready else 0 Exit "))
    sleep(30)

    if a==1 :
        ReadWhatsAppMessage(driver)
    else:
        driver.close()
        exit()

