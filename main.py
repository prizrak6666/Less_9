
from bs4 import BeautifulSoup
import requests


response = requests.get("https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D1%87%D1%83%D0%B3/2023-11-13")
if response.status_code==200:
    soup = BeautifulSoup(response.text, features="html.parser")
    temp = soup.find("p","today-temp")
    print(temp.text)










