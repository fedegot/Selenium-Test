from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pyinputplus import inputEmail, inputPassword
from selenium.webdriver.common.action_chains import ActionChains
import time
from termcolor import colored, cprint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

email = inputEmail("Inserisci la tua email: ")
paswd = inputPassword("Inserisci la tua password: ")
path2  = input(cprint((f"Premi:\n 1. Per Passaporto \n 2. Per Stato Civile \n 3. Carta D'Identita' \n"), 'red', attrs=['bold']))
PATH  = 'C:/Users/got_a/OneDrive/Documents/msedgedriver'
driver = webdriver.Edge(PATH)
print(webdriver.__version__)

driver.get("https://prenotami.esteri.it/")
print(driver.title) ## return the title

log_usr = driver.find_element(By.ID,"login-email")
log_usr.send_keys(email)
pswd_usr = driver.find_element(By.ID,"login-password")
pswd_usr.send_keys(paswd)

pswd_usr.send_keys(Keys.RETURN)

prn = driver.find_element(By.ID, "advanced").send_keys(Keys.RETURN)
print(f"You're inside your personal page{email}")

# rkPEFKH52h%p!5
# //button[@class='button primary']



driver.implicitly_wait(8000)
pren = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, f"//button[@class='button primary'][{path2}]"))
)
ActionChains(driver).move_to_element(pren).click(pren).perform()
driver.implicitly_wait(10)
#if driver.find_element(By.CLASS_NAME, "jc-bs3-container container") == True:
    #print("No posizioni aperte al moment!!!!!!!!!!!!!!!!!!!")








time.sleep(5)

driver.quit()