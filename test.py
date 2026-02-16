from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# -------------------
USERNAME = "agyeikendrick_"
PASSWORD = "Mezikpih11$$"
TWEET_TEXT = "Automated tweet from Brave!"
# -------------------

# Brave setup
chrome_options = Options()
chrome_options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

# Hide "Chrome is being controlled by automated test software"
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=chrome_options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
    """
})

driver.get("https://twitter.com/login")


# --- Wait for username input dynamically ---
wait = WebDriverWait(driver, 20)
username_input = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//input[@name="text"]')
))
username_input.send_keys(USERNAME)
username_input.send_keys(Keys.RETURN)

# --- Handle password input ---
password_input = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//input[@name="password"]')
))
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.RETURN)

time.sleep(5)

# --- Post a Tweet ---
tweet_box = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//div[@aria-label="Tweet text"]')
))
tweet_box.send_keys(TWEET_TEXT)

tweet_button = driver.find_element(By.XPATH, '//div[@data-testid="tweetButtonInline"]')
tweet_button.click()

time.sleep(5)

# --- Like first 3 tweets ---
driver.get("https://twitter.com/home")
time.sleep(5)
tweets = driver.find_elements(By.XPATH, "//div[@data-testid='like']")[:3]
for tweet in tweets:
    tweet.click()
    time.sleep(random.randint(2, 5))

print("Done! Brave bot completed.")
driver.quit()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

