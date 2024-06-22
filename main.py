from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os

# Set up the WebDriver (Assuming you have ChromeDriver installed and in your PATH)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
service = Service(executable_path=os.path.expanduser('/usr/bin/chromedriver'))  # Update the path to your ChromeDriver

driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10)

jobtitles = []
companies = []
locations = []

driver.get('https://www.linkedin.com/jobs/search?keywords="Fall+2024+Software+Intern&location=usa&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0')
driver.implicitly_wait(5)

# Find job cards
jobs = driver.find_elements(By.XPATH, "//ul[@class='jobs-search__results-list']/li")
print(f"Found {len(jobs)} job cards.")
for index, job in enumerate(jobs):
    if index >= 10:
        break
    jobtitle = job.find_element(By.XPATH, ".//h3[contains(@class, 'base-search-card__title')]").text.strip()
    print(f"Job title: {jobtitle}")
    company = job.find_element(By.XPATH, ".//h4[contains(@class, 'base-search-card__subtitle')]").text.strip()
    print(f"Company: {company}")
    location = job.find_element(By.XPATH, ".//span[contains(@class, 'job-search-card__location')]").text.strip()
    print(f"Location: {location}")

    jobtitles.append(jobtitle)
    companies.append(company)
    locations.append(location)


# Save to DataFrame
df_da = pd.DataFrame({
    'JobTitle': jobtitles,
    'Company': companies,
    'Location': locations,
})

print(df_da)
df_da.to_csv('/home/scifaipy/dev/python/selenium/test1/file_name1.csv', index=False)

driver.quit()
