from bs4 import BeautifulSoup as soup
import urllib.request as uReq

import requests
with requests.Session() as s:
    url = "https://procesos.intec.edu.do/"
    r = s.get(url)
    print(r.content)