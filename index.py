from selenium import webdriver 

PATH = '/home/fedegot/Documents/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get("https://consmanchester.esteri.it")
print(driver.title) ## return the title
#driver.quit()