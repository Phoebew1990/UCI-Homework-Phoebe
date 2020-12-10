from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import pprint
import pymongo


def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)


def scrape():

    browser = init_browser()
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    mars_data = {}

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news_title = soup.find("div", class_="bottom_gradient").get_text()
    source = soup.find("div", class_="image_and_description_container")
    news_p = source.find("div", class_="rollover_description_inner").get_text()

    mars_data["news_title"]= news_title
    mars_data["news_p"]= news_p


    url_Mars = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_Mars)  

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')   

    image = soup.find("a", class_="button fancybox")["data-fancybox-href"]

    featured_image_url = "https://jpl.nasa.gov"+image

    url_fact = "https://space-facts.com/mars/"
    browser.visit(url_fact)

    table = pd.read_html(url_fact)
    table_df = table[0]
    table_df.columns = ["Facts","Value"]

    

    fact_html = table_df.to_html()
    fact_html=fact_html.replace("\n","")

    mars_data["fact_html"]=fact_html

    url_Hemispheres = ('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')
    browser.visit(url_Hemispheres)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    hemisphere_image_urls=[]

    for i in range (4):
        images = browser.find_by_tag('h3')
        images[i].click()
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        half_url = soup.find("img", class_="wide-image")["src"]
        img_title = soup.find("h2",class_="title").text
        img_url = 'https://astrogeology.usgs.gov'+ half_url
        dictionary={"title":img_title,"img_url":img_url}
        hemisphere_image_urls.append(dictionary)
        browser.back()
        


    mars_data["photos"]= hemisphere_image_urls
        
    
    
    
    mars_data["featured_image_url"]= featured_image_url



    return mars_data
    
    
       
    

   
    







