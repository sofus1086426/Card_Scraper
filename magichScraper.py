#install dependensus
from bs4 import BeautifulSoup
import requests 


# url for scraping 
url = "https://magic.wizards.com/en/news/announcements/the-lost-caverns-of-ixalan-commander-decklists"


target = "deckbox_link"
# respons from web 
res = requests.get(url)
#pass the html and store it as a variable
soup = BeautifulSoup(res.text, "html.parser")
#scraping the html for the data we want
card_names = soup.find_all("span", attrs={"class":target})

#list to  store the info
cards =[]


for card_name in card_names:
  cards.append(card_name)

print(cards)