from colorama import Fore
import requests
import time
def Test_ping():
    print(Fore.GREEN+"\nEnter your IP or Domin Address\n")
    time.sleep(0.5)
    ip = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"webfoker"+Fore.BLUE+"~"+Fore.RED+"""]
 └──╼ """+Fore.RED+"("+Fore.WHITE+"R"+Fore.RED+")"+Fore.WHITE)
    test = requests.get('https://api.hackertarget.com/nping/?q='+ ip).text
    print(test)
  