import requests
import time
import argparse
import json
import random
import string

def randomString(strLength = 3):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(strLength))

def monitor_site(version, url, headers):
    check = True

    while check is True:
        rand_url = url + '&' + randomString()
        response = requests.get (rand_url, headers)

        response = requests.get (rand_url, headers)
        content = {}

        content = json.loads(response.text)

        new_version = content['results'][0]['version']

        if (new_version == version):
            print(f"Current version: {new_version}")
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
        url = "https://itunes.apple.com/lookup?id=1441586918&country=NZ"
    elif (args.app.lower() == "marvel" or args.app.lower() == "msf"):
        url = "https://itunes.apple.com/lookup?id=1292952049&123&country=NZ"
    
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
    content = {}

    content = json.loads(response.text)

    version = content['results'][0]['version']

    print(f"Inital version number: {version}")

    monitor_site(version, url, headers)

if __name__ == "__main__":
    main()