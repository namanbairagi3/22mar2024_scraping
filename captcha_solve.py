#Importing Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytesseract
from PIL import Image

# Path to tesseract executable (change this according to your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\ABHISHEK\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

#Opening the Webpage
browser = webdriver.Chrome()
browser.get('https://mphc.gov.in/case-status')

# Wait for the captcha to load
captcha_img = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'cp_img')))

# Save screenshot of the captcha
captcha_img.screenshot("./captcha.png")

# Read captcha using pytesseract
captcha_text = pytesseract.image_to_string(Image.open("./captcha.png")).strip()

# Find the input field and fill in the captcha
captcha_input = browser.find_element(By.ID, 'code')
captcha_input.send_keys(captcha_text)

time.sleep(5)  # Just for demonstration
