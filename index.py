from bs4 import BeautifulSoup
import requests
import schedule
import time
import datetime
import praw
import pandas as pd
import re



newslink=''
reviewlink=''
articlelink=''
videolink=''
blogslink=''
ainlink = ''
              
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


    if len(jobs_link[0].contents) > 1:
        templink = jobs_link[0].contents[1]['href']
        msgtext =  jobs_link[0].contents[1].contents[0] + "\n" + textpost[0].contents[0]
    else:
        templink = jobs_link[0].contents[0]['href']
        msgtext =  jobs_link[0].contents[0].contents[0] + "\n" + textpost[0].contents[0]

    global newslink
    if newslink != templink:
        newslink = templink
        parameters = {'chat_id': '230618475', 'text': msgtext + "\n" + newslink}
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
    
    if len(jobs_link[0].contents) > 1:
        templink = jobs_link[0].contents[1]['href']
        msgtext =  jobs_link[0].contents[1].contents[0] + "\n" + textpost[0].contents[0]
    else:
        templink = jobs_link[0].contents[0]['href']
        msgtext =  jobs_link[0].contents[0].contents[0] + "\n" + textpost[0].contents[0]

    global reviewlink
    if reviewlink != templink:
        reviewlink = templink
        parameters = {'chat_id': '230618475', 'text': msgtext + "\n" + reviewlink} 
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
    
    if len(jobs_link[0].contents) > 1:
        templink = jobs_link[0].contents[1]['href']
        msgtext =  jobs_link[0].contents[1].contents[0] + "\n" + textpost[0].contents[0]
    else:
        templink = jobs_link[0].contents[0]['href']
        msgtext =  jobs_link[0].contents[0].contents[0] + "\n" + textpost[0].contents[0]

    global articlelink
    if articlelink != templink:
        articlelink = templink
        parameters = {'chat_id': '230618475', 'text': msgtext + "\n" + articlelink}
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
    
    if len(jobs_link[0].contents) > 1:
        templink = jobs_link[0].contents[1]['href']
        msgtext =  jobs_link[0].contents[1].contents[0] + "\n" + textpost[0].contents[0]
    else:
        templink = jobs_link[0].contents[0]['href']
        msgtext =  jobs_link[0].contents[0].contents[0] + "\n" + textpost[0].contents[0]

    global videolink
    if videolink != templink:
        videolink = templink
        parameters = {'chat_id': '230618475', 'text': msgtext + "\n" + videolink}
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
   
    if len(jobs_link[0].contents) > 1:
        templink = jobs_link[0].contents[1]['href']
        msgtext =  jobs_link[0].contents[1].contents[0] + "\n" + textpost[0].contents[0]
    else:
        templink = jobs_link[0].contents[0]['href']
        msgtext =  jobs_link[0].contents[0].contents[0] + "\n" + textpost[0].contents[0]

    global blogslink
    if blogslink != templink:
        blogslink = templink
        parameters = {'chat_id': '230618475', 'text': msgtext + "\n" + blogslink}
        message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)



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

schedule.every(1).second.do(aincrawler)

while True:
    schedule.run_pending()
    time.sleep(20)