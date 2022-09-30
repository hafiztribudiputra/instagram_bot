from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time
chromeDriverPath="C:\Chrome_log\chromedriver.exe"
## Here type the instagram account you want to go to
targed_account=""
## Here Type your instagram username
username=""
## Here Type your instagram password 
password=""
URL="https://www.instagram.com/accounts/login/"
class InstaFollower():
    def __init__(self,chromeDriverPath):
        self.driver= webdriver.Chrome(executable_path=chromeDriverPath)
    def login(self):
        global URL,username,password
        self.driver.get(URL)
        time.sleep(5)
        user_name_label=self.driver.find_element(By.XPATH,"/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input")
        user_name_label.send_keys(username)
        password_label=self.driver.find_element(By.XPATH,"/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input")
        password_label.send_keys(password)
        time.sleep(2)
        connect_button=self.driver.find_element(By.XPATH,"/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button")
        connect_button.send_keys(Keys.ENTER)                                                                                     
    def find_followers(self):
        global targed_account,URL
        self.driver.get(f"https://www.instagram.com/{targed_account}")
        try:
            follow_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a"))
        )
        except:
            print("error")
        finally:
            follow_button.click()
    def get_all_buttons(self):
        all_buttons=[]
        for x in range(1,11):
            try:
                buttons = self.driver.find_elements(By.XPATH,f"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{x}]/div[3]/button")
                all_buttons.append(buttons) 
            except:
                return all_buttons
        return all_buttons
    def follow(self):
        all_buttons=self.get_all_buttons()
        for buttons in all_buttons:
            for button in buttons:
                try:
                    button.click()
                    time.sleep(1)
                except ElementClickInterceptedException:
                    cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                    cancel_button.click()
def start_bot():
    bot=InstaFollower(chromeDriverPath)
    bot.login()
    time.sleep(10)
    bot.find_followers()
    time.sleep(10)
    bot.follow()
start_bot()