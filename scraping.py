from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import csv

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

service = Service("chromedriver")  # Update this with your chromedriver path
driver = webdriver.Chrome(service=service, options=chrome_options)

# Define the URL (Replace with the actual e-commerce site)
url = "https://example.com/products"

driver.get(url)
time.sleep(3)  # Allow time for page to load

# Scroll to load dynamic content (if needed)
for _ in range(3):  
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(2)

# Get page source and parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

# Extract product details (Update selectors as per website structure)
products = []
for item in soup.find_all("div", class_="product-item"):  # Update class name
    name = item.find("h2", class_="product-title").text.strip()
    price = item.find("span", class_="product-price").text.strip()
    availability = item.find("span", class_="availability").text.strip()

    products.append([name, price, availability])

# Save to CSV
with open("products.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Price", "Availability"])
    writer.writerows(products)

print(f"Scraped {len(products)} products and saved to 'products.csv'.")
