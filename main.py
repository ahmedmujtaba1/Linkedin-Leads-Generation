from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, csv, pickle
import undetected_chromedriver as uc
from email_send import send_email

#--------------------------------------------------------#

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
path = r"B:\Ahmed'sCode\Linkedin-Leads-Generation\allforleads"
options.add_argument(f'--load-extension={path}')
options.add_argument('--log-level=3')

with open('output.csv', 'w', newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Headline', 'Linkedin URL', 'Email 1', 'Email 2', 'Phone Number 1', 'Phone Number 2'])

# -------------------------------------------------------#

print('[+] This is made by "Ahmed Mujtaba" ')
driver = webdriver.Chrome(options=options)
driver.maximize_window()
wait = WebDriverWait(driver, 5)
keywords = ["real estate"]
keyword_num = 0
keyword = keywords[keyword_num]
url = f"https://www.linkedin.com/search/results/people/?keywords={keyword.replace(' ','+')}"
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
driver.refresh()
cnt = 0
time.sleep(4.5)
flag = True
page_no = 1
found_lead = 0
all_leads = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//li[@class='reusable-search__result-container']//span[@class='entity-result__title-line entity-result__title-line--2-lines ']//a")))
try:
    driver.find_element(By.XPATH,"(//button[@class='msg-overlay-bubble-header__control msg-overlay-bubble-header__control--new-convo-btn artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view'])[2]").click()
except:pass
print(f"Found [{len(all_leads)}] Leads on Page No # [{page_no}]")
for i in range(500000000000):
    cnt += 1
    lead_name = wait.until(EC.presence_of_element_located((By.XPATH,f"(//li[@class='reusable-search__result-container']//span[@class='entity-result__title-line entity-result__title-line--2-lines ']//a)[{cnt}]"))).text
    if "LinkedIn" not in str(lead_name):
        headline = driver.find_element(By.XPATH,f"(//li[@class='reusable-search__result-container']//div[@class='entity-result__primary-subtitle t-14 t-black t-normal'])[{cnt}]").text
        profile_url = driver.find_element(By.XPATH,f"(//li[@class='reusable-search__result-container']//span[@class='entity-result__title-line entity-result__title-line--2-lines ']//a)[{cnt}]").get_attribute('href')
        lead_name = str(lead_name).split(' ')
        lead_name = f"{lead_name[0]} {lead_name[1]}".replace('View','').replace('\n','')
        driver.execute_script(f"window.open('{profile_url}');")
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='KLM_extension_company_product_name']//span[1]")))
        except:pass
        try:
            wait.until(EC.presence_of_element_located((By.ID,"KLMUnlockProfileInformation"))).click()
            time.sleep(2)
        except:
            try:
                time.sleep(2)
                wait.until(EC.presence_of_element_located((By.ID,"KLMUnlockProfileInformation"))).click()
                time.sleep(2)
            except:
                try:
                    time.sleep(1)
                    wait.until(EC.presence_of_element_located((By.ID,"KLMUnlockProfileInformation"))).click()
                    time.sleep(2)
                except:
                    try:
                        time.sleep(2)
                        wait.until(EC.presence_of_element_located((By.ID,"KLMUnlockProfileInformation"))).click()
                        time.sleep(2)
                    except:pass
        try:
            email1 = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='KLM_extensionSingleProfileViewWrapperBlockSingleRowData']//div[@class='KLM_extensionSingleProfileViewWrapperBlockSingleRowDataContent KLM_extensionSingleProfileViewWrapperBlockSingleRowDataContentContactData_1']"))).text
            email2 = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='KLM_extensionSingleProfileViewWrapperBlockSingleRowData']//div[@class='KLM_extensionSingleProfileViewWrapperBlockSingleRowDataContent KLM_extensionSingleProfileViewWrapperBlockSingleRowDataContentContactData_2']"))).text
            phone_number1 = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='KLM_extensionSingleProfileViewWrapperBlockSingleRowData']//div[@class='KLM_extensionSingleProfileViewWrapperBlockSingleRowDataContent KLM_extensionSingleProfileViewWrapperBlockSingleRowDataContentContactData_3']"))).text
            phone_number2 = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='KLM_extensionSingleProfileViewWrapperBlockSingleRowData']//div[@class='KLM_extensionSingleProfileViewWrapperBlockSingleRowDataContent KLM_extensionSingleProfileViewWrapperBlockSingleRowDataContentContactData_4']"))).text
            print("Name : ", lead_name)
            print("Headline : ", headline)
            print("Linkedin URL : ", profile_url)
            print("Email [1] : ", email1)
            print("Email [2] : ", email2)
            print("Phone Number [1] : ", phone_number1)
            print("Phone Number [2] : ", phone_number2)

            if email1:
                send_email(email1, lead_name)
            if email2:
                send_email(email2, lead_name)
            with open('output.csv', 'a', newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([lead_name, headline, profile_url, email1, email2, phone_number1, phone_number2])
            
            found_lead += 1
            print(f"Found [{found_lead}] LEADs")
            print("-----------------------------------------------------")

        except:pass
        # time.sleep(500000)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    if cnt == len(all_leads):
        last_lead = driver.find_element(By.XPATH,f"(//li[@class='reusable-search__result-container']//div[@class='entity-result__primary-subtitle t-14 t-black t-normal'])[{cnt}]")
        driver.execute_script("arguments[0].scrollIntoView();", last_lead)
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH,'//button[@aria-label="Next"]'))).click()
        page_no += 1 
        print(f"Found [{len(all_leads)}] Leads on Page No # [{page_no}]")       
        time.sleep(2)
        
        cnt = 0 
