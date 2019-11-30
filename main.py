from bs4 import BeautifulSoup as soup
import urllib.request as uReq
import time

login = '1088654'#input('Inserte su ID: ')
passw = 'Manuel144'#input('Inserte su contraseña: ')

login_data = {
    'txtID' : login,
    'txtUserPass' : passw
}

# import requests
# with requests.Session() as s:
#     url = "https://procesos.intec.edu.do/"
#     r = s.get(url)
#     pos_req = s.post(url, data=login_data)

#     oferta_url = "https://procesos.intec.edu.do/OfertaAcademica/Index"
#     oferta_get = s.get(oferta_url)
#     source = soup(oferta_get.content, 'lxml')
#     print(source.tr)

with open('Oferta.html') as oferta_get:
    source = soup(oferta_get, 'lxml')
    for x in source.findAll('td', class_='uk-text-center small-column'):
        print(x.text)