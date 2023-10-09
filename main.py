from selenium import webdriver
import time
from pydub import AudioSegment
from pydub.playback import play

file_path = "Start.mp4"

audio = AudioSegment.from_file(file_path)

play(audio)

browser = webdriver.Chrome(executable_path='chromedriver')

browser.get("https://visa.vfsglobal.com/tur/pl/pol/login")

input("Press Y to proceed: ")

def search():
    checkmark = browser.find_element_by_id("mat-checkbox-1-input")
    checkmark.click()
    time.sleep(1)
    checkmark = browser.find_element_by_id("mat-checkbox-2-input")
    checkmark.click()
    time.sleep(1)
    button = browser.find_element_by_xpath("//button[contains(text(), ' Rozpocznij nową rezerwację ')]")
    button.click()
    time.sleep(1)
    checkmark = browser.find_element_by_id("mat-checkbox-3-input")
    checkmark.click()
    time.sleep(1)
    button = browser.find_element_by_xpath("//button[contains(text(), ' Kontynuować ')]")
    button.click()
    time.sleep(1)
    input_field = browser.find_element_by_id("mat-input-9")
    input_field.send_keys("Name")
    time.sleep(1)
    input_field = browser.find_element_by_id("mat-input-10")
    input_field.send_keys("Name")
    time.sleep(1)
    input_field = browser.find_element_by_id("mat-input-11")
    input_field.send_keys("Pass")
    time.sleep(1)
    input_field = browser.find_element_by_id("mat-input-12")
    input_field.send_keys("90")
    time.sleep(1)
    input_field = browser.find_element_by_id("mat-input-13")
    input_field.send_keys("Number")
    time.sleep(1)
    input_field = browser.find_element_by_id("mat-input-14")
    input_field.send_keys("email")
    time.sleep(1)
    dropdown = browser.find_element_by_id("mat-select-value-11")
    dropdown.click()
    time.sleep(1)
    dropdown = browser.find_element_by_id("mat-option-466")
    dropdown.click()
    time.sleep(1)
    dropdown = browser.find_element_by_id("mat-select-value-13")
    dropdown.click()
    time.sleep(1)
    dropdown = browser.find_element_by_id("mat-option-851")
    dropdown.click()
    time.sleep(1)
    button = browser.find_element_by_xpath("//button[contains(text(), ' Zapisz ')]")
    button.click()
    time.sleep(1)
    dropdown = browser.find_element_by_id("category")
    dropdown.click()
    dropdown.send_keys("D Visa")
    time.sleep(1)
    dropdown = browser.find_element_by_id("mission")
    dropdown.click()
    dropdown.send_keys("Poland, Warsaw")
    time.sleep(1)
    dropdown = browser.find_element_by_id("mission")
    dropdown.click()
    dropdown.send_keys("Poland, Warsaw")
    time.sleep(1)
    start_time = time.time()
    while True:
        try:
            button = browser.find_element_by_xpath("//button[contains(text(), 'Next')]")
            button.click()
            file_path = "Alarm.mp4"
            audio = AudioSegment.from_file(file_path)
            play(audio)
            break
        except:
            if time.time() - start_time > 300:
                browser.get("https://visa.vfsglobal.com/tur/pl/pol/dashboard")
                break
            time.sleep(5)
            dropdown = browser.find_element_by_id("mission")
            dropdown.click()
            dropdown.send_keys("asd")
            time.sleep(2)
            dropdown = browser.find_element_by_id("mission")
            dropdown.click()
            dropdown.send_keys("Poland, Warsaw")
            time.sleep(5)
            continue


while True:
    search()
    time.sleep(960)