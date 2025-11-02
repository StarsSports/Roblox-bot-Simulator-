from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup browser
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Step 1: Go to Roblox
driver.get("https://www.roblox.com")
time.sleep(3)

# Step 2: Log in using cookie (manual step)
# You’ll need to inject .ROBLOSECURITY cookie manually or use a pre-authenticated session

# Step 3: Search for user
search = driver.find_element(By.NAME, "q")
search.send_keys("misterxd72")
search.send_keys(Keys.RETURN)
time.sleep(3)

# Step 4: Click on profile
driver.find_element(By.PARTIAL_LINK_TEXT, "misterxd72").click()
time.sleep(3)

# Step 5: Go to Creations tab
driver.find_element(By.LINK_TEXT, "Creations").click()
time.sleep(3)

# Step 6: Click on RPG Tower
driver.find_element(By.PARTIAL_LINK_TEXT, "RPG Tower").click()
time.sleep(3)

# Step 7: Click Play
driver.find_element(By.CLASS_NAME, "play-button").click()
time.sleep(600)  # Stay in game for 10 minutes

driver.quit()
