from bs4 import BeautifulSoup
import requests
import pandas as pd
#missal
"""
dokumen = '''
<html>
<head>
    <title>Tutorial BeautifulSoup</title>
</head>

<body>
    <p class="judul">Judul Dokumen</p>

    <p class="paragraf">Ini adalah contoh paragraf</p>

    <a href="https://ngodingdata.com" class="url">Ngodingdata</a>
</body>

</html>
'''
html_soup = BeautifulSoup(dokumen, 'html.parser')

judul = html_soup.find('p', class_='judul')#find single
paragraf = html_soup.find('p', class_='paragraf')#find single
judul_saja = html_soup.find('p', class_='judul').text#kata katanya saja
print(judul)
print(paragraf)
print(judul_saja)

all_paragraf = html_soup.find_all('p')#mencari semua
print(all_paragraf)quotes = soup.find_all('div', class_='quote')
"""
#scraping web quotes

"""
quote = soup.find('span', class_='text').text
author = soup.find('small', class_='author').text
tags = [tag.text for tag in soup.find('div', class_='tags').find_all('a', class_='tag')]
"""
data = []
page = requests.get("http://quotes.toscrape.com/")
for page in range(1,11):
    if page == 1:
        url = "http://quotes.toscrape.com"
    else:
        url = "http://quotes.toscrape.com/page/"+str(page)
        
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
        
    print(url)
    
    quotes = soup.find_all('div', class_='quote')   
    for i in quotes:
        quote = i.find('span', class_='text').text
        author = i.find('small', class_='author').text
        tags = [tag.text for tag in i.find('div', class_='tags').find_all('a', class_='tag')]
        data.append({
            "QUOTES":quote,"AUTHORS":author,"TAGS":tags})
        
        
df = pd.DataFrame(data)

df.to_csv('C:/A11.2019.12292/all_quotes1.csv', index=False, encoding="utf-8")

