from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

# Ouvertur de la page Chrome, Démarrage du robot
driver = webdriver.Chrome('chromedriver.exe')
# Lien de la page formulaire
driver.get('https://www.qualibat.com/particulier/')

# Remplir le formulaire
# liste deroulante électricien ___ Id de la balise SELECT
choixMetier = Select(driver.find_element_by_id('wqq_domaines'))
choixMetier.select_by_value('115')

# Localisation liste déroulante
departement = Select(driver.find_element_by_id("depblock_2"))
departement.select_by_value('13')

# Valider le formulaire
submitBtn = driver.find_element_by_xpath('//*[@id="lim-back-research"]/div[2]/div/div[2]/form/div[2]/div[3]/input')
submitBtn.click()

#BUT : Boucle qui recupere toutes les données en clickant sur chaque entreprise

#1-click sur un lien
clickEntreprise = driver.find_element_by_xpath('//*[@id="result-entreprise"]/tbody/tr[1]')
clickEntreprise.click()

#2-afficher tous les caractétistiques d'une entrepirse
elements = driver.find_elements_by_css_selector('div.block p')

#2Bis- Récuperer les données dans 9 tableaux
#dirigeant
#siret
#date de creation de l'entreprise
#chiffre d'affaires
#effectif de l'entreprise
#adresse
#telephone
#mail

#Declaration de tableau
#Nom entreprise !!!!!
raisonSocial = []
dirigeant = []
siret = []
dateCreationEntreprise = []
chiffreAffaire = []
effectifEntreprise = []
adresse = []
telepone = []
mail = []
compteur = 0

#recup Raison Social
raisonSocialTemporaires = driver.find_elements_by_xpath('//*[@id="lim-back-research"]/div[2]/div/div[2]/div[1]/p')
for raisonSocialTemporaire in raisonSocialTemporaires :
    raisonSocial.append(raisonSocialTemporaire.text)


#Boucle pour mettre chaque <p> dans le tableau correspondant
for element in elements :
    if compteur == 0 :
        dirigeant.append(element.text)
        compteur+=1
        print (element.text)
    elif compteur == 1 :
        siret.append(element.text)
        compteur += 1
        print(element.text)
    elif compteur == 2:
        dateCreationEntreprise.append(element.text)
        compteur += 1
        print(element.text)
    elif compteur == 3:
        chiffreAffaire.append(element.text)
        compteur += 1
        print(element.text)
    elif compteur == 4:
        effectifEntreprise.append(element.text)
        compteur += 1
        print(element.text)
    elif compteur == 5:
        adresse.append(element.text)
        compteur += 1
        print(element.text)
    elif compteur == 6:
        telepone.append(element.text)
        compteur += 1
        print(element.text)
    elif compteur == 7:
        mail.append(element.text)
        compteur += 1
        print(element.text)
        break

#revenir page precedente
clickPagePrecedente = driver.find_element_by_xpath('//*[@id="lim-back-research"]/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/a[2]')
clickPagePrecedente.click()
#3-recuperer tous les elements de la page

#4-retourner sur la page d'avant
#5-passer a la seconde entreprise et recuperer les données
#6-scrapper une page
#7scrapper toutes les pages
