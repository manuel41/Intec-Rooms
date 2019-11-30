from bs4 import BeautifulSoup as soup
import urllib.request as uReq
from Room import Room
import time
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
    existingRoom = False
    for x in asig_tags:
        if tag == 3 and existingRoom == False:
            for y in range(len(rooms)):
                if rooms[y].name == x.text:
                    newroom = rooms[y]
                    existingRoom = True
                    break
                else:
                    newroom = Room()
                    existingRoom = True
                    break
        if x.text != '':
            if tag == 5:
                newroom.ParseTime(x.text, 'monday')
            if tag == 6:
                newroom.ParseTime(x.text, 'tuesday')
            if tag == 7:
                newroom.ParseTime(x.text, 'wednesday')
            if tag == 8:
                newroom.ParseTime(x.text, 'thursday')
            if tag == 9:
                newroom.ParseTime(x.text, 'friday')
            if tag == 10:
                newroom.ParseTime(x.text, 'saturday')
        tag+=1