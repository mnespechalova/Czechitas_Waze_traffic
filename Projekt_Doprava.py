import pandas as pd
import numpy as np
import ast # nainstalovat balicek ast, ktery prevede string na seznam, automaticky rozpozna, ze v hranatych zavorkach mame list
from datetime import datetime
import geopy.geocoders # potrebujeme k geolokacnim udajum, doplneni nazvu ulic k souradnicim
from geopy.geocoders import Nominatim
""" from geopy extra rate Limiter import Nominatim """


trafficDelaysDf = pd.read_csv(r"C:\Users\Misulka\Desktop\Czechitas\Digitalni_akademie\Python\Projekt\trafficDelaysAll_16-10-2020.csv")
trafficEventsDf= pd.read_csv(r"C:\Users\Misulka\Desktop\Czechitas\Digitalni_akademie\Python\Projekt\trafficEventsAll_16-10-2020.csv")
usersCount =  pd.read_csv(r"C:\Users\Misulka\Desktop\Czechitas\Digitalni_akademie\Python\Projekt\poctyUzivatelu.csv", sep = ";", names = ["time", "usersCnt", "eventsCnt"], header =None)

usersCount. shape # ukaze pocet radku a sloupcu
trafficDelaysDf= trafficDelaysDf.drop(columns='type') #smazat prvni sloupec s nazvem type, protoze ho tam mame dvakrat

trafficDelaysDf.columns =trafficDelaysDf.drop(columns =['type']) #metoda drop columns smaze sloupec  s nazvem type

trafficDelaysDf.columns = trafficDelaysDf.columns.str.replace('properties.','')
#trafficDelaysDf.columns = trafficDelaysDf.columns.str.replace('geometry.','')
trafficDelaysDf= trafficDelaysDf.rename(columns={'geometry.type':'coordType'})
trafficDelaysDf= trafficDelaysDf.rename(columns={'geometry.coordinates':'coordinates'})
#trafficDelaysDf['coordType']=trafficDelaysDf['coordType'].iloc[:,1]
type(trafficDelaysDf['coordType'])
for colName in trafficDelaysDf.columns: # cyklus na vypis typu sloupcu
    print(type(trafficDelaysDf[colName]))


    #chceme prevest datum na cas
dateTimeStrList=[]  #chceme list bez tecek, kde je datum a cas, dame podminku, ze je tam separator . a +, protoze nekde nebyly milisekundy, tak nam to bez toho nerozdelilo
for i in range (0,len(trafficDelaysDf['pubMillis'])):
  if "." in trafficDelaysDf['pubMillis'][i]:
    dateTimeStrList.append (trafficDelaysDf['pubMillis'][i].lsplit(".")[0])
  elif "+" in trafficDelaysDf['pubMillis'][i]:
    dateTimeStrList.append (trafficDelaysDf['pubMillis'][i].lsplit("+")[0])

dateTimeList=[]
for i in range (0,len(dateTimeStrList['pubMillis'])):#chceme rozdelit cas na 2 sloupecky
      dateTimeList.append (datetime.strptime(dateTimeStrList[i], [%Y %m %d %H:%M:%S'])# prevede ze stringu na format datum a cas # pouzijeme metodu strptime


len(dateTimeList) # overime si, ze mame cely soubor, vyslo nam 116 709

weekDayList[] # chceme ziskat nazev dne
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
for i in range (0, len(dateTimeList)):
  weekDayList.append(weekDays[dateTiemList[i].weekday()])
trafficDelaysDf['datum_cas']= strptime('trafficDelaysDf['pubMillis'][0]) # prevede ze stringu na format datum a cas # pouzijeme metodu strptime

#nalepime nove sloupce do dataframu
trafficDelaysDf['datumCas']= dateTimeList
trafficDelaysDf['weekDaysCas']= weekDayList


hoursList=[]#chceme vytvorit sloupec s hodinou, udelame hourlist, bude to integer
for i in range(0,len(dateTimeList)):
  hoursList.append(dateTimeList[i].hour)

trafficDelaysDf['hours']= hoursList #nalepime nove sloupce do dataframu

minutesList=[]#chceme vytvorit sloupec s minutama
for i in range(0,len(dateTimeList)):
  minutesList.append(dateTimeList[i].minute)

trafficDelaysDf['minutes']= minutesList #nalepime novy sloupec do dataframu

quarters =[]#chceme vytvorit sloupec s minutama, zda je to ctvrt pul, trictvrte, cela
for i in range(0,len(dateTimeList)):
  if trafficDelaysDf['minutes'][i] <=15:
    quarters.append('1')
  elif trafficDelaysDf['minutes'][i] <=30:
    quarters.append('2')
  elif trafficDelaysDf['minutes'][i] <=45:
    quarters.append('3')
  else:
    quarters.append('4')
trafficDelaysDf['quarters']= quarters #nalepime novy sloupec do dataframu

#chceme dat sloupec coordinates do posledniho sloupce, protoze jsme tam nalepili jine sloupce, najit za domaci ukol
[trafficDelaysDf[trafficDelaysDf.columns[:-6]], trafficDelaysDf[trafficDelaysDf.columns[-6]]]
trafficDelaysDf1 = trafficDelaysDf[trafficDelaysDf[trafficDelaysDf.columns[:-6]], trafficDelaysDf[trafficDelaysDf.columns[-6]]]

trafficDelaysCoordByRowsDf=trafficDelaysDf.assign(coordinates=trafficDelaysDf.coordinates.str.split(",")).explode('coordinates') #ulozim si do noveho Df, metoda explode rozdeluje coordinates do radku

test = trafficDelaysDf["coordinates"][0]
test2 = ast.literal_eval(test)

coordList = []
for i in trafficDelaysDf.index:
  nNestList = ast.literal_eval(trafficDelaysDf["coordinates"][i])
  coordList.append(nNestList)# udela sloupec se sourednicema seznam v seznamu

trafficDelaysDf2=trafficDelaysDf.copy #zduplikovali jsme tabulku ,protoze jsme chteli zamenit sloupce coordinates
trafficDelaysDf2['coordinates']=coordList

allrowsList#dame vsechny radky

""" print(type(test2)) 
print(test2)
print(len(test2)) """


newlist = []
#dame vsechny radky
allrows =trafficDelaysDf2.value.tolist()
for line in allrows:
    newList += [line[:-1] + [coor] for coor in line[-1]] #kod od Martina, list comprehension misto explode, chceme coordinates

newlistMulti = []
for line in newList:  
    if 'MultiLineString' in line:
      newListMulti += [line[:-1] + [coor] for coor in line [-1]]
    else:
      NewListMulti.append(line)

trafficDelaysDf2= pd.DataFrame(newList)
trafficDelaysDf2.head#metoda k tisku nekolika radku

trafficDelaysDf3= pd.DataFrame(newListMulti)
trafficDelaysDf3.head #metoda k tisku nekolika radku

trafficDelaysDf3.columns =trafficDelaysDf.columns


#chceme si zkontrolovat, co se stalo s MultilineString ve sloupci coordinates
trafficDelaysDf2[['coordinates']trafficDelaysDf2['coordtype'==MultiLineString]

# chceme doplnit nazvy ulic k souradnicim, vyuzijeme modul geopy

geopy.geocoders.options.default_user_agent = 'Edg/86.0.622.43'
geolocator = Nominatim()
type(trafficDelaysDf3['coordinates'][0][0]) # vypise typ

trafficDelaysCoord = pd.read_csv(r"C:\Users\Misulka\Desktop\Czechitas\Digitalni_akademie\Python\Projekt\coord.csv")

trafficDelaysDf['street'].fillna('',inplace=True) #nahradi NaN za prazdny znak

trafficDelaysDf['street'].head ()

streetNaN = trafficDelaysDf['uuid'] trafficDelaysDf['street']==''] #vyfiltruj radky, ktere maji prazdnou ulici, je jich 4835

trafficDelaysCoord['uuid'].isin(streetNaN) # podminku, kterou vlozime

trafficDelaysCoordNaN=trafficDelaysCoord['uuid'].isin(streetNaN) # df, kde mame jenom radky,kde chybela ulice


streetList=[] # vytvorime list ulic, ktery pak prilepime
for rows in trafficDelaysCoordNaN['coordinates']:
  souradnice= str(row[1])+''+str(row[0])
 """  geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1) """ # dohledat zpozdeni

  location = geolocator.geocode(souradnice, language = "cz")
  nazev = location.raw['display_name']
  ulice = nazev.split(",")
  if len(ulice) == 9:
    streetList.append(ulice[1])
  elif len(ulice) == 8:
    streetList.append(ulice[0])
  else:
    streetList.append(ulice)


streetListdF = pd.DataFrame(columns=['streets3'])
streetlist2dF('street3')

trafficDelaysDf['pubMillis']trafficDelaysDf['pubMillis']].str.contains("+00")] # chceme vedet, zda tam je posun i jiny nez 00

#chceme prevest datum na cas
dateTimeStrList=[]  #chceme list bez tecek, kde je datum a cas, dame podminku, ze je tam separator . a +, protoze nekde nebyly milisekundy, tak nam to bez toho nerozdelilo
for i in range (0,len(trafficDelaysDf['pubMillis'])):
  if "." in trafficDelaysDf['pubMillis'][i]:
    dateTimeStrList.append (trafficDelaysDf['pubMillis'][i].lsplit(".")[0])
  elif "+" in trafficDelaysDf['pubMillis'][i]:
    dateTimeStrList.append (trafficDelaysDf['pubMillis'][i].lsplit("+")[0])

dateTimeList=[]
for i in range (0,len(dateTimeStrList['pubMillis'])):#chceme rozdelit cas na 2 sloupecky
      dateTimeList.append (datetime.strptime(dateTimeStrList[i], [%Y %m %d %H:%M:%S'])# prevede ze stringu na format datum a cas # pouzijeme metodu strptime


len(dateTimeList) # overime si, ze mame cely soubor, vyslo nam 116 709

weekDayList[] # chceme ziskat nazev dne
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
for i in range (0, len(dateTimeList)):
  weekDayList.append(weekDays[dateTiemList[i].weekday()])
trafficDelaysDf['datum_cas']= strptime('trafficDelaysDf['pubMillis'][0]) # prevede ze stringu na format datum a cas # pouzijeme metodu strptime

#nalepime nove sloupce do dataframu
trafficDelaysDf['datumCas']= dateTimeList
trafficDelaysDf['weekDaysCas']= weekDayList


hoursList=[]#chceme vytvorit sloupec s hodinou, udelame hourlist, bude to integer
for i in range(0,len(dateTimeList)):
  hoursList.append(dateTimeList[i].hour)

trafficDelaysDf['hours']= hoursList #nalepime nove sloupce do dataframu

minutesList=[]#chceme vytvorit sloupec s minutama
for i in range(0,len(dateTimeList)):
  minutesList.append(dateTimeList[i].minute)

trafficDelaysDf['minutes']= minutesList #nalepime novy sloupec do dataframu

quarters =[]#chceme vytvorit sloupec s minutama, zda je to ctvrt pul, trictvrte, cela
for i in range(0,len(dateTimeList)):
  if trafficDelaysDf['minutes'][i] <=15:
    quarters.append('1')
  elif trafficDelaysDf['minutes'][i] <=30:
    quarters.append('2')
  elif trafficDelaysDf['minutes'][i] <=45:
    quarters.append('3')
  else:
    quarters.append('4')
trafficDelaysDf['quarters']= quarters #nalepime novy sloupec do dataframu

#chceme dat sloupec coordinates do posledniho sloupci, protoze jsme tam nalepili jine sloupce
trafficDelaysDf


print (trafficDelaysDf.info())
trafficDelaysDf.shape
print (trafficDelaysDf_columns())