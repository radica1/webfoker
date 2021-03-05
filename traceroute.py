from colorama import Fore
import time
import requests

def trace():
    print(Fore.GREEN+"\nEnter your IP or Domin Address\n")
    time.sleep(0.5)
    ip = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"webfoker"+Fore.BLUE+"~"+Fore.RED+"""]
 └──╼ """+Fore.RED+"("+Fore.WHITE+"R"+Fore.RED+")"+Fore.WHITE)
    trace_rezullt = requests.get('https://api.hackertarget.com/mtr/?q=' + ip).text
    print(trace_rezullt)

    x = True
    while x == True:
        print("Do you want to save this data?(y/n)")
        yes=input(Fore.GREEN+"(y/n?)"+Fore.WHITE)
        if yes == "y" or yes == "Y":
            data=open("traceroute.txt","w")
            data.write(trace_rezullt)
            data.close
            x = False
        elif yes == "n" or yes == "N":
            x=False
            pass


    

