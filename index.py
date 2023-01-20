from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pyinputplus import inputEmail, inputPassword
from selenium.webdriver.common.action_chains import ActionChains
import time
from termcolor import colored, cprint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request


from bs4 import BeautifulSoup
import requests


options = webdriver.ChromeOptions()
options.add_argument('--headless')


email = inputEmail("Inserisci la tua email: ")
paswd = inputPassword("Inserisci la tua password: ")
path2 = 0

def input22():
    ll = [1, 2, 3]
    global path2
    leo = int(input(cprint((f"Premi:\n 1. Per Passaporto \n 2. Per Stato Civile \n 3. Carta D'Identita' \n"), 'red', attrs=['bold'])))
    if leo in ll:
        path2 = leo  
    else:
        print("Il tasto che hai premuto non e' corretto")
        path2 = 0

input22()
PATH  = 'C:/Users/got_a/OneDrive/Documents/msedgedriver'
driver = webdriver.Chrome(options=options)
print(webdriver.__version__)

driver.get("https://prenotami.esteri.it/")
print(driver.title) ## return the title

log_usr = driver.find_element(By.ID,"login-email")
log_usr.send_keys(email)
pswd_usr = driver.find_element(By.ID,"login-password")
pswd_usr.send_keys(paswd)

pswd_usr.send_keys(Keys.RETURN)

prn = driver.find_element(By.ID, "advanced").send_keys(Keys.RETURN)
cprint((f"You're inside your personal page {email}"), 'red', attrs=['bold'])


def onebu():
    driver.implicitly_wait(8000)
    pren = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//button[@class='button primary'][{path2}]"))
    )
    ActionChains(driver).move_to_element(pren).click(pren).perform()
    driver.implicitly_wait(10)
    
onebu()
    
cprint(("Stiamo per cercare la prenotazione...\n"), 'red', attrs=['bold'])
count = []
while True:
    try:
        count.append(1)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "jconfirm"))
        )
        exi = driver.find_element(By.CLASS_NAME,"jconfirm-buttons")
        cprint((f"Tentantivo numero {len(count)}\nAl momento non ci sono date disponibili per il servizio richiesto...\nRiproviamo...\n\n"), 'red', attrs=['bold'])
        ActionChains(driver).move_to_element(exi).click(exi).perform()
        time.sleep(2)
        
        onebu()
        
    except:
        strUrl = driver.current_url
        oo = str(strUrl)
        urllib.request.urlretrieve(oo, "pagina.txt")
        urllib.request.urlretrieve(oo, "pagina.html")
        cprint(("copia html"), 'red', attrs=['bold'])
        
        break

driver.quit()