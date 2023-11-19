# coding:utf8
#coded by mr.x
#tobat ker sekali kali
"""
untuk para kang recode mohon authornya di cantumkan
Ya bukan di pelajari malah di recode!
"""
import time,os,sys,re,threading
import subprocess as sp
try:
   from tqdm import tqdm
   import requests as req
   import requests
   from bs4 import BeautifulSoup as bs
except ImportError:
    sp.call('pip2 install tqdm bs4 requests',shell=True, stderr=sp.STDOUT)
#=---data--=
header=({'User-Agent':'Mozillla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'})

#=---data---=

G='\033[92m'
P='\033[97m'
R='\033[91m'
X='\033[90m'

link=[]
nam=[]
ukur=[]

def banner():
    os.system('clear')
    print """
{}   ▒▒{}██████{}▒▒▒▒▒▒{} -{} Surah Al-Qur'an mp3 Downloader
{}   ▒▒{}██{}▒▒{}█████{}▒▒▒{} -{} Abdurrahman-as-sudais
{}   ▒▒{}██{}▒▒▒▒▒{}██{}▒▒▒{} -{} Coded by Mr.X
{}   ▒▒{}█████{}▒▒{}██{}▒▒▒{} -{} version 1.0
{}   ▒▒▒▒▒{}██████{}▒▒▒    

    {}1.{}Lihat surah
    {}2.{}update
    {}3.{}info
    {}0.{}keluar
   """.format(X,G,X,G,P,X,G,X,G,X,G,P,X,G,X,G,X,G,P,X,G,X,G,X,G,P,X,G,X,G,P,G,P,G,P,G,P)
    menu()
def menu():
    ijo=raw_input(G+'   ["] '+P+'pilih: ')
    if ijo=='1':main()
    elif ijo=='2':
	n=raw_input(G+'   [?] '+P+'yakin(y/n): ')
	if n.lower() == "y":
	   print G+"   [*]"+P+" Tunggu sebentar jangan keluar nanti error."
    	   sp.call('cd ..;rm -rf surah-alquran-mp3',shell=True, stderr=sp.STDOUT)
	   sp.call('git clone https://github.com/Whomrx666/surah-alquran-mp3',shell=True, stderr=sp.STDOUT)
	   sp.call('cd surah-alquran-mp3',shell=True, stderr=sp.STDOUT)
	   sp.call('python2 surah-alquran-mp3.py',shell=True, stderr=sp.STDOUT)
	else:menu()
    elif ijo == '3':
        info()
    elif ijo == '0':
        sys.exit()
    else:
        banner()

def main():
  try:
    print '{}   [{}*{}]{} memuat surah sabar ya ...'.format(G,X,G,P)
    url="https://islamdownload.net/124129-download-murottal-mp3-abdurrahman-as-sudais.html"
    data=requests.get(url).text
    parser=bs(data,'html.parser')
    et=parser.find_all('a')
    ha=parser.find_all('div', {'align':'right'})
    b=0
    ukur.append('hai')
    for ai in ha:
        ukur.append(ai.text)
    link.append('hai')
    nam.append('hai')
    print '\n      '+G+25*'-'
    for go in et:
        o=go.get('href')
        if 'SURAT' in o:
           link.append(o)
    	   b+=1
	   hail=hai=o[o.find('_')-0:].replace('%27','').replace('.mp3','').replace('SURAT','').replace('__','').replace('_',' ')
           hai=(o[o.find('_')-0:].replace('%27','').replace('.mp3','').replace('SURAT','').replace('_',' ').replace('27T','T').replace('27A','A')+'\n'+'      '+G+25*'-').lower()
	   nam.append(hail)
	   print X+'      ['+G,b,X+']'+P+hai
        else:pass

    selet=int(raw_input(G+'\n   ["]'+P+' piligan:  '))
    if selet=='':main()
    elif selet=='0':main()
    elif selet>len(link):main()
    else:
        print """
         {}[•] {}surah: {}
         {}[•] {}ukran: {}
         {}----------------------------
        """.format(G,P,nam[selet].lower(),G,P,ukur[selet],G)
        don=raw_input('   '+G+'[+]'+P+' Download'+R+'(y/n): '+P)
        if 'y'==don:
           file=raw_input(G+'   [+] '+P+'save file: ').replace('.mp3','').replace('.mp4','')
	   gokil=req.get(link[selet],headers=header)
	   chunk_size=1024
	   total_size=int(gokil.headers['Content-Length'])
           with open(file+'.mp3','wb') as f:
	     for fdata in tqdm(desc=G+'   [*] '+nam[selet].lower().replace('al ','')+P,iterable = gokil.iter_content(chunk_size = chunk_size),total = total_size/chunk_size, unit = 'kb',ncols=45,ascii=True):
                f.write(fdata)
           print G+'   [+] '+P+'selesai nama: '+file+'.mp3'
           lagi=raw_input(G+'   [?]'+P+' download lagi'+R+'(y/n): '+P)
           if 'y'==lagi:
               banner()
	   else:sys.exit()
        else:banner()
  except Exception as F:
       print G+"   ["+R+"!"+G+"]"+P+" Jaringan Error"
       raw_input(G+'   {•}-'+P+'Enter kembali ke menu ...')

 
def info():
    print """
\t  {}_______________________________
\t [{}:::::::::::{}informasi{}:::::::::::{}]
\t  -------------------------------
\t{}
\t   created      19-november-2023
\t   author       Mr.X
\t   telegram:  https://t.me/@Whomr_X
\t
\t   thanks_to    BINC
\t   report       https://wa.me/6287855190571
\t   {}youtube{}  https://youtube.com/@whomrx666   
\t
\t {}---------------------------------

""".format(G,X,G,X,G,P,R,P,X)
    menu() 


if __name__=="__main__":
   banner()
