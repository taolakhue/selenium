from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://ca.indeed.com/jobs?q=computer%20science%20internship&l=Toronto,%20ON&radius=25&ts=1630423938843&pts=1630353837882&rq=1&rsIdx=0")

job_desc_list = []

counter = 0

try:
    main = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"resultsBodyContent"))
    )

    job_titles = main.find_elements_by_tag_name("h2")
    company_names = main.find_elements_by_class_name("companyName")

    companies = [company.text for company in company_names]
    for i in range(len(job_titles)):
        job_titles[i].click()
        time.sleep(1)
        vjs_desc = main.find_element_by_id("vjs-desc")
        job_desc_list.append(vjs_desc.text)
        print(vjs_desc.text)


    job_list = [title.text.replace('new\n','') for title in job_titles ]
    
finally:
    #time.sleep(2)
    #driver.quit()
    pass


#print(len(companies))
#print(len(job_titles))
print(job_desc_list)