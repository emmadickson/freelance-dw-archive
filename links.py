from bs4 import BeautifulSoup
import urllib.request
import requests
import os
t = open('404.txt', 'w')
tt = open('404_small.txt', 'w')

for filename in os.listdir('index.php/'):
    if filename.endswith(".html"): 
        print("http://localhost:3000/index.php/%s" % filename)
        resp = urllib.request.urlopen("http://localhost:3000/index.php/%s" % filename)
        soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'), features="html.parser")
        links = []
        for link in soup.find_all('a', href=True):
            links.append(link['href'])

        links = set(links)  
        t.write("FOUND ON PAGE: %s\n" % filename)  
        for link in links:
            if '../' in link:
                link = link[3:len(link)]
            link_relative = "http://localhost:3000/index.php/" + link
            resp = requests.get(link_relative)
            status_code = resp.status_code
            if str(status_code) == '404':
                t.write(link)
                t.write("\n")
                if 'http' not in link:
                    tt.write("FOUND ON PAGE: %s\n" % filename)  
                    tt.write(link)
                    tt.write("\n")
