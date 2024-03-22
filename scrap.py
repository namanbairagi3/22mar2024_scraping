from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import pytesseract
from PIL import Image


# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Start Chrome in maximized mode
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

# Path to tesseract executable (change this according to your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\ABHISHEK\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'


# Provide path to the chromedriver executable
webdriver_service = Service('./chromedriver.exe') 
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Open the webpage
driver.get('https://mphc.gov.in/case-status')

# Wait for the captcha to load
captcha_img = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'cp_img')))

# Save screenshot of the captcha
captcha_img.screenshot("./captcha.png")

# Read captcha using pytesseract
captcha_text = pytesseract.image_to_string(Image.open("./captcha.png")).strip()

# Find the input field for captcha and fill it
captcha_input = driver.find_element(By.ID, 'code')
captcha_input.send_keys(captcha_text)

# Find the input element by its ID for captcha
input_element = driver.find_element(By.ID, "code")
input_element.send_keys("123")

# Find the input element with id "txtnos" and fill it
input_element = driver.find_element(By.ID, "txtnoS")
input_element.send_keys("123")

# Find the select element by its ID for case type
select_element = driver.find_element(By.ID, "lst_caseS")
select = Select(select_element)
select.select_by_visible_text("WP - WRIT PETITION")

# Find the select element by its ID for year
select_element = driver.find_element(By.ID, "txtyear")
select = Select(select_element)
select.select_by_visible_text("2010")

# Find the button element by its ID and click it
button_element = driver.find_element(By.ID, "bt1")
button_element.click()

print(select_element)
print(select)

time.sleep(20)

# Close the browser
driver.quit()
