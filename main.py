from selenium import webdriver
from selenium.webdriver.support.ui import  Select
from selenium.webdriver.common.by import By
import pandas as pd
import time
website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
#path = 'F:\ChromeDriver\chromedriver.exe'
driver = webdriver.Chrome('F:\ChromeDriver\chromedriver.exe')
driver.get(website)

all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button.click()

dropdown=Select(driver.find_element(By.ID,'country'))
dropdown.select_by_visible_text('Germany')
time.sleep(4)

matches = driver.find_elements(By.TAG_NAME,'tr')
date=[]
home_team = []
away_team = []
score = []
for match in matches:
    date.append(match.find_element(By.XPATH,'./td[1]').text)
    home=match.find_element(By.XPATH, './td[2]').text
    home_team.append(home)
    print(home)
    score.append(match.find_element(By.XPATH, './td[3]').text)
    away_team.append(match.find_element(By.XPATH, './td[4]').text)
driver.close()
#Export to CSV
df = pd.DataFrame({'date': date,'home_team': home_team,'score': score,'away_team': away_team})
df.to_csv('football_data.csv',index=False)
print(df)
