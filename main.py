import time

import requests

def connected_to_internet(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        #r = requests.get('http://192.168.2.11:5000/say/?text=The+internet+is+up')
        #print(r.status_code)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
        r = requests.get('http://192.168.2.11:5000/say/?text=The+internet+is+down')
        print(r.status_code)
    return False


while True:
    connected_to_internet()
    time.sleep(30)
