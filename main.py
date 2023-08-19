from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

chrome_driver_path = "C:\Development\chromedriver.exe"
ser = Service(executable_path=chrome_driver_path)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", False)

EMAIL='mandliyaritika@gmail.com'
PASSWORD=os.getenv("PASSWORD")

def get_url(URL,BUY_PRICE):
    driver = webdriver.Chrome(options=options, service=ser)
    driver.get(URL)
    price_element = driver.find_element( By.CLASS_NAME, 'a-offscreen')
    title = driver.find_element(By.ID,'productTitle')
# retrieve the text from the price element
    price = price_element.get_attribute('innerHTML')
    title = title.text.strip()
    product_price= float(price.replace("₹", "").replace(",", ""))
    if product_price< BUY_PRICE:
        message = f"{title} is now {product_price}"
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            result = connection.login(EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
            )



webPage = input("Enter URL of the Amazon Product (Press Enter After Entering URL) : ")
BUY_PRICE =int(input("Enter Your Buying Price: "))

get_url(webPage,BUY_PRICE)