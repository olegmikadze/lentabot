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
                parameters = {'chat_id': '230618475', 'text': "https://www.reddit.com" + submission.permalink}
                message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)
                return "https://www.reddit.com" + submission.permalink


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
    jobs_link = website_content.find_all(class_ = 'thumb-responsive')


    
    global newslink

    if newslink != jobs_link[0]['href']:
        newslink = jobs_link[0]['href']
        parameters = {'chat_id': '230618475', 'text': newslink}
        message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)
        return(newslink)


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
    jobs_link = website_content.find_all(class_ = 'thumb-responsive')

    global reviewlink
    if reviewlink != jobs_link[0]['href']:
        reviewlink = jobs_link[0]['href']
        parameters = {'chat_id': '230618475', 'text': reviewlink}
        message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)
        return reviewlink

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
    jobs_link = website_content.find_all(class_ = 'thumb-responsive')

    global articlelink
    if articlelink != jobs_link[0]['href']:
        articlelink = jobs_link[0]['href']
        parameters = {'chat_id': '230618475', 'text': articlelink}
        message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)
        return articlelink


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
    jobs_link = website_content.find_all(class_ = 'thumb-responsive')

    global videolink
    if videolink != jobs_link[0]['href']:
        videolink = jobs_link[0]['href']
        parameters = {'chat_id': '230618475', 'text': videolink}
        message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)
        return videolink

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
    jobs_link = website_content.find_all(class_ = 'thumb-responsive')

    global blogslink
    if blogslink != jobs_link[0]['href']:
        blogslink = jobs_link[0]['href']
        parameters = {'chat_id': '230618475', 'text': blogslink}
        message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)
        return blogslink

schedule.every(1).second.do(newscrawling)
schedule.every(1).second.do(reviewcrawling)
schedule.every(1).second.do(articlecrawling)
schedule.every(1).second.do(videocrawling)
schedule.every(1).second.do(blogcrawling)
schedule.every(1).second.do(redditcrawling)

while True:
    schedule.run_pending()
