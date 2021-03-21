from selenium import webdriver   #to handle chromium webdriver
from selenium.webdriver.common.keys import Keys #to have keys name
from selenium.webdriver.support.ui import Select #to select from dropdown list
import time #to pause the scrolling 

#load the chrome webdriver (get the right one from https://chromedriver.chromium.org/downloads)
browser = webdriver.Chrome("C:\YOURPATH\chromedriver.exe")

#user data (enter here the data you need to modify)
user_cap = "20154"
power = 2700
gas = 1000
url = "https://www.ilportaleofferte.it/portaleOfferte/it/confronto-tariffe-prezzi-luce-gas.page?tipoOfferta=&code-istat=&cap-comune="
contract_type = "power" 
#use: "gas" "dual" or "power"

#get into the website
browser.get(url)

#page1

if contract_type == "dual": 
    dual = browser.find_element_by_id("dual").click()
elif contract_type == "gas":
    gas_only = browser.find_element_by_id("gas").click()
else:
    power_only = browser.find_element_by_id("energiaElettrica").click()


cap = browser.find_element_by_id("capComune")
cap.send_keys(user_cap)
time.sleep(0.5)
cap.send_keys(Keys.DOWN, Keys.RETURN)

pfix = browser.find_element_by_id("prezzoFisso").click()

casa = browser.find_element_by_id("casa").click()

if contract_type == "dual" or contract_type == "power":
    residente = browser.find_element_by_id("residenteSI").click()

else:
    pass 

avanti = browser.find_element_by_class_name("btn").click()

#page2

if contract_type == "dual" or contract_type == "power":
    potenza =  Select(browser.find_element_by_id("scegliPotenza"))
    potenza.select_by_index(2)

    consumo_luce = browser.find_element_by_id("consumoSI").click()

    kwh = browser.find_element_by_id("consumoAnnuoSomma")
    kwh.send_keys(power)
    
    try:
        avanti = browser.find_element_by_link_text("Avanti").click()
    except:
        confronta = browser.find_element_by_name("confronta").click()

else:
    pass

#page3

if contract_type == "dual" or contract_type == "gas":
    cottura = browser.find_element_by_xpath('//label[@for="cottura"]').click()
    acqua = browser.find_element_by_xpath('//label[@for="acquaCalda"]').click()
    riscaldamento = browser.find_element_by_xpath('//label[@for="riscaldamento"]').click()

    consumo_gas = browser.find_element_by_id("consumoGasSI").click()

    smc = browser.find_element_by_id("ConsumoAnnuoGas")
    smc.send_keys(gas)

else:
    pass 
try:
    avanti = browser.find_element_by_link_text("Avanti").click()
except:
    confronta = browser.find_element_by_name("confronta").click()
