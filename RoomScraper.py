from bs4 import BeautifulSoup as soup
import urllib.request as uReq
import Room
from datetime import datetime
import os.path
import urllib

def GetFileMonth():
    path = 'Oferta.html'
    file_created = os.path.getctime(path)

    d = datetime.utcfromtimestamp(file_created)
    formated_date = d.strftime('%m')
    return int(formated_date)

def RewriteSourceCode():
    if os.path.exists('Oferta.html'):
        os.remove('Oferta.html')

    login = input('Inserte su ID: ')
    passw = input('Inserte su contraseña: ')

    login_data = {
        'txtID' : login,
        'txtUserPass' : passw
    }
    
    import requests
    with requests.Session() as s:
        url = "https://procesos.intec.edu.do/"
        r = s.get(url)
        pos_req = s.post(url, data=login_data)
        oferta_get = s.get('https://procesos.intec.edu.do/OfertaAcademica/Index')
        oferta_source = oferta_get.content

        oferta_file = open('Oferta.html', 'wb')
        oferta_file.write(oferta_source)
        oferta_file.close

def GetRooms():
    current_month = datetime.today().month
    if (not os.path.exists('Oferta.html')):
        RewriteSourceCode()
    file_created_month = GetFileMonth()

    if (file_created_month > 4 or file_created_month < 2) and 1 < current_month < 5:
        RewriteSourceCode()
    elif (file_created_month < 5 or file_created_month > 7) and 4 < current_month < 8:
        RewriteSourceCode()
    elif (file_created_month < 8 or file_created_month > 10) and 7 < current_month < 11:
        RewriteSourceCode()
    elif (file_created_month < 11 or file_created_month > 1) and (current_month > 10 or current_month == 1):
        RewriteSourceCode()

    rooms = []
    time_list = []
    time_count = 0
    global rooms_section
    oferta = open('Oferta.html')

    source = soup(oferta, 'lxml')
    asig_tags = source.findAll('td', class_='uk-text-center small-column')
    tag = 0
    existingRoom = False
    for x in asig_tags:
        if tag == 2:
            rooms_section = x.text.split(', ')
        if x.text != '' and tag > 2:
            time_list.append(x.text)
            time_list.append(tag)
        if tag == 8:
            if len(rooms_section) == 1 and rooms_section[0] == 'VT1' or rooms_section[0] == 'VIRTU':
                pass
            else:
                if 'VT1' in rooms_section:
                    rooms_section.remove('VT1')
                if 'VIRTU' in rooms_section:
                    rooms_section.remove('VIRTU')
                hours = int(len(time_list)/2)
                count = 0
                room_count = 0
                excount = 0
                if time_list != []:
                    for a in range(hours):
                        room = Room.Room()
                        room.name = rooms_section[room_count]
                        for y in range(len(rooms)):
                            if rooms[y].name == rooms_section[room_count]:
                                room = rooms[y]
                                break
                        if hours == len(rooms_section):
                            room.AddTime(time_list[count], time_list[count+1])
                            room_count += 1
                        elif len(rooms_section) == 1:
                            room.AddTime(time_list[count], time_list[count+1])
                        elif hours == 3 and len(rooms_section) == 2:
                            excount+=1
                            room.AddTime(time_list[count], time_list[count+1])
                        if excount == 2:
                            room_count+=1
                        count += 2
                        if room not in rooms:
                            rooms.append(room)
            tag = -1
            existingRoom = False
            room_count = 0
            time_list.clear()
        tag+=1
    return rooms