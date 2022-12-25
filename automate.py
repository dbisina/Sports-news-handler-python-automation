from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import os
import sys

#gets the path os the executable we are going to create
application_path = os.path.dirname(sys.executable)

now = datetime.now()
date_atm = now.strftime("%m%d%Y")


website = 'https://www.thesun.co.uk/sport/football/'
path = "/Users/danie/Downloads/chromedriver.exe "

#headless option -- everything is done in the background
options = Options()
options.headless = True
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

'''
#headed option - that is the process and broswer is hown
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)
'''
containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')


titles = []
subtitles = []
links = []


for container in containers:
    title=container.find_element(by="xpath", value='./a/h3').text
    subtitle=container.find_element(by="xpath", value='./a/p').text
    link=container.find_element(by="xpath", value='./a').get_attribute("href")

    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

import pandas as pd
dict = {'title':titles,
        'subtitle':subtitles,
        'link':links}

df_headlines = pd.DataFrame(dict)

fileName = f'headline--{date_atm}.csv'
finalPath = os.path.join(application_path, fileName)
df_headlines.to_csv(finalPath)

driver.quit()