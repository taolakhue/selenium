from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


import time
import pandas as pd
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://ca.indeed.com/jobs?q=computer%20science%20internship&l=Toronto,%20ON&radius=25&ts=1630423938843&pts=1630353837882&rq=1&rsIdx=0")
#time.sleep(100)
companies=[]
job_list=[]
job_desc_list = []

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
        #job_title=[job_title.text for job_title in job_titles]
        #companies = [company.text for company in company_names]


        for i in range(len(job_titles)):
            job_titles[i].click()
            time.sleep(2)
            vjs_desc = main.find_element_by_id("vjs-desc")
            job_desc_list.append(vjs_desc.text)

        for title in job_titles:

            title = title.text.replace('new\n','')
            job_list.append(title)

        for company in company_names:

            company = company.text
            companies.append(company)

        #job_list = [title.text.replace('new\n','') for title in job_titles]

    finally:
        pass
def main():
    main = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"resultsBodyContent"))
        )
    #forward = main.find_elements_by_class_name("np")
    #print("this is forward",forward[0])

    try:
        for i in range (3):
            time.sleep(2)
            ignored_exceptions = (NoSuchElementException,StaleElementReferenceException)

            get_page()

            if i == 0:
                button = WebDriverWait(driver,10,ignored_exceptions=ignored_exceptions)\
                .until(EC.presence_of_element_located((By.CLASS_NAME,'np'))) 
            else:
                button = WebDriverWait(driver,10,ignored_exceptions=ignored_exceptions)\
                    .until(EC.presence_of_element_located((By.XPATH,'//*[@id="resultsCol"]/nav/div/ul/li[7]/a/span')))

            print("here",button)
            button.click()
            driver.refresh()


    finally:
        df = create_df(companies,job_list,job_desc_list)
        df.to_csv("data.csv")
        #time.sleep(3)
        driver.quit()

main()
#print(len(companies))
#print(len(job_titles))
#print(job_desc_list)
