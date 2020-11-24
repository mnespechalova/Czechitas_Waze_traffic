import requests
from requests_html import HTML
seznamUlic = []
for p in range(30,1860,30):
    url = f"https://encyklopedie.brna.cz/home-mmb/?acc=seznam_ulic&from={p}"
    response = requests.get(url)
    html = HTML(html=response.content)
    for bunka in html.find('.a_list'):
        seznamUlic.append(bunka.text)
soubor = open('uliceBrno.txt', 'w', encoding='utf-8')
[soubor.write(jmeno+",") for jmeno in seznamUlic]
soubor.close()




