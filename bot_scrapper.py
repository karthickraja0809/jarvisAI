from time import sleep 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

url = 'https://cdn.botpress.cloud/webchat/v1/index.html?options=%7B%22config%22%3A%7B%22composerPlaceholder%22%3A%22Talk%20To%20AVA%22%2C%22botConversationDescription%22%3A%22AVA%20-%20Virtual%20Assistance%22%2C%22botId%22%3A%22edc5688c-dea4-403e-a8b7-174f74b2747f%22%2C%22hostUrl%22%3A%22https%3A%2F%2Fcdn.botpress.cloud%2Fwebchat%2Fv1%22%2C%22messagingUrl%22%3A%22https%3A%2F%2Fmessaging.botpress.cloud%22%2C%22clientId%22%3A%22edc5688c-dea4-403e-a8b7-174f74b2747f%22%2C%22webhookId%22%3A%2278eee72c-3c67-4a7a-b3f7-0e4a4b6db757%22%2C%22lazySocket%22%3Atrue%2C%22themeName%22%3A%22prism%22%2C%22botName%22%3A%22AVA%20-%20Virtual%20Assistance%22%2C%22stylesheet%22%3A%22https%3A%2F%2Fwebchat-styler-css.botpress.app%2Fprod%2F05f75384-6d96-4cf6-8e18-d72b393ccc12%2Fv47548%2Fstyle.css%22%2C%22frontendVersion%22%3A%22v1%22%2C%22useSessionStorage%22%3Atrue%2C%22enableConversationDeletion%22%3Atrue%2C%22theme%22%3A%22prism%22%2C%22themeColor%22%3A%22%232563eb%22%2C%22chatId%22%3A%22bp-web-widget%22%2C%22encryptionKey%22%3A%22IrgljO2qz6miJtEKUVSASHA0fQNwG0fv%22%7D%7D'
chrome_driver_path = 'chromedriver.exe'

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Enable headless mode (runs Chrome without GUI)
chrome_options.add_argument('--log-level=3')  # Set Chrome log level
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2')

# Create a WebDriver service
service = Service(chrome_driver_path)

# Initialize Chrome WebDriver with the specified service and options
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(url)
sleep(3)

def click_on_chat_button():
    button = driver.find_element(By.XPATH, '/html/body/div/div/button')
    button.click()
    sleep(2)

def is_loader_visible(loader_class_name):
    try:
        loader = driver.find_element(By.CLASS_NAME, loader_class_name)
        return loader.is_displayed()
    except NoSuchElementException:
        return False

def send_query(text):
    textarea = driver.find_element(By.ID, 'input-message')
    textarea.send_keys(text)
    send_btn = driver.find_element(By.ID, 'btn-send')
    send_btn.click()
    sleep(1)

def retrieve_chat():
    chat_number = 2
    while True:
        try:
            p = driver.find_element(By.XPATH, f'/html/body/div/div/div/div[2]/div[1]/div/div/div[{chat_number}]/div/div[2]/div/div/div/div/div/p')
            print("\nAVA: " + p.text)
            chat_number += 2
        except NoSuchElementException:
            break

click_on_chat_button()
sleep(2)

# Example usage
send_query("Hello")
sleep(2)
retrieve_chat()
