import urllib.request
import csv
import sys
from bs4 import BeautifulSoup


def getWikiURL():
    urls = []
    with open(sys.argv[1], newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
            urls.append(row[0])

    pages = []
    for url in urls:
        html = urllib.request.urlopen(url).read()

        soup = BeautifulSoup(html, "html.parser")
        table = soup.find('table', class_='infobox')
        span = soup.find('span', class_='url') if table == None else table.find('span', class_='url')
        a = soup.find('a', class_='external') if span == None else span.find('a', class_='external')

        tmp = str(a)
        b = tmp.find('href') + 6
        tmp = tmp[b:]
        e = tmp.find('"')
        a = tmp[:e]
        pages.append(a)

    with open('wikipedia_answers.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        for i in range(len(urls)):
            spamwriter.writerow([urls[i], pages[i]])



if __name__ == '__main__':
    getWikiURL()
