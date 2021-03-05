import sys
import requests
import os
import time
import bypass
import Dns_Look_Up
import find_admain_page
import findiplocation
import HTTPheader
import nmap_fast_scanner
import pagelinke
import sayhi
import Test_ping
import traceroute
import whois



try:
    from colorama import Fore
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install colorama\n
    pip3 install colorama
        """)

#---------------------------

try:
    import requests
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install requests\n
    pip3 install requests
        """)

#---------------------------
sayhi.sayhi()

while True:
    sayhi.menu()
    
    num = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"webfoker"+Fore.BLUE+"~"+Fore.RED+"""]
    └──╼"""+Fore.RED+"("+Fore.WHITE+"R"+Fore.RED+")"+Fore.WHITE)
    num=str(num)
    
    if num == "3":
            sayhi.Exit()
    if num == "2":
            sayhi.DDOS()
    if num == "1":
        
        sayhi.information()
        option = input(Fore.YELLOW+">>")
        if option == "1":
            bypass.bypasss()
        if option == "2":
             Dns_Look_Up.Dns_Look()
        if option == "3":
            find_admain_page.adminfinder()
            find_admain_page.save_data()
        if option == "4":
            HTTPheader.Httpheader()
        if option == "5":
            nmap_fast_scanner.nmap1()
        if option == "6":
            pagelinke.pagelinke()
        if option == "7":
            Test_ping.Test_ping()  
        if option == "8":
            traceroute.trace()
        if option == "9":
            whois.whois()          
    else:
        print(">")


