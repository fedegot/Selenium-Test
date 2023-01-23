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
from pywebcopy import save_webpage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options



driver = webdriver.Firefox(executable_path=r"/usr/local/bin/geckodriver")


email = inputEmail("Inserisci la tua email: ")
paswd = inputPassword("Inserisci la tua password: ")
path2 = 0

def input_servizio():
    ll = [1, 2, 3]
    global path2
    leo = int(input(cprint((f"Premi:\n 1. Per Passaporto \n 2. Per Stato Civile \n 3. Carta D'Identita' \n"), 'red', attrs=['bold'])))
    if leo in ll:
        path2 = leo  
    else:
        print("Il tasto che hai premuto non e' corretto")
        path2 = 0

path3 = 0
def tip_preno():
    ll = [1, 2]
    global path3
    leo = int(input(cprint((f"Premi:\n 1. Prenotazione Singola \n 2. Prenotazione Multipla \n"), 'red', attrs=['bold'])))
    if leo in ll:
        path3 = leo  
    else:
        print("Il tasto che hai premuto non e' corretto")
        path3 = 0
        
        
path4 = 0
def figli_min():
    ll = [1, 2]
    global path4
    leo = int(input(cprint((f"Hai figli minori:\n 1. Si \n 2. No \n"), 'red', attrs=['bold'])))
    if leo in ll:
        path4 = leo  
    else:
        print("Il tasto che hai premuto non e' corretto")
        path4 = 0
        
        
path5 = ""
def indirizzo():
    global path5
    leo = input(cprint((f"Indirizzo di residenza:"), 'red', attrs=['bold']))
    path5 = leo
    
path6 = ""
def statusr():
    global path6
    leo = input(cprint((f"La tua statura:"), 'red', attrs=['bold']))
    path6 = leo
    
path7 = 0
def stato_civ():
    ll= [1,2,3,4,5,6,7,8,9]
    global path7
    leo = int(input(cprint((f"Premi:\n 1. Coniugato/a \n 2. Divorziato/a \n 3. Vedovo/a \n 4. Celibe/Nubile \n 5. Separato/a 6. \n 6. Unito/a civilmente \n 7. Separato/a Un. Civile \n 8. Divorziato/a Un. Civile \n 9. Vedovo/a Un. Civile"), 'red', attrs=['bold'])))
    if leo in ll:
        path7 = leo  
    else:
        print("Il tasto che hai premuto non e' corretto")
        path7 = 0
        
        
path8 = ""
def commento_1():
    global path8
    leo = input(cprint(("Lascia delle note per il consolato:"), 'red', attrs=['bold']))
    path8 = leo
    
    
path9 = 0
def consenso_dati():
    global path9
    ll= [1,2]
    leo = input(cprint(("Lascio il consenso dei dati personali \n 1. Si \n 2. No")))
    if leo in ll:
        path9 = leo
    else:
        print("Il tasto che hai premuto non e' corretto")
        path9 = 0
        
consenso_dati()
input_servizio()
tip_preno()
figli_min()
indirizzo()
statusr()
stato_civ()
commento_1()


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

def downpage(oo):
        download_folder = 'C:/Users/got_a/OneDrive/Documents/Consolato/Selenium-Test/oo'    
        kwargs = {'bypass_robots': True, 'project_name': 'recognisable-name'}
        save_webpage(oo, download_folder, **kwargs)
        
        
strUrl = driver.current_url
oo = str(strUrl)
downpage(oo)
    
    
cprint(("Stiamo per cercare la prenotazione...\n"), 'red', attrs=['bold'])
count = []
while True:
    try:
        count.append(1)
        element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "jconfirm"))
        )
        exi = driver.find_element(By.CLASS_NAME,"jconfirm-buttons")
        cprint((f"Tentantivo numero {len(count)}\nAl momento non ci sono date disponibili per il servizio richiesto...\nRiproviamo...\n\n"), 'red', attrs=['bold'])
        ActionChains(driver).move_to_element(exi).click(exi).perform()
        time.sleep(2)
        onebu()
        
    except:
        
        if path9 == 1:
            driver.find_element(By.ID,"PrivacyCheck").click()
            print("Dati personali Accettati")
            driver.find_element(By.ID,"btnAvanti").click()
            break
        else: print("Non ho il consenso dei dati personali, impossibile andare avanti.")
        
        
        
        exii = driver.find_element(By.ID,"typeofbookingddl")
        select = Select(exii)
        select.select_by_index(path3)
        
        exi2 = driver.find_element(By.ID,"ddls_0")
        select = Select(exi2)
        select.select_by_index(path3)
        
        exi3 = driver.find_element(By.ID,"ddls_1")
        select = Select(exi3)
        select.select_by_index(path4)
        
        exi4 = driver.find_element(By.ID,"DatiAddizionaliPrenotante_2___testo")
        exi4.send_keys(path5)
        
        exi5 = driver.find_element(By.ID,"DatiAddizionaliPrenotante_3___testo")
        exi5.send_keys(path6)
        
        exi6 = driver.find_element(By.ID,"ddls_4")
        select = Select(exi3)
        select.select_by_index(path7)
        #Note
        exi7 = driver.find_element(By.ID,"BookingNotes")
        exi7.send_keys(path8)
        
        
        
        
        
        strUrl = driver.current_url
        oo = str(strUrl)
        urllib.request.urlretrieve(oo, "pagina.txt")
        urllib.request.urlretrieve(oo, "pagina.html")
        cprint(("copia html"), 'red', attrs=['bold'])
        print('\a')
        downpage(oo)
        
        
        
        
        break

driver.quit()