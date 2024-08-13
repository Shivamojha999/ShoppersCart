import requests
from abc import ABC, abstractmethod

class Request(ABC):
    endpoint = "http://shoppingcart.local"
    request = requests
    securityKey = {"key":"ck_4ae151306917ba478ef1429d9dbb9bc3567625cc","secret":"cs_bf853a98b9e4df3c6255c782530478d9d4a0761a"}
    dbParameters = {"user":"root","password":"root","host":"localhost","port":"10005","dataBase":"local"}
