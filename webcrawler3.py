from lxml import html 
import requests

#inspired by http://docs.python-guide.org/en/latest/scenarios/scrape/ 

#need to add a conditional for type of politician

#convert file storage system to dictionary (enabling both title, and url)

textfile = file('rcp_test','w')

def simple_scraper():
    news_source = requests.get('http://www.realclearpolitics.com/')
    html_tree = html.fromstring(news_source.text)
    for link in html_tree:
        #source = html_tree.xpath('//*[@id="story"]/text()')
        article_url = html_tree.xpath('//*[@id="story"]/a/@href')
        textfile.write(str(article_url))
    textfile.close()
	
simple_scraper()