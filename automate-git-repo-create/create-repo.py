
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time
from dotenv import load_dotenv

import argparse

# args
parser = argparse.ArgumentParser()
parser.add_argument("-r", dest="repo_name", help="Repository Name")

args = parser.parse_args()
if args.repo_name:
  repo_name = args.repo_name

load_dotenv()

USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")
DIR = os.getenv("DIR")

def create():
    base_project_path = DIR
    path = base_project_path+repo_name
    is_path_exists = os.path.exists(path)
    if not is_path_exists:
        os.makedirs(path)

    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.get('https://github.com/login')
    time.sleep(1)

    driver.find_element(By.ID, "login_field").send_keys("aiasha.arshi@gmail.com")
    driver.find_element(By.ID, "password").send_keys("Apajaan1!")
    time.sleep(1)

    driver.find_element(By.CLASS_NAME, "js-sign-in-button").send_keys(Keys.RETURN)
    time.sleep(2)

    plus_button = driver.find_element(By.XPATH, '//*[@id="repos-container"]/h2/a')
    plus_button.click()
    time.sleep(2)


    driver.find_element(By.CLASS_NAME, "js-repo-name").send_keys(repo_name)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="repository_visibility_private"]').click()
    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="new_repository"]/div[5]/button').click()

    time.sleep(10)


if __name__ == "__main__":
    create()
    a=1