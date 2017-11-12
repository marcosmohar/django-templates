from .models import Character
import requests
from bs4 import BeautifulSoup

def scrapper(characters):
    sw_url = "http://starwars.wikia.com/wiki/{}"
    # formatea cada personaje de una lista de personajes y lo añade a una lista url_characters
    url_characters =[sw_url.format(character['name'].replace(' ', '_')) for character in characters] 
    # iniciar una lista para los characters
    list_characters = list()
    for index,url in enumerate(url_characters, start=0):
        req = requests.get(url)
        try:
            soup = BeautifulSoup(req.text, 'html.parser')
            imgs = soup.find_all('img', attrs={'class': 'pi-image-thumbnail'})
            list_characters.append(
                dict(
                    name=characters[index]['name'],
                    img_url = imgs[0]['src']
                )
            )
        except:
            list_characters.append(
                dict(
                    name=characters[index]['name'],
                    img_url= ''
                )
            )
    return list_characters

def get_character(page):
    url = "https://swapi.co/api/people/?page={}".format(page)
    r = requests.get(url)
    if r.status_code == 200:
        characters = scrapper(r.json()['results'])
        for character in characters:
            Character.objects.create(
                name = character['name'],
                img_url = character['img_url'],
                page = page
            )
