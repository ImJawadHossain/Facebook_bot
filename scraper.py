from fb_xpath import *
import xlsxwriter
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pathlib

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

driver.get("https://www.facebook.com/public/Forhadul-Islam")
print(input("After log-in facebook, type anything and press Enter: "))


workbook = xlsxwriter.Workbook('25.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Name')
worksheet.write('B1', 'Bio')
worksheet.write('C1', "Work")
worksheet.write('D1', "Education")
worksheet.write('E1', "Profile Url")


def getdata():
    i = 2
    a = 0
    while a < 10:

        driver.implicitly_wait(10)
        element = driver.find_elements_by_xpath(profile)
        ActionChains(driver).key_down(Keys.CONTROL).click(element[i]).key_up(Keys.CONTROL).perform()
        driver.switch_to.window(driver.window_handles[1])

        driver.implicitly_wait(6)
        name = driver.find_element_by_xpath(profileName).text
        worksheet.write('A' + str(i) + '', name)
        worksheet.write('E' + str(i) + '', driver.current_url)
        print("name sucessfully saved!")
        for g in range(6):
            education = "//div[@class='dati1w0a tu1s4ah4 f7vcsfb0 discj3wi']//div//div[5]//div[1]//div[1]//div[2]//div[1]"
            if driver.find_elements_by_xpath(education):
                work = driver.find_elements_by_xpath(education)
                worksheet.write('C' + str(i) + '', work[0].text)
                worksheet.write('D' + str(i) + '', work[-1].text)
                print("work and education sucessfuly saved!")
            else: print("work and education xpath not found")


            if driver.find_elements_by_xpath(profileBio):
                bio = driver.find_element_by_xpath(profileBio).text
                worksheet.write('B' + str(i) + '', bio)
                print("profile bio successfuly saved!")
            else:print("profile bio xpath not fuond")

        driver.close()
        driver.switch_to.window(driver.window_handles[-1])

        i += 1
        a += 1
try:
    getdata()
except:
    pass
workbook.close()