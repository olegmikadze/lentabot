from bs4 import BeautifulSoup
import requests
import schedule
import time
import datetime

newslink=''
reviewlink=''
articlelink=''
videolink=''
blogslink=''


def newscrawling():
    '''
    Args: website_link = string; link of website to be crawled
          link_class = string; class name for job link on website
    Returns: jobs_link = list; list of jobs
    '''

    # get content of website and parse it
    website_request = requests.get('https://itc.ua/news', timeout=5)

    website_content = BeautifulSoup(website_request.content, 'html.parser')
    # extract job description
    jobs_link = website_content.find_all(class_ = 'thumb-responsive')

   
    
    global newslink
    if newslink != jobs_link[0]['href']:
        parameters = {'chat_id': '230618475', 'text': jobs_link[0]['href']}
        message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)
        newslink = jobs_link[0]['href']
        return jobs_link[0]['href']


def reviewcrawling():
    '''
    Args: website_link = string; link of website to be crawled
          link_class = string; class name for job link on website
    Returns: jobs_link = list; list of jobs
    '''

    # get content of website and parse it
    website_request = requests.get('https://itc.ua/articles', timeout=5)

    website_content = BeautifulSoup(website_request.content, 'html.parser')
    # extract job description
    jobs_link = website_content.find_all(class_ = 'thumb-responsive')

   
    
    global reviewlink
    if reviewlink != jobs_link[0]['href']:
        parameters = {'chat_id': '230618475', 'text': jobs_link[0]['href']}
        message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)
        reviewlink = jobs_link[0]['href']
        return jobs_link[0]['href']

def articlecrawling():
    '''
    Args: website_link = string; link of website to be crawled
          link_class = string; class name for job link on website
    Returns: jobs_link = list; list of jobs
    '''

    # get content of website and parse it
    website_request = requests.get('https://itc.ua/stati', timeout=5)

    website_content = BeautifulSoup(website_request.content, 'html.parser')
    # extract job description
    jobs_link = website_content.find_all(class_ = 'thumb-responsive')

   
   
    global articlelink
    if articlelink != jobs_link[0]['href']:
        parameters = {'chat_id': '230618475', 'text': jobs_link[0]['href']}
        message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)
        articlelink = jobs_link[0]['href']
        return jobs_link[0]['href']


def videocrawling():
    '''
    Args: website_link = string; link of website to be crawled
          link_class = string; class name for job link on website
    Returns: jobs_link = list; list of jobs
    '''

    # get content of website and parse it
    website_request = requests.get('https://itc.ua/video', timeout=5)

    website_content = BeautifulSoup(website_request.content, 'html.parser')
    # extract job description
    jobs_link = website_content.find_all(class_ = 'thumb-responsive')

   
   
    global videolink
    if videolink != jobs_link[0]['href']:
        parameters = {'chat_id': '230618475', 'text': jobs_link[0]['href']}
        message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)
        videolink = jobs_link[0]['href']
        return jobs_link[0]['href']

def blogcrawling():
    '''
    Args: website_link = string; link of website to be crawled
          link_class = string; class name for job link on website
    Returns: jobs_link = list; list of jobs
    '''

    # get content of website and parse it
    website_request = requests.get('https://itc.ua/blogs', timeout=5)

    website_content = BeautifulSoup(website_request.content, 'html.parser')
    # extract job description
    jobs_link = website_content.find_all(class_ = 'thumb-responsive')

   
   
    global blogslink
    if blogslink != jobs_link[0]['href']:
        blogslink = jobs_link[0]['href']
        parameters = {'chat_id': '230618475', 'text': jobs_link[0]['href']}
        message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)
        return jobs_link[0]['href']



def send_message():
    '''
    Takes the chat id of a telegram bot and the text that was  crawled from the
    website and sends it to the bot
    Args: chat_id = string; chat id of the telegram bot, 
          text = string; crawled text to be sent
    Returns: None
    '''
    parameters = {'chat_id': '230618475', 'text': "HIIII"}
    message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)

schedule.every(1).second.do(newscrawling)
schedule.every(1).second.do(reviewcrawling)
schedule.every(1).second.do(articlecrawling)
schedule.every(1).second.do(videocrawling)
schedule.every(1).second.do(blogcrawling)



while True:
    schedule.run_pending()
    time.sleep(1)
