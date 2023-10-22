# This scrapper script scrapes 71 quotes and saves them in "data_quotes.txt" file
# From this list, one file is randomly chosen and displayed on the canvas once the main program is run
# Last Line is manually removed to avoid printing empty text
# URL OF THE ORIGINAL DATA = https://graciousquotes.com/focus/


from bs4 import BeautifulSoup
import requests
import os
import sys


# for pyinstaller to locate assets and data
# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


URL = "https://graciousquotes.com/focus/"
response = requests.get(URL)
webpage = response.content
# print(webpage)
soup = BeautifulSoup(webpage, "html.parser")
# print(soup.prettify(encoding="utf-8"))
info = soup.select("div article div figure")
with open(resource_path("data_quotes.txt"), "w") as quotes:
    for q in info:
        quotes.write(f"{q.getText()} \n")
        # print(q.getText())
