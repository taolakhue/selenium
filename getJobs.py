from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os
import time
import csv
import pandas as pd
import re 
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://ca.indeed.com/jobs?q=computer%20science%20internship&l=Toronto,%20ON&radius=25&ts=1630423938843&pts=1630353837882&rq=1&rsIdx=0")
#time.sleep(100)
job_desc_list = []
temp_list = []
counter = 5

def create_df(*args):
    df = pd.DataFrame({
        "company":args[0],
        "job_header":args[1],
        "job_description":args[2]
    })
    return df

def get_page():
    try:
        main = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"resultsBodyContent"))
        )
    # Get company names and job titles
        job_titles = main.find_elements_by_tag_name("h2")
        company_names = main.find_elements_by_class_name("companyName")
        job_title=[list(job_title.text) for job_title in job_titles]
        companies = [company.text for company in company_names]
    
    # Get job description of each companies    
        for i in range(len(job_titles)):
            job_titles[i].click()
            time.sleep(4)
            vjs_desc = main.find_element_by_id("vjs-desc")
            job_desc_list.append(vjs_desc.text)
        #print(vjs_desc.text)
            time.sleep(1)
        job_list = [title.text.replace('new\n','') for title in job_titles ]

    # put into dictionary
        df = create_df(companies,job_list,job_desc_list)
        a = df.to_csv("data.csv")
        return a
    
    finally:
    #time.sleep(2)
    #driver.quit()
        pass

def main ():
    main = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"resultsBodyContent"))
        )
    forward = main.find_elements_by_class_name("np")

    print(len(forward))
    for i in range (6):
        try:
            time.sleep(2)
            a = main.find_elements_by_class_name("popover-x-button-close")
            if a != 0 :
                print('aaa')
      
        except NoSuchElementException as ex:
            pass
        forward[i].click()



main()

#print(len(companies))
#print(len(job_titles))
#print(job_desc_list)
