from colorama import Fore
import time
import requests
def Httpheader():
    print(Fore.GREEN+"\nenter web address\n")
    time.sleep(0.5)
    ip = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"webfoker"+Fore.BLUE+"~"+Fore.RED+"""]
 └──╼ """+Fore.RED+"("+Fore.WHITE+"R"+Fore.RED+")"+Fore.WHITE)
    http= requests.get('https://api.hackertarget.com/httpheaders/?q=' + ip).text
    print(http)  
    x = True
    while x == True:
        print("Do you want to save this data?(y/n)")
        yes=input(Fore.GREEN+"(y/n?)"+Fore.WHITE)
        if yes == "y" or yes == "Y":
            data=open("Httpheader.txt","w")
            data.write("Http Header for : "+ip+"\n"+http)
            data.close()
            x = False
        elif yes == "n" or yes == "N":
            x=False
            pass    
   