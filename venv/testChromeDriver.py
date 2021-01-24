from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


# Ouvertur de la page Chrome, Démarrage du robot
driver = webdriver.Chrome('chromedriver.exe')
# Lien de la page formulaire
driver.get('https://www.qualibat.com/particulier/')