gun=int(input("Günü giriniz: "))
if (gun<23):
 import requests
 from bs4 import BeautifulSoup
 import matplotlib.pyplot as cizim
 import numpy as n
 site_url = "http://finans.mynet.com/borsa/hisseler/adana-adana-cimento-a/tarihselveriler/"
 r =requests.get(site_url)
 soup= BeautifulSoup(r.content,"html.parser")
 veriLer=soup.find_all("table",{"class":"fnNewDataTable ndt-Gray ndt-BorderGray"})
 tarihsel_liste = ( veriLer[0].contents)[len( veriLer[0].contents)-2]
 tarihsel_liste = tarihsel_liste.find_all("tr")
 diziFiyat = []
 diziTarih = []
 diziHacim = []
 for veri in tarihsel_liste:
   bilgiler = veri.find_all("td")
   tarih = bilgiler[0].text
   sonFiyat = bilgiler[1].text
   hacim = bilgiler[4].text
   print(tarih, " | ", sonFiyat, " | ", hacim)
   print("*****************************************")
   diziFiyat = diziFiyat + [sonFiyat]
   diziTarih = diziTarih + [tarih]
   diziHacim = diziHacim + [hacim]
#******************Cizgi Grafigi******************************************
 D=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
 cizim.plot(D[0:gun],diziFiyat[0:gun], 'ro')
 cizim.plot(D[0:gun],diziFiyat[0:gun])
 cizim.xticks(D[0:gun],diziTarih[0:gun],rotation=45)
 cizim.xlabel('TARİHLER')
 cizim.ylabel('SON FİYATLAR')
 cizim.show()
#******************Sutun Grafigi*******************************************
 N = gun
 ind = n.arange(N)
 width = 0.15
 fig, ax = cizim.subplots()
 rects1 = ax.bar(ind,diziHacim[0:gun], width, color='b')
 ax.set_xlabel('TARİHLER')
 ax.set_ylabel('HACİMLER')
 ax.set_title('Tarihlere Göre Hacim Grafiği')
 ax.set_xticks(ind )
 ax.set_xticklabels (diziTarih[0:gun], rotation=45)
 ax.legend((rects1[0],'Hacim'))
 def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2.,height,'%d' % int(height), ha='center', va='bottom')
 autolabel(rects1)
 cizim.show()
else:
    print("Lütfen doğru aralıkta gün sayısı giriniz!")









