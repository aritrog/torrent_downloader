import requests
from bs4 import BeautifulSoup,SoupStrainer
import os,subprocess,sys
#import winsound
import time

h={
	"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}


def t_searcher(key):
	rl=[]
	c=0
	count=-1
	prev=" "
	surl="https://1337x.to/search/"+key+"/1/"
	ress=requests.get(surl,headers=h)
	ss=BeautifulSoup(ress.content,'html.parser')
	for data in ss.find_all('div',attrs={'class':'table-list-wrap'}):
		for ttr in data.find_all('tr'):
			count=count+1
			if count==0 :
				continue
			temp=ttr.find_all('a')
			for al in temp:
				temp2=al['href']
				if al.find('torrent')!=-1:
					rl.append(temp2)
			txt=str(count)
			for tdd in ttr.find_all('td'):
				txt=txt+"\t"+tdd.text
			print(txt)	
	frl=[]
	for l in rl:
		if l.find('torrent')!=-1:
			frl.append(l)
	key2=int(input())
	nurl="https://1337x.to"+str(frl[key2-1])
	print(nurl)
	ct_searcher(nurl)
			
	
def ct_searcher(surl):

	ress=requests.get(surl,headers=h)
	ss=BeautifulSoup(ress.content,'html.parser')
	ssp=ss.find('div',attrs={'class':'col-9 page-content'})	
	print(ssp)
	for al in ssp.find_all('a'):
		temp=al['href']
		temp=str(temp)
		if temp.find("magnet")!=-1:
			result=temp
			break
	print(result)
	#os.startfile(result)	
	open_magnet(result)

def open_magnet(magnet):
        """Open magnet according to os."""
        if sys.platform.startswith('linux'):
            subprocess.Popen(['xdg-open', magnet],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elif sys.platform.startswith('win32'):
            os.startfile(magnet)
        elif sys.platform.startswith('cygwin'):
            os.startfile(magnet)
        elif sys.platform.startswith('darwin'):
            subprocess.Popen(['open', magnet],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            subprocess.Popen(['xdg-open', magnet],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
	
	
	
#key=input()
#key=key.replace(" ","+")
#t_searcher(key)
