import requests
from bs4 import BeautifulSoup
enter_url = input("Enter the URL to be parsed ")

req = requests.get(url=enter_url)
content = req.content
soup_1 = BeautifulSoup(content, "html.parser")
soup = soup_1.find_all({"body" : "font_size"})

for all_soups in soup:
    input_1 = input("Enter value to be found ")
    soup_name = all_soups.find("{}".format(input_1))
    print(soup_name)
    pint("Created by Parth K (age : 12)")
