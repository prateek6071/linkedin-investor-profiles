
# import web driver
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
import pandas as pd
from openpyxl.workbook import Workbook
# specifies the path to the chromedriver.exe
from webdrivermanager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=r'D:\chromedriver.exe')
driver.get('https://www.linkedin.com')
username = driver.find_element_by_id('session_key')

username.send_keys('prateekpamecha1511@gmail.com')
password = driver.find_element_by_id('session_password')

# send_keys() to simulate key strokes
password.send_keys('chinkydidi@88')
log_in_button = driver.find_element_by_class_name('sign-in-form__submit-button')

# locate submit button by_class_id


# .click() to mimic button click
log_in_button.click()
def getuserdata(page):
    driver.get('https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%2C%22101165590%22%2C%22105015875%22%2C%22101174742%22%2C%22101282230%22%2C%22100456013%22%2C%22103819153%22%2C%22105646813%22%2C%22106693272%22%2C%22105117694%22%2C%22102890719%22%2C%22104688944%22%2C%22106315325%22%2C%22101452733%22%5D&keywords=investor&origin=FACETED_SEARCH&page='+ str(page))

    driver.implicitly_wait(1)
    items =driver.find_elements_by_class_name('reusable-search__result-container')
    for i in items:
        a=[]
        k=i.find_element_by_class_name('entity-result__title-text')
        l=i.find_element_by_class_name('entity-result__primary-subtitle')
        a=k.text.split()

        profile_name=a[0 ] +" " + a[1 ]
        attribute=l.text
        try:
            degree=a[7 ]
        except:
            degree="private"
        location=i.find_element_by_class_name('entity-result__secondary-subtitle').text
        try:
            current_designation=i.find_element_by_class_name('entity-result__summary').text
        except:
            current_designation="private"
        try:
            profile_link=i.find_element_by_tag_name('a').get_attribute('href')
        except:
            profile_link="private"
        try:
            image_link=i.find_element_by_tag_name('img').get_attribute('src')
        except:
            image_link="private"
        userprofiledata={'profile_name':profile_name,
                         'degree':degree,
                         'location':location,
                         'current_designation':current_designation,
                         'profile_link':profile_link,
                         'image_link':image_link

                          }
        userdata.append(userprofiledata)


userdata=[]
for i in range(0,250):
    getuserdata(i)


df=pd.DataFrame(userdata)
print(df.head())
df.to_csv('userdata.csv')
df.to_excel('userdata.xlsx')

