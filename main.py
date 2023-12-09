from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, csv
import undetected_chromedriver as uc

#--------------------------------------------------------#

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--log-level=3')

# -------------------------------------------------------#

print('[+] This is made by "Ahmed Mujtaba" ')
driver = webdriver.Chrome(options=options)
driver.maximize_window()
wait = WebDriverWait(driver, 5)
keywords = ["best 10th gen intel cpu"]
keyword_num = 0
keyword = keywords[keyword_num]
url = f"https://www.amazon.com/s?k={keyword.replace(' ', '+')}&ref=nb_sb_noss"
link_wait_time = 4.2
print(f"[+] Requesting the url of Amazon. Waiting for {link_wait_time} second/s")
driver.get(url)
time.sleep(link_wait_time)
total_product_no = 0
num = 0
page_no = 1
product_list = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//span[@data-component-type="s-search-results"]//div[@data-component-type="s-search-result"]')))
print(f"[+] Product Found : {len(product_list)}")
for x in range(50):
    for producT in product_list:
        print("[+] ---------------------------------------------------------------")
        total_product_no += 1
        num += 1
        print(f"[+] Scraping Product No #[{num}] on page no #[{page_no}].")
        try:
            data_asin = producT.get_attribute('data-asin')
        except:
            data_asin = ''
        product_url = driver.find_element(By.XPATH, f'(//span[@data-component-type="s-search-results"]//div[@data-component-type="s-search-result"]//h2//a)[{num}]').get_attribute('href')
        title = driver.find_element(By.XPATH, f'(//div[@data-component-type="s-search-result"]//h2)[{num}]').text
        try:
            price = str(driver.find_element(By.XPATH, f'(//div[@data-component-type="s-search-result"]//span[@class="a-price"])[{num}]').text).replace("\n",".")
        except: price = ""
        driver.execute_script(f"window.open('{product_url}');")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)
        try:
            rating = wait.until(EC.presence_of_element_located(((By.XPATH,"(//span[@id='acrPopover'])[1]")))).get_attribute('title')
        except:
            rating = ''

        review_url = product_url.replace('dp','product-reviews')

        try:
            brand_bio_link= driver.find_element(By.XPATH,"//a[@id='bylineInfo']").text
            brand_name = str(brand_bio_link).replace('Visit the ', '').replace(' Store', '')
        except:
            brand_name= ''
        
        print(f"[+] Title : ", title)
        print(f"[+] Product URL : ", product_url)
        print(f"[+] Data-Asin : {data_asin}")
        print(f"[+] Price : {price}")
        print(f"[+] Brand Name : {brand_name}")
        print(f"[+] Rating : {rating}")
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        print("[+] ------------------------------")
        if num == len(product_list):
            # wait.until(EC.presence_of_element_located((By.XPATH,"//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']"))).click()
            driver.get(f'https://www.amazon.com/s?k=keyboard&ref=nb_sb_noss&page={page_no}')
            page_no += 1
            num = 0
            print(f"[+] Moving to page no {page_no}")
            time.sleep(2.2)
            break