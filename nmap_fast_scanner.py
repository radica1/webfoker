from colorama import Fore
import time
import requests
def nmap1():
    print(Fore.GREEN+"\nEnter IP for fast scan with nmap \n")
    time.sleep(0.5)
    ip = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"webfoker"+Fore.BLUE+"~"+Fore.RED+"""]
 └──╼ """+Fore.RED+"("+Fore.WHITE+"R"+Fore.RED+")"+Fore.WHITE)
    tcp = requests.get('https://api.hackertarget.com/nmap/?q=' + ip).text
    
    print(tcp)  
    x = True
    while x == True:
        print("Do you want to save this data?(y/n)")
        yes=input(Fore.GREEN+"(y/n?)"+Fore.WHITE)
        if yes == "y" or yes == "Y":
            data=open("nmap_rezult.txt","w")
            data.write("your who tcp scan for : "+ip+"\n"+tcp)
            data.close()
            x = False
        elif yes == "n" or yes == "N":
            x=False
            pass    
