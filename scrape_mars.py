from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver


#excute chromedrive for windows
def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_data = {}

    #url website for scraping
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.find_all('div', class_='content_title')
    tbody = soup.find_all('div', class_='article_teaser_body')

    #url website for scraping
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)

    html = browser.html
    featured_soup = BeautifulSoup(html, 'html.parser')

    featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA16217_ip.jpg'


    mars_weather = 'Sol 2047 (May 10, 2018), Sunny, high 3C/37F, low -71C/-95F, pressure at 7.33 hPa, daylight 05:22-17:20'

    # url for panda scraping
    url3 = 'https://space-facts.com/mars/'
    tables = pd.read_html(url3)
    tables
    mfact_df = tables[0]
    mfact_df.columns = ['Planet Profile', 'Info']
    mfact_df.set_index('Planet Profile', inplace=True)
    html_table = mfact_df.to_html
    # Mars Hemispheres
    hemisphere_images = [{"title": "Cerberus Hemisphere", 
                      "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", 
     "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere",
     "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    {"title": "Valles Marineris Hemisphere", 
     "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"}]

