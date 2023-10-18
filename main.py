from selenium.webdriver import Chrome                               # Chromedriver
from selenium.webdriver.common.by import By                         # To find the elements
from selenium.webdriver.support.ui import WebDriverWait             # To wait
from selenium.webdriver.support import expected_conditions as EC    # To wait
from selenium.webdriver.chrome.options import Options               # To resize the chrome window
from selenium.common.exceptions import TimeoutException             # To apply try/except
import time
from vlc import MediaPlayer

driver = Chrome()

driver.get("https://visa.vfsglobal.com/tur/pl/pol/login")
time.sleep(2)
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
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,"mat-checkbox-1"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,"mat-checkbox-2"))).click()
    time.sleep(2)    
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//mat-button-wrapper/span[contains(., 'Rozpocznij nową rezerwację')]"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,"mat-checkbox-3"))).click()
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//mat-stroked-button/span[contains(., 'Kontynuować')]"))).click()
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,"mat-select-0"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//mat-option/span[contains(., 'Male')]"))).click()
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,"mat-select-2"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//mat-option/span[contains(., 'Turkiye')]"))).click()
    time.sleep(2)
    driver.find_element(By.ID, "mat-input-3").send_keys("isim")
    driver.find_element(By.ID, "mat-input-4").send_keys("soyisim")
    driver.find_element(By.ID, "mat-input-5").send_keys("passaport")
    driver.find_element(By.ID, "mat-input-6").send_keys("90")
    driver.find_element(By.ID, "mat-input-7").send_keys("1234567890")
    driver.find_element(By.ID, "mat-input-8").send_keys("eposta")
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"mat-focus-indicator mat-stroked-button mat-button-base btn btn-block btn-brand-orange mat-btn-lg"))).click()

    # Let's test it until here.


while True:
    search()
    time.sleep(960)