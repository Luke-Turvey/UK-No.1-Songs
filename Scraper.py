from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv

uClient = uReq('https://www.officialcharts.com/chart-news/all-the-number-1-singles__7931/')
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")
rows = page_soup.findAll("tr")

for row in rows[3:]:
    songs = row.text.splitlines()[1:]
    if not 'DATE' in songs:
        with open(r'numberones.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([songs[0], songs[1], songs[2],songs[3]])


