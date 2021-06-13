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













def get_about_data():
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


def go_post_and_collect_data():
    driver.get("https://www.facebook.com/forhadul06/posts/4329746860380234")
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(all_react_out).click()

    driver.switch_to.active_element

    driver.implicitly_wait(3)
    i = 1
    while i < 5:
        time.sleep(1)
        post_liker_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div["+str(i)+"]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/*[local-name()='svg'][1]/*[name()='g'][1]/*[name()='circle'][1]"
        i += 1
        element = driver.find_elements_by_xpath(post_liker_xpath)
        ActionChains(driver).key_down(Keys.CONTROL).click(element[-1]).key_up(Keys.CONTROL).perform()

        driver.switch_to.window(driver.window_handles[1])
        driver.implicitly_wait(5)
        if driver.find_elements_by_xpath("//span[normalize-space()='About']"):
            driver.find_element_by_xpath("//span[normalize-space()='About']").click()

        get_about_data()
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])
