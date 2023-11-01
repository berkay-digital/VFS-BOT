from selenium.webdriver import Chrome                       
from selenium.webdriver.common.by import By                        
from selenium.webdriver.support.ui import WebDriverWait           
from selenium.webdriver.support import expected_conditions as EC   
from selenium.webdriver.chrome.options import Options            
from selenium.common.exceptions import TimeoutException            
import time
import random
from vlc import MediaPlayer
name = ""
surname = ""
passport = ""
code = ""
number = ""
mail = ""

with open('creds.txt', 'r') as file:
    lines = file.read().splitlines()

if len(lines) >= 6:
    name = lines[0]
    surname = lines[1]
    passport = lines[2]
    code = lines[3]
    number = lines[4]
    mail = lines[5]
else:
    print("The file 'creds.txt' does not contain enough lines.")
    exit()





driver = Chrome()

driver.get("https://visa.vfsglobal.com/tur/pl/pol/login")
time.sleep(5)
try:
    WebDriverWait(driver, 10) \
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
                                                    "div#onetrust-button-group button#onetrust-accept-btn-handler"))) \
                .click()
    # sometimes it doesn't work, so let's try again
    WebDriverWait(driver, 10) \
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
                                                "div#onetrust-button-group button#onetrust-accept-btn-handler"))) \
            .click()
except:
    pass

input("Press enter to proceed after entering the credentials.")


def search():
    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,"mat-checkbox-1"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,"mat-checkbox-2"))).click()
        time.sleep(2)
        driver.set_window_size(100, 700)    
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.mat-focus-indicator.btn.mat-btn-lg.btn-block.btn-brand-orange.mat-raised-button.mat-button-base"))).click()    
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,"mat-checkbox-3"))).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.mat-focus-indicator.btn.mat-btn-lg.btn-block.btn-brand-orange.mat-stroked-button.mat-button-base"))).click()    
        time.sleep(2)
        driver.maximize_window()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,"mat-select-0"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//mat-option/span[contains(., 'Male')]"))).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,"mat-select-2"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//mat-option/span[contains(., 'TURKEY')]"))).click()
        time.sleep(2)
        driver.find_element(By.ID, "mat-input-3").send_keys(name)
        driver.find_element(By.ID, "mat-input-4").send_keys(surname)
        driver.find_element(By.ID, "mat-input-5").send_keys(passport)
        driver.find_element(By.ID, "mat-input-6").send_keys(code)
        driver.find_element(By.ID, "mat-input-7").send_keys(number)
        driver.find_element(By.ID, "mat-input-8").send_keys(mail)
        time.sleep(30)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.mat-focus-indicator.mat-stroked-button.mat-button-base.btn.btn-block.btn-brand-orange.mat-btn-lg"))).click()
        # Let's test it until here. Edit: it works
        time.sleep(3)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,"mat-select-14"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//mat-option/span[contains(., '1 - Wiza typu D')]"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,"mat-select-16"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//mat-option/span[contains(., '4 - wiza typu D w celu innym  niż wymienione')]"))).click()
        time.sleep(2)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,"mat-select-18"))).click()
        MediaPlayer(r"Alarm.mp4").play()           
        time.sleep(20)                                     
        exit()
    except:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "navbarDropdown"))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "dropdown-item"))).click()
while True:
    search()
    time.sleep(random.uniform(3 * 60, 7 * 60))
