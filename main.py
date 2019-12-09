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
room_count = 0
global rooms_section
with open('Oferta.html') as oferta_get:
    source = soup(oferta_get, 'lxml')
    asig_tags = source.findAll('td', class_='uk-text-center small-column')
    tag = 0
    existingRoom = False
    for x in asig_tags:
        if tag == 2:
            rooms_section = x.text.split(', ')
        if tag > 1:
            if len(rooms) == 0:
                room = Room.Room()
                room.name = rooms_section[room_count]
                existingRoom = True
            else:
                room = Room.Room()
                room.name = rooms_section[room_count]
                for y in range(len(rooms)):
                    if rooms[y].name == rooms_section[room_count]:
                        room = rooms[y]
                        break
        if x.text != '' and tag > 2:
            room.AddTime(x.text, tag)
            if room_count + 1 < len(rooms_section):
                room_count +=1
        if tag == 8:
            if room not in rooms:
                rooms.append(room)
            tag = -1
            room_count = 0
        tag+=1