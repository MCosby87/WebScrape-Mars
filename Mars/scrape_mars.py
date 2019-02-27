{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pymongo\n",
    "from bs4 import BeautifulSoup\n",
    "from splinter import Browser\n",
    "import datetime as dt\n",
    "import time\n",
    "import requests\n",
    "import os\n",
    "import pandas as pd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "!which chromedriver\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': '/usr/local/bin/chromedriver'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = \"https://mars.nasa.gov/news/\"\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "html= browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "mars_article = soup.find(\"div\", class_= \"list_text\")\n",
    "news_title = mars_article.find(\"div\", class_= \"content_title\").text\n",
    "news_p = mars_article.find(\"div\", class_= \"article_teaser_body\").text\n",
    "print(news_title)\n",
    "print(news_p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "image_url = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "browser.visit(image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "html2 = browser.html\n",
    "soup = BeautifulSoup(html2, 'html.parser')\n",
    "image = soup.find(\"img\", class_=\"thumb\")[\"src\"]\n",
    "img = \"https://jpl.nasa.gov\"+image\n",
    "print(img)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "twitter_url =\"https://twitter.com/marswxreport?lang=en\"\n",
    "browser.visit(twitter_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "html3 = browser.html\n",
    "soup= BeautifulSoup(html3, 'html.parser')\n",
    "tweet = soup.find(\"p\", class_=\"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text\").text\n",
    "print(tweet)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "facts_url = \"https://space-facts.com/mars/\"\n",
    "facts = pd.read_html(facts_url)\n",
    "facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "facts_df = facts[0]\n",
    "facts_df.columns = [\"Entities\", \"Measurements\"]\n",
    "facts_df.set_index([\"Entities\"])\n",
    "facts_string = facts_df.to_html()\n",
    "print(facts_string)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "hem_url = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "browser.visit(hem_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "html4 = browser.html\n",
    "soup = BeautifulSoup(html4, 'html.parser')\n",
    "hem=[]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range (4):\n",
    "    time.sleep(5)\n",
    "    images = browser.find_by_tag('h3')\n",
    "    images[i].click()\n",
    "    html4 = browser.html\n",
    "    soup = BeautifulSoup(html4, 'html.parser')\n",
    "    partial = soup.find(\"img\", class_=\"wide-image\")[\"src\"]\n",
    "    img_title = soup.find(\"h2\",class_=\"title\").text\n",
    "    img_url = 'https://astrogeology.usgs.gov'+ partial\n",
    "    dictionary={\"title\":img_title,\"img_url\":img_url}\n",
    "    hem.append(dictionary)\n",
    "    browser.back()\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(hem)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
