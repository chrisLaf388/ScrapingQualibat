from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

# Ouvertur de la page Chrome, Démarrage du robot
driver = webdriver.Chrome("chromedriver.exe")
# Lien de la page formulaire
driver.get('https://www.qualibat.com/particulier/')

# Remplir le formulaire
# liste deroulante électricien ___ Id de la balise SELECT
choixMetier = Select(driver.find_element_by_id('wqq_domaines'))
choixMetier.select_by_value('106')

#########
# Localisation liste déroulante
departement = Select(driver.find_element_by_id("depblock_2"))
departement.select_by_value('13')

# Valider le formulaire
submitBtn = driver.find_element_by_xpath('//*[@id="lim-back-research"]/div[2]/div/div[2]/form/div[2]/div[3]/input')
submitBtn.click()

# Déclaration des tableaux
nomsEntreprise = []
villesEntreprise = []
effectifs = []
telephones = []

# init
iPageCourante = 0
sText = ''
sPageTotal = ''
iPageTotal = 0
i = 0
bPageContinue = True
iLongueurSousChaine = 0
tNumero = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
bCheckNumeroTotalPage = True
# recuperation
sText = driver.find_element_by_xpath('//*[@id="result-entreprise_paginate"]/span[4]').text
i = len(sText) - 1
j = 0
k = 2

# recupération du nombre total de page (string -> int)
while (i > 0):
    # Boolean pour sortir de la boucle quand le nombre de page totale est trouvé
    bCheckNumeroTotalPage = False

    for j in tNumero:
        # Verifie si c'est un numéro
        if (sText[i] == j):
            sPageTotal += sText[i]
            bCheckNumeroTotalPage = True
    i -= 1
    if bCheckNumeroTotalPage == False:
        i = 0

# [::-1]inverse l'ordre des nombres pour les remettre dans l'ordre
sPageTotal = sPageTotal[::-1]
print(sPageTotal)

colonne = 0
j = 0
bConditionColonne = True
iPageTotal = int(sPageTotal)
while bPageContinue:
    print('boucle page')
    bConditionColonne = True
    colonne = 0
    # Scraper tous les infos de la page
    while bConditionColonne:
        colonne += 1
        for k in range(2, 6):
            print('karo')
            # Si Pas d'erreur alors Fait les instructions du try SINON Met condition = Faux
            try:
                bConditionColonne = True
                tamp = driver.find_element_by_xpath(
                    '//*[@id="result-entreprise"]/tbody/tr[' + str(colonne) + ']/td[' + str(k) + ']').text
                if (k == 2):
                    nomsEntreprise.append(tamp)
                elif (k == 3):
                    villesEntreprise.append(tamp)
                elif (k == 4):
                    effectifs.append(tamp)
                elif (k == 5):
                    telephones.append(tamp)

            except NoSuchElementException:
                print("erreur")

                bConditionColonne = False

    j += 1
    # condition pour continuer a cliquer tant que i n'atteind pas le nombre de page max
    if j < iPageTotal:
        pageNext = driver.find_element_by_xpath('//*[@id="result-entreprise_next"]')
        pageNext.click()
    else:
        bPageContinue = False

print('fin de boucle')

# affichage en tableau
test = pd.DataFrame({
    'Nom entreprise': nomsEntreprise,
    'villesEntreprise': villesEntreprise,
    'effectifs': effectifs,
    'téléphones': telephones

})

print(test)
test.to_csv('essai.csv',sep="|", encoding = 'iso-8859-1')
