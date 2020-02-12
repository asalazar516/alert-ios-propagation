import requests
import time
from bs4 import BeautifulSoup


def main():
    url = "https://apps.apple.com/nz/app/marvel-strike-force-squad-rpg/id1292952049"
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    response = requests.get (url, headers)

    soup = BeautifulSoup(response.text, "html.parser")

    for item in soup.select("p.whats-new__latest__version"):
        version = item.get_text()
    
    print(version)

    if("Version 3.9.0" == version):
        print("same")
    else:
        print("Different")

if __name__ == "__main__":
    main()