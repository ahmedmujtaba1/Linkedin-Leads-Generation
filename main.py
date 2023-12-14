from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, csv, pickle
import undetected_chromedriver as uc

#--------------------------------------------------------#

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
path = r"B:\Ahmed'sCode\Linkedin-Leads-Generation\allforleads"
options.add_argument(f'--load-extension={path}')
options.add_argument('--log-level=3')

# -------------------------------------------------------#

print('[+] This is made by "Ahmed Mujtaba" ')
driver = webdriver.Chrome(options=options)
driver.maximize_window()
wait = WebDriverWait(driver, 5)
keywords = ["best 10th gen intel cpu"]
keyword_num = 0
keyword = keywords[keyword_num]
url = f"https://www.linkedin.com/search/results/people/?keywords={keyword.replace(' ','+')}&origin=GLOBAL_SEARCH_HEADER&sid=%3BLX"
link_wait_time = 4.2
print(f"[+] Requesting the url search of Linkedin. Waiting for {link_wait_time} second/s")
driver.get(url)
time.sleep(link_wait_time)
# user_input = input("Are you done? [y/n]: ")
# cookies = driver.get_cookies()
# with open('cookies.pkl', 'wb') as f:
#     pickle.dump(cookies, f)
with open('cookies.pkl', 'rb') as f:
    cookies = pickle.load(f)
for cookie in cookies:
    driver.add_cookie(cookie)