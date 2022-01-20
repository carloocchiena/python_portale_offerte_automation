from datetime import date
import time 

from bs4 import BeautifulSoup as BS4  
import lxml 

from selenium import webdriver   
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By               
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# user data (enter here the data you need to modify)
today = date.today()
user_cap = "20154"
power = 2700
gas = 1000
url = "https://www.ilportaleofferte.it/portaleOfferte/it/confronto-tariffe-prezzi-luce-gas.page?tipoOfferta=&code-istat=&cap-comune="
contract_type = "dual" # use: "gas" "dual" or "power"

# get into the website
driver.get(url)

# page1

if contract_type == "dual": 
    dual = driver.find_element(By.ID, "dual").click()
elif contract_type == "gas":
    gas_only = driver.find_element(By.ID, "gas").click()
else:
    power_only = driver.find_element(By.ID, "energiaElettrica").click()

cap = driver.find_element(By.ID, "capComune")
cap.send_keys(user_cap)
time.sleep(0.5)
cap.send_keys(Keys.DOWN, Keys.RETURN)

pfix = driver.find_element(By.ID, "prezzoFisso").click()

casa = driver.find_element(By.ID, "casa").click()

if contract_type == "dual" or contract_type == "power":
    residente = driver.find_element(By.ID, "residenteSI").click()
else:
    pass 

avanti = driver.find_element(By.CLASS_NAME, "btn").click()

# page2

if contract_type == "dual" or contract_type == "power":
    potenza =  Select(driver.find_element(By.ID, "scegliPotenza"))
    potenza.select_by_index(2)

    consumo_luce = driver.find_element(By.ID, "consumoSI").click()

    kwh = driver.find_element(By.ID, "consumoAnnuoSomma")
    kwh.send_keys(power)
    
    try:
        avanti = driver.find_element(By.LINK_TEXT, "Avanti").click()
    except:
        confronta = driver.find_element(By.NAME, "confronta").click()
else:
    pass

# page3

if contract_type == "dual" or contract_type == "gas":
    cottura = driver.find_element(By.XPATH, '//label[@for="cottura"]').click()
    acqua = driver.find_element(By.XPATH, '//label[@for="acquaCalda"]').click()
    riscaldamento = driver.find_element(By.XPATH, '//label[@for="riscaldamento"]').click()

    consumo_gas = driver.find_element(By.ID, "consumoGasSI").click()

    smc = driver.find_element(By.ID, "ConsumoAnnuoGas")
    smc.send_keys(gas)
else:
    pass 

try:
    avanti = driver.find_element(By.LINK_TEXT, "Avanti").click()
except:
    confronta = driver.find_element(By.NAME, "confronta").click()
    
# printing out the results (only order of operators)
new_url = driver.page_source
soup = BS4(new_url, "lxml")
competitors = soup.find_all("p", {"class": ["nome_venditore"]})

for rank, comp, in enumerate(competitors):
    print (str(today)+ " " + f"{rank + 1}:" + comp.text)
    
# printing out the results (operators and annual cost of the energy supply)
new_url = driver.page_source
soup = BS4(new_url, "lxml")
competitors = soup.find_all(class_= ["nome_venditore", "prezzoOffertaValore"])

for rank, comp, in enumerate(competitors):
    print (str(today)+ " " + f"{rank + 1}:" + comp.text)
    
