import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# Input the URL you want to scrap the pdf files
url = "https://www.rnsit.ac.in"

# If there is no such folder, the script will create one automatically
folder = 'webscraping'
if not os.path.exists(folder):os.mkdir(folder)

# Get the response object
response = requests.get(url)
#print(response.text)

# Response.text gives you a String, further parsing it using html parser
soup = BeautifulSoup(response.text, "html.parser")   

# Hunting for all the anchor tags containing .pdf in the href
for link in soup.select("a[href$='.pdf']"):
    # Name the pdf files using the last portion of each link which are unique in this case
    # link['href'].split('/')[-1] : Nothing but extracting the file name from the href
    filename = os.path.join(folder,link['href'].split('/')[-1])
    
    with open(filename, 'wb') as f:
        #print(requests.get(urljoin(url,link['href'])).content)
        f.write(requests.get(urljoin(url,link['href'])).content)
