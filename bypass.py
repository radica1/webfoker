import sys
import os
import socket
import time
from colorama import Fore,Back


def bypasss():
    print("Welcome to Bypass Cloud Flare part ")
    print("Enter your domin address")
    site = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"webfoker"+Fore.BLUE+"~"+Fore.RED+"""]
    └──╼ """+Fore.RED+"("+Fore.WHITE+"R"+Fore.RED+")"+Fore.WHITE)

    #finding subdomin with this 
    subdomin = ['ftp', 'cpanel', 'webmail', 'localhost', 'local', 'mysql', 'forum', 'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access', 'admin', 'administrator', 'email', 'downloads', 'ssh', 'owa', 'bbs', 'webmin', 'paralel', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure', 'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support', 'web', 'dev',"about"]
    #finish subdomin     
    for sub in subdomin:
      
        try:
            hosts = str(sub) + "." + str(site)
            bypass = socket.gethostbyname(str(hosts))
            #print('Cloudflare Bypassed ! Real IP Address => '+bypass)
            print (Fore.WHITE+" [!] CloudFlare Bypass " + Fore.BLUE+str(bypass) +Fore.YELLOW +' | ' +Fore.GREEN+ str(hosts))
        except Exception:
            pass
    print("do you want to continue ?")
    yes = input(Fore.YELLOW+">>(y/n)")
    if yes == "y" or yes == "Y":
         pass
    if yes == "n" or yes =="N":
        pass
            
     
