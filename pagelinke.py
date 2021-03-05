from colorama import Fore
import time
import requests
def pagelinke():
    print(Fore.GREEN+"\nenter web address:\n")
    time.sleep(0.5)
    ip = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"webfoker"+Fore.BLUE+"~"+Fore.RED+"""]
 └──╼ """+Fore.RED+"("+Fore.WHITE+"R"+Fore.RED+")"+Fore.WHITE)
    who= requests.get('https://api.hackertarget.com/pagelinks/?q='+ip).text
    print(who)  
    x = True
    while x == True:
        print("Do you want to save this data?(y/n)")
        yes=input(Fore.GREEN+"(y/n?)"+Fore.WHITE)
        if yes == "y" or yes == "Y":
            data=open("pagelinke.txt","w")
            data.write("page links for : "+ip+"\n"+who)
            data.close()
            x = False
        elif yes == "n" or yes == "N":
            x=False
            pass    
   