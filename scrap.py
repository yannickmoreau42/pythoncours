import requests
import csv
from bs4 import BeautifulSoup
def extraire_donnees(elements):
    resultat = []
    for element in elements:
        resultat.append(element.string)
    return resultat

url = "https://www.youtube.com/channel/UC2-n0hri1DcZCbRRgavmqcQ/videos"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

jus = soup.find_all(class_="style-scope ytd-channel-name")
print(extraire_donnees(jus))
prix = soup.find_all(class_="prix")
print(extraire_donnees(prix)) 

with open('jus.csv', 'w') as f:
   writer = csv.writer(f, delimiter=',')
   for i in range(len(prix)):
      ligne = [jus[i], prix[i]]
      writer.writerow(ligne)