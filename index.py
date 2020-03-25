from bs4 import BeautifulSoup
import requests
import schedule
import time
import datetime
import praw
import pandas as pd
import re

reddit = praw.Reddit(client_id='rk_SiB6rupsdbQ', \
                     client_secret='fXQ1Bw_EZCphnD9IDgGpZhy55Rs', \
                     user_agent='lentaua', \
                     username='olegsan', \
                     password='EnNbGGkG20')

newslink=''
reviewlink=''
articlelink=''
videolink=''
blogslink=''

redditlinks = {}

def fillredditlinks():
    for sub in reddit.user.subreddits():
        for submission in sub.new(limit=1):
            redditlinks[submission.subreddit_name_prefixed] = str(submission.created_utc)
fillredditlinks()

def redditcrawling():
    for sub in reddit.user.subreddits():
        for submission in sub.new(limit=1):
            if redditlinks[submission.subreddit_name_prefixed] != str(submission.created_utc):
                redditlinks[submission.subreddit_name_prefixed] = str(submission.created_utc)
                parameters = {'chat_id': '230618475', 'text': submission.subreddit_name_prefixed + ": " + submission.title + "\n\n" + submission.selftext + "\n" + submission.url}
                message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)


def newscrawling():
    '''
    Args: website_link = string; link of website to be crawled
          link_class = string; class name for job link on website
    Returns: jobs_link = list; list of jobs
    '''

    # get content of website and parse it
    website_request = requests.get('https://itc.ua/news', timeout=1)

    website_content = BeautifulSoup(website_request.content, 'html.parser')
    # extract job description
    jobs_link = website_content.find_all(class_ = 'entry-title')
    textpost =  website_content.find_all(class_ = 'entry-excerpt')

    global newslink
    if newslink != jobs_link[0].contents[0]['href']:
        newslink = jobs_link[0].contents[0]['href']
        parameters = {'chat_id': '230618475', 'text': jobs_link[0].contents[0].contents[0] + "\n" + textpost[0].contents[0] + "\n" + newslink}
        message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)


def reviewcrawling():
    '''
    Args: website_link = string; link of website to be crawled
          link_class = string; class name for job link on website
    Returns: jobs_link = list; list of jobs
    '''

    # get content of website and parse it
    website_request = requests.get('https://itc.ua/articles', timeout=1)

    website_content = BeautifulSoup(website_request.content, 'html.parser')
    # extract job description
    jobs_link = website_content.find_all(class_ = 'entry-title')
    textpost =  website_content.find_all(class_ = 'entry-excerpt')

    global reviewlink
    if reviewlinks != jobs_link[0].contents[0]['href']:
        reviewlinks = jobs_link[0].contents[0]['href']
        parameters = {'chat_id': '230618475', 'text': jobs_link[0].contents[0].contents[0] + "\n" + textpost[0].contents[0] + "\n" + reviewlinks}
        message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)


def articlecrawling():
    '''
    Args: website_link = string; link of website to be crawled
          link_class = string; class name for job link on website
    Returns: jobs_link = list; list of jobs
    '''

    # get content of website and parse it
    website_request = requests.get('https://itc.ua/stati', timeout=1)

    website_content = BeautifulSoup(website_request.content, 'html.parser')
    # extract job description
    jobs_link = website_content.find_all(class_ = 'entry-title')
    textpost =  website_content.find_all(class_ = 'entry-excerpt')

    global articlelink
    if articlelink != jobs_link[0].contents[0]['href']:
        articlelink = jobs_link[0].contents[0]['href']
        parameters = {'chat_id': '230618475', 'text': jobs_link[0].contents[0].contents[0] + "\n" + textpost[0].contents[0] + "\n" + articlelink}
        message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)



def videocrawling():
    '''
    Args: website_link = string; link of website to be crawled
          link_class = string; class name for job link on website
    Returns: jobs_link = list; list of jobs
    '''

    # get content of website and parse it
    website_request = requests.get('https://itc.ua/video', timeout=1)

    website_content = BeautifulSoup(website_request.content, 'html.parser')
    # extract job description
    jobs_link = website_content.find_all(class_ = 'entry-title')
    textpost =  website_content.find_all(class_ = 'entry-excerpt')

    global videolink
    if videolink != jobs_link[0].contents[0]['href']:
        videolink = jobs_link[0].contents[0]['href']
        parameters = {'chat_id': '230618475', 'text': jobs_link[0].contents[0].contents[0] + "\n" + textpost[0].contents[0] + "\n" + videolink}
        message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)


def blogcrawling():
    '''
    Args: website_link = string; link of website to be crawled
          link_class = string; class name for job link on website
    Returns: jobs_link = list; list of jobs
    '''

    # get content of website and parse it
    website_request = requests.get('https://itc.ua/blogs', timeout=1)

    website_content = BeautifulSoup(website_request.content, 'html.parser')
    # extract job description
    jobs_link = website_content.find_all(class_ = 'entry-title')
    textpost =  website_content.find_all(class_ = 'entry-excerpt')

    global blogslink
    if blogslink != jobs_link[0].contents[0]['href']:
        blogslink = jobs_link[0].contents[0]['href']
        parameters = {'chat_id': '230618475', 'text': jobs_link[0].contents[0].contents[0] + "\n" + textpost[0].contents[0] + "\n" + blogslink}
        message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)

ainlink = ''

def aincrawler():
    '''
    Args: website_link = string; link of website to be crawled
          link_class = string; class name for job link on website
    Returns: jobs_link = list; list of jobs
    '''

    # get content of website and parse it
    website_request = requests.get('https://ain.ua/post-list/', timeout=1)

    website_content = BeautifulSoup(website_request.content, 'html.parser')
    # extract job description
    jobs_link = website_content.find_all(class_ = 'post-link')

    global ainlink
    if ainlink != jobs_link[0]['href']:
        ainlink = jobs_link[0]['href']
        parameters = {'chat_id': '230618475', 'text': jobs_link[0].contents[0] + "\n" + ainlink}
        message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)



schedule.every(1).second.do(newscrawling)
schedule.every(1).second.do(reviewcrawling)
schedule.every(1).second.do(articlecrawling)
schedule.every(1).second.do(videocrawling)
schedule.every(1).second.do(blogcrawling)
schedule.every(1).second.do(redditcrawling)
schedule.every(1).second.do(aincrawler)


while True:
    schedule.run_pending()
