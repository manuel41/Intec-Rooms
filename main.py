from bs4 import BeautifulSoup as soup
import urllib.request as uReq
from Room import Room

login = '1088654'#input('Inserte su ID: ')
passw = 'Manuel144'#input('Inserte su contraseña: ')

# login_data = {
#     'txtID' : login,
#     'txtUserPass' : passw
# }

# import requests
# with requests.Session() as s:
#     url = "https://procesos.intec.edu.do/"
#     r = s.get(url)
#     pos_req = s.post(url, data=login_data)
#     print(pos_req.content)

rooms = []
with open('Oferta.html') as oferta_get:
    source = soup(oferta_get, 'lxml')
    asig_tags = source.findAll('td', class_='uk-text-center small-column')
    tag = 0
    for x in asig_tags:
        if tag == 0:
            newroom = Room()
        if tag == 3:
            for y in rooms:
                if rooms[y].name == x.text:
                    pass
            newroom.name = x.text
        if tag == 4

        #tag+=1
