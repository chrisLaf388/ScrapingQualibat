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
choixMetier.select_by_value('106')

# Localisation liste déroulante
departement = Select(driver.find_element_by_id("depblock_2"))
departement.select_by_value('13')

# Valider le formulaire
submitBtn = driver.find_element_by_xpath('//*[@id="lim-back-research"]/div[2]/div/div[2]/form/div[2]/div[3]/input')
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
                        contact = contact.replace('\nTéléphone : ', '|')
                        contact = contact.replace('\nMail : ', '|')
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


