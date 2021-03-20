from selenium import webdriver   #to handle chromium webdriver
from selenium.webdriver.common.keys import Keys #to have keys name
from selenium.webdriver.support.ui import Select #to select from dropdown list
import time #to pause the scrolling 

#load the chrome webdriver (get the right one from https://chromedriver.chromium.org/downloads)
browser = webdriver.Chrome("C:\YOURPATH\chromedriver.exe")

#user data
user_cap = "20154"
power = 2700
gas = 1000
url = "https://www.ilportaleofferte.it/portaleOfferte/it/confronto-tariffe-prezzi-luce-gas.page?tipoOfferta=&code-istat=&cap-comune="

#login into the website
browser.get(url)
#page1
dual = browser.find_element_by_id("dual").click()

cap = browser.find_element_by_id("capComune")
cap.send_keys(user_cap)
time.sleep(0.5)
cap.send_keys(Keys.DOWN, Keys.RETURN)

pfix = browser.find_element_by_id("prezzoFisso").click()

casa = browser.find_element_by_id("casa").click()

residente = browser.find_element_by_id("residenteSI").click()

avanti = browser.find_element_by_class_name("btn").click()

#page2
potenza =  Select(browser.find_element_by_id("scegliPotenza"))
potenza.select_by_index(2)

consumo_luce = browser.find_element_by_id("consumoSI").click()

kwh = browser.find_element_by_id("consumoAnnuoSomma")
kwh.send_keys(power)

avanti = browser.find_element_by_link_text("Avanti").click()

#page3
cottura = browser.find_element_by_xpath('//label[@for="cottura"]').click()
acqua = browser.find_element_by_xpath('//label[@for="acquaCalda"]').click()
riscaldamento = browser.find_element_by_xpath('//label[@for="riscaldamento"]').click()

consumo_gas = browser.find_element_by_id("consumoGasSI").click()

smc = browser.find_element_by_id("ConsumoAnnuoGas")
smc.send_keys(gas)

avanti = browser.find_element_by_link_text("Avanti").click()
