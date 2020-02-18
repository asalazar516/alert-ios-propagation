import requests
import time
from bs4 import BeautifulSoup
import argparse

def monitor_site(version, url, headers):
    check = True

    while check is True:
        response = requests.get (url, headers)

        soup = BeautifulSoup(response.text, "html.parser")

        for item in soup.select("p.whats-new__latest__version"):
            new_version = item.get_text()

        if (new_version == version):
            print(f"{new_version}")
            time.sleep(45)
            continue
        else:
            t = time.localtime
            current_time = time.strftime("%H:%M:%S", t)
            current_date = time.strftime("%B %d, %Y", t)
            print(f"Version has changed from {version} to {new_version}!")
            print(f"Updated at {current_time} at {current_date}")
            check = False

def process(args):
    url = ""
    if(args.app.lower() == "avatar"):
        url = "https://apps.apple.com/nz/app/avatar-pandora-rising/id1441586918"
    elif (args.app.lower() == "marvel" or args.app.lower() == "msf"):
        url = "https://apps.apple.com/nz/app/marvel-strike-force-squad-rpg/id1292952049"
    
    if(url != ""):
        inital_scrape(url)
    else:
        print(f"{args.app} is not a FNG app. Suggestion use Avatar or Marvel")
    

def main():
    parser = argparse.ArgumentParser(description="Monitor FNG iOS propagation time")
    parser.add_argument("app", help="name a FNG app's IP title")
    args = parser.parse_args()

    process(args)

def inital_scrape(url):
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    response = requests.get (url, headers)

    soup = BeautifulSoup(response.text, "html.parser")

    for item in soup.select("p.whats-new__latest__version"):
        version = item.get_text()

    monitor_site(version, url, headers)

if __name__ == "__main__":
    main()