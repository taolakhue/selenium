from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://ca.indeed.com/jobs?q=computer%20science%20internship&l=Toronto,%20ON&radius=25&ts=1630423938843&pts=1630353837882&rq=1&rsIdx=0")



try:
    main = WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.ID,"mosaic-zone-jobcards"))
    )

    for element in main:
        header = element.
        print(element.text)



finally:
    driver.quit()
