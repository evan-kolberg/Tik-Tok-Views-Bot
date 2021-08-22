from selenium import webdriver
from time import sleep
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path=r'C:\Users\-------\PycharmProjects\Tik Tok Bot\chromedriver.exe',options=chrome_options) #Change it

vidUrl = "https://vm.tiktok.com/ZMR2R9kUH"

def setup():
    global tabs
    #tabs = int(input("How many tabs would you like? 11 is recommended to bypass daily limit."))
    tabs = 11
    for i in range(tabs):
        driver.execute_script("window.open('https://tokkz.com');")
    driver.switch_to.window(driver.window_handles[tabs])

def views():
    try:
        for i in range(tabs):
            driver.find_element_by_id("tiktok_url").click()
            sleep(1)
            driver.find_element_by_id("tiktok_url").send_keys("https://vm.tiktok.com/ZMR2R9kUH")
            sleep(1)
            driver.find_element_by_xpath("/html/body/div[1]/main/div/article/div/div[1]/div/div/div[2]/div/div/div[1]/div[3]/input[2]").click()
            sleep(2)
            driver.execute_script("window.scrollBy(0, 500)", "")
            sleep(5)
            driver.find_element_by_xpath("/html/body/div[1]/main/div/article/div/div[1]/div/div/div[2]/div/div/div[1]/div[3]/div[1]/div/p").click()
            sleep(2)
            driver.switch_to.window(driver.window_handles[tabs - i - 1])
            if tabs - i - 1 == 0:
                driver.close()
            sleep(2)
    except:
        print("AN ERROR OCCURED. THIS WAS MOST LIKELY DUE TO CONNECTING ISSUES. PLEASE RESTART ME.")
        driver.close()

if __name__ == "__main__":
    setup()
    sleep(5)
    views()
