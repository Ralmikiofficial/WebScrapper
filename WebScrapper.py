# Import requirements
import requests
from bs4 import BeautifulSoup #pip install bs4
from googlesearch import search
import urllib.request

# Function to download given file 
def download_file(download_url, filename): #takes input of url and filename that you want to give to the file
    response = urllib.request.urlopen(download_url)
    file = open(filename + ".pdf", 'wb')
    file.write(response.read())
    file.close()

# inurl is a set that contains 3 strings or you can add more , more you add more the chances you dont miss the file
inurl = ["insider trading policy", "upsi", "unpublished price sensitive information"]
downloaded = 0 #var to check if file is downloaded to exit if done
query = ""


# Forming a query with company name + x (eg. AIA ENGINEERING LTD INSIDER TRADING POLICY)
for x in inurl:
    a = "example" #a is name of site or organisation or the website name you want to scrap
    a = a.replace(".","") #no important just in case there is "." is removes it to make sure it doesn't cause any problem
    query = a + x

# Finding the first three results on searching query on google 
    for j in search(query, tld="co.in", num=3, stop=3, pause=5): #increase num and stop to increase your chances of getting file
        url = j
        if url.lower().find('.pdf') != -1: # If we get lucky enough that the first link occurs is the pdf we were looking for it will download it and exit code
            download_file(url, a)
            downloaded = 1
            break
# If obtained link is not a pdf,parse the page. 
        r = requests.get(url)
        htmlContent = r.content
        soup = BeautifulSoup(htmlContent, 'html.parser')
# Find the links with extention .pdf on the pages we got.
        anchors = soup.select("a[href$='.pdf']")
        for link in anchors:
            pdflink = link.get('href')
# Finding the keywords, inside, insider, trading policy in the pdf, if found download it. (we are finding insider trading policy for this example)
            if pdflink.lower().find('inside') != -1: #changes values of .find according to your dessired file possible name
                print(pdflink)
                download_file(pdflink, a)
                downloaded = 1
                break
            elif pdflink.lower().find('insider') != -1:
                print(pdflink)
                download_file(pdflink, a)
                downloaded = 1
                break
            elif pdflink.lower().find('tradingpolicy') != -1:
                print(pdflink)
                download_file(pdflink, a)
                downloaded = 1
                break
    if downloaded == 1 :
        print("pdf downloaded")
        downloaded = 0
        break
