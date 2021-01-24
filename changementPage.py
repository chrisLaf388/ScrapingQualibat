from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

# Ouvertur de la page Chrome, Démarrage du robot
driver = webdriver.Chrome('chromedriver.exe')
# Lien de la page formulaire
driver.get('https://www.qualibat.com/particulier/')

# Remplir le formulaire
# liste deroulante électricien ___ Id de la balise SELECT
choixMetier = Select(driver.find_element_by_id('wqq_domaines'))
choixMetier.select_by_value('106')

# Localisation liste déroulante
departement = Select(driver.find_element_by_id("depblock_2"))
departement.select_by_value('13')

# Valider le formulaire
submitBtn = driver.find_element_by_xpath('//*[@id="lim-back-research"]/div[2]/div/div[2]/form/div[2]/div[3]/input')
submitBtn.click()

# 1-click sur un lien
clickEntreprise = driver.find_element_by_xpath('//*[@id="result-entreprise"]/tbody/tr[1]')
clickEntreprise.click()

# afficher tous les caractétistiques d'une entrepirse
elements = driver.find_elements_by_css_selector('div.block p')
compteur = 0
for element in elements:
    if compteur == 0:
        compteur += 1
        print(element.text)
    elif compteur == 1:

        compteur += 1
        print(element.text)
    elif compteur == 2:

        compteur += 1
        print(element.text)
    elif compteur == 3:

        compteur += 1
        print(element.text)
    elif compteur == 4:

        compteur += 1
        print(element.text)
    elif compteur == 5:

        compteur += 1

        #adr = element.replace('<br>', ' ')
        adr = element.text
        adr = adr.replace('\n', ' ')
        adr = adr.strip('Adresse : ')
        print(adr)
    elif compteur == 6:

        compteur += 1
        tel = element.text
        tel = tel.strip('Téléphone : ')
        print(tel)
    elif compteur == 7:

        compteur += 1
        mail = element.text
        mail = mail.strip('Mail : ')
        print(mail)
        break