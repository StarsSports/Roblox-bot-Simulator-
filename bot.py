from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json, time, os

# Load accounts
with open("accounts.json") as f:
    accounts = json.load(f)

# Setup logging
report = {}
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

# Setup browser
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")

for acc in accounts:
    username = acc["username"]
    password = acc["password"]
    print(f"Logging in as {username}")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.roblox.com/login")
    time.sleep(3)

    try:
        # Fill login form
        driver.find_element(By.ID, "login-username").send_keys(username)
        driver.find_element(By.ID, "login-password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(5)

        # CAPTCHA detection
        if "captcha" in driver.page_source.lower():
            print(f"{username} blocked by CAPTCHA.")
            report[username] = "CAPTCHA Blocked"
            driver.save_screenshot(f"screenshots/{username}_captcha.png")
            input(f"🛑 Solve CAPTCHA for {username}, then press Enter to continue...")
            time.sleep(5)

        # Check login success
        if "home" in driver.current_url:
            print(f"{username} logged in.")
            driver.get("https://www.roblox.com/users/profile?username=misterxd72")
            time.sleep(3)
            try:
                driver.find_element(By.PARTIAL_LINK_TEXT, "RPG Tower").click()
                time.sleep(3)
                report[username] = "Success"
                driver.save_screenshot(f"screenshots/{username}_success.png")
            except:
                report[username] = "Game Not Found"
                driver.save_screenshot(f"screenshots/{username}_gamefail.png")
        else:
            report[username] = "Login Failed"
            driver.save_screenshot(f"screenshots/{username}_fail.png")

    except Exception as e:
        report[username] = f"Error: {str(e)}"

    driver.quit()
    time.sleep(2)

# Save report
with open("report.json", "w") as f:
    json.dump(report, f, indent=2)

print("✅ Bot loop complete.")
