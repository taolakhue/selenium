from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://ca.indeed.com/jobs?q=computer%20science%20internship&l=Toronto,%20ON&radius=25&ts=1630423938843&pts=1630353837882&rq=1&rsIdx=0")



try:
    main = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"resultsBodyContent"))
    )

    job_titles = main.find_elements_by_tag_name("h2")
    company_name = main.find_elements_by_class_name("companyName")
    """
    for i in range (len(job_titles)):
        print(job_titles[i].text)
        print(company_name[i].text)
        job_titles[i].click()
        #get content
        time.sleep(1)
    """
    job_titles[0].click()
    #Switch to another iFrame
    a=main.find_element_by_id("vjs-container")
    
    #job_description = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"jobDescriptionText")))

    

finally:
    time.sleep(5)
    