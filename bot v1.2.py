from selenium import webdriver
from time import sleep
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path=r'C:\Users\ekpro\PycharmProjects\Tik Tok Bot\chromedriver.exe',options=chrome_options)

vidUrl = "https://vm.tiktok.com/ZMR2TNcHF"

def setup():
    global tabs
    tabs = 11
    driver.get("https://tokkz.com")
    for i in range(tabs-1):
        driver.execute_script("window.open('https://tokkz.com');")

# Tab order: 0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

def views():
    try:
        for i in range(tabs):
            driver.switch_to.window(driver.window_handles[i])
            sleep(1)
            driver.find_element_by_id("tiktok_url").click()
            sleep(1)
            driver.find_element_by_id("tiktok_url").send_keys(vidUrl)
            sleep(1)
            driver.find_element_by_xpath("/html/body/div[1]/main/div/article/div/div[1]/div/div/div[2]/div/div/div[1]/div[3]/input[2]").click()
            sleep(2)
            driver.execute_script("window.scrollBy(0, 500)", "")
            sleep(5)
            driver.find_element_by_xpath("/html/body/div[1]/main/div/article/div/div[1]/div/div/div[2]/div/div/div[1]/div[3]/div[1]/div/p").click()
            sleep(2)
            print("Tab",i,"was successful!")
            if i == 10:
                for handle in driver.window_handles:
                    driver.switch_to.window(handle)
                    driver.close()
    except:
        print("AN ERROR OCCURED. THIS WAS MOST LIKELY DUE TO CONNECTION ISSUES. TERMINATING PROGRAM...")
        sleep(2)
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            driver.close()
        setup()
        print("SUCCESSFULLY REFRESHED")
        views()

if __name__ == "__main__":
    setup()
    sleep(5)
    views()
