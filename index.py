from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pyinputplus import inputEmail, inputPassword
import time


email = inputEmail("Inserisci la tua email: ")
paswd = inputPassword("Inserisci la tua password: ")
PATH = '/home/fedegot/Documents/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get("https://prenotami.esteri.it/")
print(driver.title) ## return the title

log_usr = driver.find_element(By.ID,"login-email")
log_usr.send_keys(email)
pswd_usr = driver.find_element(By.ID,"login-password")
pswd_usr.send_keys(paswd)

pswd_usr.send_keys(Keys.RETURN)

prn = driver.find_element(By.ID, "advanced").send_keys(Keys.RETURN)
print(f"You're inside your personal page{email}")
#prenot = driver.find_element(By.XPATH, "https://prenotami.esteri.it/Services/Booking/1137").send_keys(Keys.RETURN)
driver.navigate().to('https://prenotami.esteri.it/Services/Booking/1137')

time.sleep(5)

driver.quit()