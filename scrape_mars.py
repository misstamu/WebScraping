
# coding: utf-8

# In[1]:


#dependencies
from splinter import Browser
from bs4 import BeautifulSoup


# In[2]:


#excute chromedrive for windows
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# Scraping NASA Mars News

# In[3]:


#url website for scraping
url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[7]:


#loop through page to find all titles
for x in range(50):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.find_all('div', class_='content_title')
    #t_body = soup.find_all('div', class_='article_teaser_body')

    for title in titles:
        print(title.text)


    browser.click_link_by_partial_text('More')


# In[9]:


#loop through page to find all title bodies
for x in range(50):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    tbody = soup.find_all('div', class_='article_teaser_body')

    for t in tbody:
        print(t.text)


    browser.click_link_by_partial_text('More')


# JPL Mars Space Featured Image

# In[3]:


#url website for scraping
url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url2)


# In[12]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')
furl = soup.find_all('article', class_='carousel_item')
print(furl)


# In[13]:


featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA16217_ip.jpg'


# Mars Weather

# In[14]:


mars_weather = 'Sol 2047 (May 10, 2018), Sunny, high 3C/37F, low -71C/-95F, pressure at 7.33 hPa, daylight 05:22-17:20'


# Mars Facts

# In[1]:


# panda dependency
import pandas as pd


# In[2]:


# url for panda scraping
url3 = 'https://space-facts.com/mars/'


# In[3]:


tables = pd.read_html(url3)
tables


# In[7]:


mfact_df = tables[0]
mfact_df.columns = ['Planet Profile', 'Info']
mfact_df.set_index('Planet Profile', inplace=True)
mfact_df


# In[8]:


html_table = mfact_df.to_html
html_table


# Mars Hemispheres

# In[9]:


hemisphere_images = [{"title": "Cerberus Hemisphere", 
                      "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", 
     "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere",
     "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    {"title": "Valles Marineris Hemisphere", 
     "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"}]

