from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://ca.indeed.com/jobs?q=computer%20science%20internship&l=Toronto,%20ON&radius=25&ts=1630423938843&pts=1630353837882&rq=1&rsIdx=0")



try:
    main = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"mosaic-zone-jobcards"))
    )

    job_titles = main.find_elements_by_tag_name("h2")
    b = main.find_elements_by_class_name("companyName")

    for i in range (len(job_titles)):
        print(job_titles[i].text)
        print(b[i].text)
    

finally:
    time.sleep(5)
    driver.quit()
