from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import pandas as pd
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://ca.indeed.com/jobs?q=computer%20science%20internship&l=Toronto,%20ON&radius=25&ts=1630423938843&pts=1630353837882&rq=1&rsIdx=0")

job_desc_list = []
temp_list = []
counter = 5



try:
    main = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"resultsBodyContent"))
    )
    # Get company names and job titles
    job_titles = main.find_elements_by_tag_name("h2")
    company_names = main.find_elements_by_class_name("companyName")
    job_title=[job_title.text for job_title in job_titles]
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
    data_dict = {'Job_title': job_list, 'Company_names':companies, 'Job_description':job_desc_list }
    print("This is data_dict: ",data_dict)
    temp_list.append(data_dict)
    df = pd.DataFrame(temp_list)
    df.to_csv('data.csv')
    
finally:
    #time.sleep(2)
    #driver.quit()
    pass



#print(len(companies))
#print(len(job_titles))
#print(job_desc_list)
