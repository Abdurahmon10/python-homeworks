from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import json

chrome_options = Options()
chrome_options.add_argument("--window-position=-1700,-200")  # Position window on the second screen

# Set up the WebDriver (use the path to your driver if not in PATH)
driver = webdriver.Chrome(chrome_options)  # For Firefox, use webdriver.Firefox()

# Open a website
driver.get("https://www.demoblaze.com/")

laptops_button = driver.find_element(By.XPATH, '//*[@id="itemc"][2]')
laptops_button.click()
time.sleep(1)

laptops=[]

while True:
    infos = driver.find_elements(By.CLASS_NAME, 'h-100')
    for info in infos:
        name = info.find_element(By.CLASS_NAME, 'hrefch').text.strip()
        price = info.find_element(By.TAG_NAME, 'h5').text.strip()
        description = info.find_element(By.ID, 'article').text.strip().replace('\n', '')
        laptops.append({'name' : name, 'price' : price, 'description' : description})
    next_button = driver.find_element(By.ID, 'next2')
    if next_button.value_of_css_property('display') == 'none':
        break
    next_button.click()
    time.sleep(1)

with open("laptops.json", "w") as json_file:
    json.dump(laptops, json_file, indent=4)

with open("laptops.json", "r") as json_file:
    laptop_data = json.load(json_file)

print(laptop_data)

time.sleep(5)
# Close the browser
driver.quit()