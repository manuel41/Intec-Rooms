from bs4 import BeautifulSoup as soup
import urllib.request as uReq
import Room
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
        if tag == 2 and existingRoom == False and len(x.text) == 5:
            if len(rooms) == 0:
                newroom = Room.Room()
                newroom.name = x.text
                existingRoom = True
            else:
                for y in range(len(rooms)):
                    if rooms[y].name == x.text:
                        newroom = rooms[y]
                        existingRoom = True
                        break
            if existingRoom == False:
                newroom = Room.Room()
                newroom.name = x.text
                existingRoom = True
        if x.text != '':
            if tag == 3:
                newroom.AddTime(x.text, 'monday')
            if tag == 4:
                newroom.AddTime(x.text, 'tuesday')
            if tag == 5:
                newroom.AddTime(x.text, 'wednesday')
            if tag == 6:
                newroom.AddTime(x.text, 'thursday')
            if tag == 7:
                newroom.AddTime(x.text, 'friday')
            if tag == 8:
                newroom.AddTime(x.text, 'saturday')
        if tag == 8:
            if newroom in rooms:
                pass
            else:
                rooms.append(newroom)
            existingRoom = False
            tag = -1
        tag+=1