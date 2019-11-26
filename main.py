from bs4 import BeautifulSoup as soup
import urllib.request as uReq

login = input('Inserte su ID: ')
passw = input('Inserte su contraseña: ')

login_data = {
    'txtID' : login
    'txtUserPass' : passw
}

import requests
with requests.Session() as s:
    url = "https://procesos.intec.edu.do/"
    r = s.get(url)
    print(r.content)