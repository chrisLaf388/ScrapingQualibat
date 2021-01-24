#PROGRAMME FINI DE SCRAP AVEC AJUSTATION D AFFICHAGE

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
choixMetier = Select(driver.find_element_by_id('wqq_metiers_select'))
choixMetier.select_by_value('plombierchauffagisteclimaticien')

#Click plombier
choixPeintre = driver.find_element_by_xpath('//*[@id="lim-back-research"]/div[2]/div/div[1]/form/div[2]/div[2]/div[19]/div[3]/div[1]')
choixPeintre.click()

# Localisation liste déroulante
departement = Select(driver.find_element_by_id("depblock"))
departement.select_by_value('45')

# Valider le formulaire
submitBtn = driver.find_element_by_xpath('//*[@id="lim-back-research"]/div[2]/div/div[1]/form/div[2]/div[4]/input')
submitBtn.click()

#BUT : Boucle qui recupere toutes les données en clickant sur chaque entreprise

#Declaration de tableau
raisonSocial = []
dirigeants = []
sirets = []
dateCreationEntreprise = []
chiffreAffaires = []
effectifsEntreprise = []
contacts =[]
compteur = 0
compteurPageActuel = 1
bPageActuel = True
while (bPageActuel):

    #boucle qui entre dans un lien et retourne a la page precedente
    for colonne in range(1,11):

        # btnPageSuivant Boucle
        btnPageSuivant = driver.find_element_by_xpath('//*[@id="result-entreprise_next"]')
        for nbClickPage in range(1, compteurPageActuel):
            btnPageSuivant.click()

        #Pour empecher erreur si - 10 colonnes
        try :
            # 1-click sur un lien
            clickEntreprise = driver.find_element_by_xpath('//*[@id="result-entreprise"]/tbody/tr['+str(colonne)+']')
            clickEntreprise.click()


        except :
            bPageActuel = False
            break

        try :

            # recup Raison Social
            raisonSocialTemporaires = driver.find_elements_by_xpath('//*[@id="lim-back-research"]/div[2]/div/div[2]/div[1]/p')

            # afficher tous les caractétistiques d'une entrepirse
            elements = driver.find_elements_by_css_selector('div.block')
            compteur = 0
            for raisonSocialTemporaire in raisonSocialTemporaires:
                raisonSocial.append(raisonSocialTemporaire.text)
            for element in elements:

                if compteur == 0:
                    #Controles avec if
                    compteur += 1

                    if element.text.startswith('DIRIGEANT') :
                        dirigeant = element.text.replace('DIRIGEANT\n', '')
                        dirigeant = dirigeant.replace('\n', ' ')
                        print(dirigeant)
                        dirigeants.append(dirigeant)
                        continue

                    else:
                        dirigeants.append('null')
                        print('null')


                if compteur == 1:
                    compteur += 1
                    if element.text.startswith('SIRET'):
                        siret = element.text.replace('SIRET\n', '')
                        print(siret)
                        sirets.append(siret)
                        continue

                    else:
                        sirets.append('null')
                        print('null')

                if compteur == 2:
                    compteur += 1
                    if element.text.startswith('CRÉATION DE L’ENTREPRISE'):
                        dateCreat = element.text.replace('CRÉATION DE L’ENTREPRISE\n', '')
                        print(dateCreat)
                        dateCreationEntreprise.append(dateCreat)
                        continue

                    else:
                        dateCreationEntreprise.append('null')
                        print('null')

                if compteur == 3:
                    compteur += 1
                    if element.text.startswith('CHIFFRE'):
                        chriffre = element.text.replace("CHIFFRE D'AFFAIRES\n", "")
                        print(chriffre)
                        chiffreAffaires.append(chriffre)
                        continue

                    else:
                        chiffreAffaires.append('null')
                        print('null')

                if compteur == 4:
                    compteur += 1
                    if element.text.startswith('EFFECTIF'):
                        effectif = element.text.replace('EFFECTIF DE L’ENTREPRISE\n', '')
                        print(effectif)
                        effectifsEntreprise.append(effectif)
                        continue

                    else:
                        effectifsEntreprise.append('null')
                        print(element.text)
                        print('null')

                if compteur == 5:
                    if element.text.startswith('CONTACT'):
                        contact = element.text.replace('CONTACT\nAdresse : ', '')
                        contact = contact.replace(',\n', ' ')
                        contact = contact.replace('\nTéléphone :', '|')
                        contact = contact.replace('\nMail :', '|')
                        positionUrl = contact.find('http')
                        positionUrl2 = contact.find('www')
                        if contact.startswith('http',positionUrl):
                            contact = contact[:-(len(contact) - (positionUrl-1))]
                        if contact.startswith('www', positionUrl2):
                            contact = contact[:-(len(contact) - (positionUrl2-1))]

                        print(contact)
                        contacts.append(contact)
                        compteur += 1

                    else:
                        print('null')
                        contacts.append('null')

                    break

        #si aucune information sur la fiche contact ESSAI DE RECUP LES 4 Champs sur l'annuaire
        except:
            print('error')

        # revenir page precedente
        driver.back()

    compteurPageActuel += 1









print(len(raisonSocial))
print(len(dirigeants))
print(len(dirigeants))
print(len(dirigeants))
print(len(dirigeants))
test = pd.DataFrame({
    'Nom entreprise' : raisonSocial,
    'dirigeant' : dirigeants,
    'siret' : sirets,
    'dateCreationEntreprise' : dateCreationEntreprise,
    'chiffreAffaire' : chiffreAffaires,
    'effectifEntreprise' : effectifsEntreprise,
    'contact' : contacts

})

print(test)
test.to_csv('essai.csv',sep="|", encoding = 'iso-8859-1')


