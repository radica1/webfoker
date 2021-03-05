import sys
import os
import socket
import time
from colorama import Fore,Back


def sayhi():
    
    #start interviwe
    print(Fore.RED+"========================================================================")
    time.sleep(1)   
    print(Fore.RED+""" 
    ######      #     ######   ###   #####      #     #       
    #     #    # #    #     #   #   #     #    # #    #       
    #     #   #   #   #     #   #   #         #   #   #       
    ######   #     #  #     #   #   #        #     #  #       
    #   #    #######  #     #   #   #        #######  #       
    #    #   #     #  #     #   #   #     #  #     #  #       
    #     #  #     #  ######   ###   #####   #     #  ####### \n""")

    time.sleep(2)
    print("############################################################\n\n\n\n\n ")
    time.sleep(1)
    
    #finish interviwe
  
def menu():
    time.sleep(0.1)
    print(Fore.RED+"Choose one of the options below\n")
    time.sleep(0.1)
    print(Fore.LIGHTYELLOW_EX+" [1] Information Gathering\n")
    time.sleep(0.1)
    print(Fore.LIGHTYELLOW_EX+" [2] DDOS Attack\n")
    time.sleep(0.1)
    print(Fore.LIGHTYELLOW_EX+" [3] Exit \n")



def information():
    time.sleep(0.1)
    print(Fore.GREEN+"  [1]"+Fore.BLUE+" - Bypass Cloud Flare")    
    print(Fore.CYAN+"  %%%%%%%%%%%%%%%%%%%%") 
   
    time.sleep(0.1)
    print(Fore.GREEN+"  [2]"+Fore.BLUE+" - Dns Look Up ")    
    print(Fore.CYAN+"  %%%%%%%%%%%%%%%%%%%%") 

    time.sleep(0.1)
    print(Fore.GREEN+"  [3]"+Fore.BLUE+" - Find Admin Page")    
    print(Fore.CYAN+"  %%%%%%%%%%%%%%%%%%%%") 

    time.sleep(0.1)
    print(Fore.GREEN+"  [4]"+Fore.BLUE+" - Show Http Header ")    
    print(Fore.CYAN+"  %%%%%%%%%%%%%%%%%%%%") 

    time.sleep(0.1)
    print(Fore.GREEN+"  [5]"+Fore.BLUE+" - Scan TCP Port ")    
    print(Fore.CYAN+"  %%%%%%%%%%%%%%%%%%%%") 

    time.sleep(0.1)
    print(Fore.GREEN+"  [6]"+Fore.BLUE+" - Get Page Links")    
    print(Fore.CYAN+"  %%%%%%%%%%%%%%%%%%%%") 


   
    print(Fore.GREEN+"  [7]"+Fore.BLUE+" - Test Ping")    
    print(Fore.CYAN+"  %%%%%%%%%%%%%%%%%%%%") 

    time.sleep(0.1)
    print(Fore.GREEN+"  [8]"+Fore.BLUE+" - Trace Toute")    
    print(Fore.CYAN+"  %%%%%%%%%%%%%%%%%%%%") 

    time.sleep(0.1)
    print(Fore.GREEN+"  [9]"+Fore.BLUE+" - whois")    
    print(Fore.CYAN+"  %%%%%%%%%%%%%%%%%%%%") 

def DDOS():
    print(Fore.LIGHTRED_EX+"""
    
    ██████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗ ██████╗     ███████╗ ██████╗  ██████╗ ███╗   ██╗
    ██╔════╝██╔═══██╗████╗ ████║██║████╗  ██║██╔════╝     ██╔════╝██╔═══██╗██╔═══██╗████╗  ██║
    ██║     ██║   ██║██╔████╔██║██║██╔██╗ ██║██║  ███╗    ███████╗██║   ██║██║   ██║██╔██╗ ██║
    ██║     ██║   ██║██║╚██╔╝██║██║██║╚██╗██║██║   ██║    ╚════██║██║   ██║██║   ██║██║╚██╗██║
    ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║██║ ╚████║╚██████╔╝    ███████║╚██████╔╝╚██████╔╝██║ ╚████║
    ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝
                                                                                          


    
    """)
def Exit():
    print(Fore.LIGHTCYAN_EX+"!!!GOOD BYE!!!")
    time.sleep(2)
    sys.exit    
   