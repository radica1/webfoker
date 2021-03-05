from colorama import Fore
import time
import requests
def Dns_Look():
    print(Fore.GREEN+"\nEnter your Domin Address\n")
    time.sleep(0.5)
    ip = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"webfoker"+Fore.BLUE+"~"+Fore.RED+"""]
 └──╼ """+Fore.RED+"("+Fore.WHITE+"R"+Fore.RED+")"+Fore.WHITE)
    Dns_Look_Up= requests.get('https://api.hackertarget.com/dnslookup/?q=' + ip).text
    print(Dns_Look_Up)  
    x = True
    while x == True:
        print("Do you want to save this data?(y/n)")
        yes=input(Fore.GREEN+"(y/n?)"+Fore.WHITE)
        if yes == "y" or yes == "Y":
            data=open("Dns_LookUp.txt","w")
            data.write("your Dns looku for : "+ip+"\n"+Dns_Look_Up)
            data.close()
            x = False
        elif yes == "n" or yes == "N":
            x=False
            pass    
   