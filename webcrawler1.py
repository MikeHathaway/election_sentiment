#This is my first webcrawler

#Importing necessary libraries
from bs4 import BeautifulSoup
from urllib2 import urlopen

#For eventual interactive use
#int_news_source = raw_input('Enter Url to be mined:')

#URL to be parsed
news_source = 'http://www.realclearpolitics.com'


textfile = file('test1.txt','w')

#Code inspired by http://www.gregreda.com/2013/03/03/web-scraping-101-with-python/ 
def get_article_links(article_url):
    html = urlopen(article_url).read()
    soup = BeautifulSoup(html, "lxml") #initalizes url to be parsed by lxml
    homepage = soup.find("body", "homepage")
    section_links = [news_source + br.a["href"] for br in homepage.findAll("br")]
    textfile.write(str(section_links)) #adds link to textfile
    textfile.close()
    return section_links