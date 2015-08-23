from lxml import html 
import requests

#inspired by http://docs.python-guide.org/en/latest/scenarios/scrape/ 


textfile = file('rcp_test','w')

def simple_scraper():
    news_source = requests.get('http://www.realclearpolitics.com/')
    html_tree = html.fromstring(news_source.text)
    for link in html_tree:
        article = dict()
        article['source'] = html_tree.xpath('//*[@id="story"]/text()')
        article['url'] = html_tree.xpath('//*[@id="story"]/a/@href')
        textfile.write(str(article))
    textfile.close()
	
simple_scraper()