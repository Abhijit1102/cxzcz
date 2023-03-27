from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin

import requests
import re
import os
from urllib.request import urlopen as uReq

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time



application = Flask(__name__)  # initializing a flask app
app = application

@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/review', methods=['POST']) # route to show the review comments in a web UI
@cross_origin()
def index():
    try:
        searchString = request.form['content'].replace(" ", "")
        
        options = Options()
        driver = webdriver.Firefox(options=options)
        driver.implicitly_wait(5)


        driver.get("https://www.youtube.com/@PW-Foundation/videos")
        time.sleep(5)
        allchannellist = driver.find_elements(By.CSS_SELECTOR, "a#video-title-link")
            
        urls = list(dict.fromkeys(map(lambda a : a.get_attribute("href"), allchannellist)))
        driver.quit()
        urls = urls[:5]
        driver.quit()

        thumbnails_links = []
        for url in urls:
            # Extract video ID from URL
            exp = "^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*"
            s = re.findall(exp, url)[0][-1]

            # Construct image URL
            thumbnail_url = f"https://i.ytimg.com/vi/{s}/maxresdefault.jpg"
            thumbnails_links.append(thumbnail_url)

        options = Options()
        driver = webdriver.Firefox(options=options)

        driver.implicitly_wait(5)


        driver.get("https://www.youtube.com/@PW-Foundation/videos")
        time.sleep(5)

        driver.implicitly_wait(5)


        driver.get("https://www.youtube.com/@PW-Foundation/videos")
        time.sleep(5)
        all_titles = driver.find_elements(By.CSS_SELECTOR, "a#video-title-link")
        titles = [title.get_attribute('title') for title in all_titles]
        driver.quit()
        titles= titles[:5]
        
        driver = webdriver.Firefox(options=options)

        driver.implicitly_wait(5)
        driver.get("https://www.youtube.com/@PW-Foundation/videos")
        time.sleep(5)
        allchannellist = driver.find_elements(By.CSS_SELECTOR, "span.style-scope.ytd-video-meta-block")
        views_time = list(dict.fromkeys(map(lambda a : a.get_attribute("innerHTML"), allchannellist)))
        driver.quit()
        views_time = views_time[0:11]
        views =[i  for i in views_time if i.endswith("views")]
        times = [i  for i in views_time if not i.endswith("views")]

        mydict = {"urls": urls, "thumbnails_links": thumbnails_links, 
                  "titles": titles, "views": views,
                  "time": times}
        
        return render_template('results.html', mydicts=mydict)

    except Exception as e:
        print('The Exception message is: ', e)
        return f'something is wrong: {e}'

if __name__ == "__main__":
    app.run(debug=True)
