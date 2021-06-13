from fb_xpath import *
import xlsxwriter
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pathlib
import time



all_react_out = "//span[@class='pcp91wgn']"


chrome_options = Options()
scriptDirectory = pathlib.Path().absolute()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument('--profile-directory=Default')
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('disable-infobars')
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("user-data-dir=chrome-data")
chrome_options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
driver = webdriver.Chrome("./chromedriver.exe", chrome_options=chrome_options)


driver.get("https://mbasic.facebook.com/groups/bdblock")
driver.implicitly_wait(5)





def go_post():


    a = 1
    while a < 3:
        if driver.find_elements_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/section[1]/article["+str(a)+"]/footer[1]/div[2]/span[1]/a[1]"):
            driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/section[1]/article["+ str(a)+"]/footer[1]/div[2]/span[1]/a[1]").click()
            driver.implicitly_wait(5)

            if driver.find_elements_by_xpath(
                    "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/a[1]/div[1]"):
                driver.find_element_by_xpath(
                    "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/a[1]/div[1]").click()

                i = 1
                while i < 4:



                    likers = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/ul[1]/li["+str(i)+"]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[3]/header[1]/h3[1]/a[1]")
                    ActionChains(driver).key_down(Keys.CONTROL).click(likers).key_up(Keys.CONTROL).perform()
                    driver.switch_to.window(driver.window_handles[1])
                    curl = driver.current_url
                    get_about = curl.replace("mbasic","www")
                    print(get_about)
                    driver.get(get_about)
                    driver.implicitly_wait(5)
                    if driver.find_elements_by_xpath("//span[normalize-space()='About']"):
                        driver.find_element_by_xpath("//span[normalize-space()='About']").click()
                    time.sleep(3)
                    # Data.......

                    #common
                    time.sleep(1)
                    profile_url = driver.current_url
                    print(profile_url)
                    if driver.find_elements_by_xpath(profile_name_xpath):
                        profile_name_data = driver.find_elements_by_xpath(profile_name_xpath)
                        print(profile_name_data[-1].text)
                    #uncommon
                    if driver.find_elements_by_xpath(profile_bio_xpath):
                        profile_bio_data = driver.find_element_by_xpath(profile_bio_xpath).text
                        print(profile_bio_data)

                    if driver.find_elements_by_xpath(work_data_xpath):
                        work_data = driver.find_element_by_xpath(work_data_xpath).text
                        print(work_data)
                    if driver.find_elements_by_xpath(edu_data_xpath):
                        edu_data = driver.find_element_by_xpath(edu_data_xpath).text
                        print(edu_data)
                    if driver.find_elements_by_xpath(current_city_data_xpath):
                        current_city_data = driver.find_element_by_xpath(current_city_data_xpath).text
                        print(current_city_data)
                    if driver.find_elements_by_xpath(from_city_data_xpath):
                        from_city_data = driver.find_element_by_xpath(from_city_data_xpath).text
                        print(from_city_data)
                    if driver.find_elements_by_xpath(relationship_data_xpath):
                        relationship_data = driver.find_element_by_xpath(relationship_data_xpath).text
                        print(relationship_data)
                    print("\n\n\n")
                    driver.close()
                    driver.switch_to.window(driver.window_handles[-1])
                    i += 1
                driver.get("https://mbasic.facebook.com/groups/bdblock")
                a += 1
go_post()