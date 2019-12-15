# Importing Dependencies
import pandas as pd
from bs4 import BeautifulSoup
import requests
import os
from splinter import Browser

def scrape():
    # Webpage to scrape url for NASA
    url_nasa = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at            +desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

    # Creating Beautiful Soup connection and output file to NASA url
    response_nasa = requests.get(url_nasa)
    soup_nasa = BeautifulSoup(response_nasa.text, 'html.parser')

    # Locating and storing html title and paragraph tags
    news_titles = soup_nasa.find_all('div', class_='content_title')
    news_paragraphs = soup_nasa.find_all('div', class_='article_teaser_body')

    # Pulls first article title and removes /n characters
    first_news_title = news_titles[0].text
    first_news_title = first_news_title.replace("\n", "")
    first_news_title

    # Pulls first article description
    # # first_news_paragraph = news_paragraphs[0].text
    # # Is empty and returns an error


    # Creatin splinter file for NASA url
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url_nasa)
    html = browser.html


    # Uses splinter and soup to search for feature image
    for x in range(1,6):

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        feature_image_url_end = soup.find('div', {'class': 'list_image'}).img['src']

    feature_image_url = 'https://mars.nasa.gov' + feature_image_url_end

    feature_image_url

    # Mars weather twitter scraping
    url_twitter = "https://twitter.com/marswxreport?lang=en"

    # Getting new connection and output file
    response_twitter = requests.get(url_twitter)
    soup_twitter = BeautifulSoup(response_twitter.text, 'html.parser')

    # Scrapes webpage for the most recent tweet about Mars weather
    mars_weather = soup_twitter.find('p', {'class': 'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text'})
    mars_weather.text

    # Mars Facts Webpage url
    url_facts = "https://space-facts.com/mars/"

    # Pandas scraping for Mars Facts url
    facts_dfs = pd.read_html(url_facts)

    # Pandas table manipulation and writing to html
    facts_df = facts_dfs[0]
    facts_df.columns = ['Variable', 'Value']
    facts_df.set_index('Variable')
    facts_html = facts_df.to_html('table.html')

    # Astrogeology webpage urls
    url_cerberus = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    url_schiaparelli = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    url_syrtis_major = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    url_valles_marineris = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'

    # Getting new connections and output files
    response_cerberus = requests.get(url_cerberus)
    soup_cerberus = BeautifulSoup(response_cerberus.text, 'html.parser')

    response_schiaparelli = requests.get(url_schiaparelli)
    soup_schiaparelli = BeautifulSoup(response_schiaparelli.text, 'html.parser')

    response_syrtis_major = requests.get(url_syrtis_major)
    soup_syrtis_major = BeautifulSoup(response_syrtis_major.text, 'html.parser')

    response_valles_marineris = requests.get(url_valles_marineris)
    soup_valles_marineris = BeautifulSoup(response_valles_marineris.text, 'html.parser')

    # Dictionaries to hold hemisphere data
    cerberus = {'title' : soup_cerberus.find('h2', {'class': 'title'}), \
                'img_url' : soup_cerberus.find('img', {'class': 'wide-image'})}
    schiaparelli = {'title' : soup_schiaparelli.find('h2', {'class': 'title'}), \
                    'img_url' : soup_schiaparelli.find('img', {'class': 'wide-image'})}
    syrtis_major = {'title' : soup_syrtis_major.find('h2', {'class': 'title'}), \
                    'img_url' : soup_syrtis_major.find('img', {'class': 'wide-image'})}
    valles_marineris = {'title' : soup_valles_marineris.find('h2', {'class': 'title'}), \
                        'img_url' : soup_valles_marineris.find('img', {'class': 'wide-image'})}

    hemisphere_image_urls = [cerberus, schiaparelli, syrtis_major, valles_marineris]
