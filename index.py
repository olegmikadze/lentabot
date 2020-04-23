from bs4 import BeautifulSoup
import requests
import schedule
import time
import datetime
import praw
import pandas as pd
import re
from pymongo import MongoClient
from telethon import TelegramClient, events
from telethon.tl.custom.chatgetter import ChatGetter
import asyncio
import os
# class for link in twitter css-1dbjc4n r-my5ep6 r-qklmqi r-1adg3ll ``

# Use your own values from my.telegram.org
api_id = 1351607
api_hash = '78482690f0761d1396e013a98c93e7b8'
telegramclient = TelegramClient(os.path.abspath('login.session'), api_id, api_hash).start()

#Mongo
client = MongoClient('mongodb://oleg:1@lentabotcluster-shard-00-00-ioehr.mongodb.net:27017,lentabotcluster-shard-00-01-ioehr.mongodb.net:27017,lentabotcluster-shard-00-02-ioehr.mongodb.net:27017/test?ssl=true&replicaSet=lentabotCluster-shard-0&authSource=admin&retryWrites=true&w=majority');
db = client.lentadb;
collection = db.lentacollection;




async def main():
    # get all saved telegram chanels from db
    channellinks = collection.find_one({'doc_id': 'telegramLinks'})

    # loop throw the dialogs of telegram client
    async for dialog in telegramclient.iter_dialogs():
        dialog_name = str(dialog.id)
        time = str(dialog.message.date).split('+')[0]
        if dialog.is_channel and dialog.message.message:
            # if channel exists in db
            if dialog_name in channellinks:
                if channellinks[dialog_name] != time:
                    collection.find_one_and_update({ 'doc_id': 'telegramLinks'}, { '$set': { dialog_name: time }} )
                    await dialog.message.forward_to('lentaus_bot')
            else:
                collection.find_one_and_update({ 'doc_id': 'telegramLinks'}, { '$set': { dialog_name: '' }} )



reddit = praw.Reddit(client_id='rk_SiB6rupsdbQ', \
                     client_secret='fXQ1Bw_EZCphnD9IDgGpZhy55Rs', \
                     user_agent='lentaua', \
                     username='olegsan', \
                     password='EnNbGGkG20')



def redditcrawling():
    redditlinks = collection.find_one({'doc_id': 'redditLinks'})
    for sub in reddit.user.subreddits():
        for submission in sub.new(limit=1):
            if str(submission.subreddit_name_prefixed) in redditlinks:
                if redditlinks[submission.subreddit_name_prefixed] != str(submission.created_utc):
                    collection.find_one_and_update({ 'doc_id': 'redditLinks'}, { '$set': { submission.subreddit_name_prefixed: str(submission.created_utc) }} )
                    parameters = {'chat_id': '230618475', 'text': submission.subreddit_name_prefixed + ": " + submission.title + "\n\n" + submission.selftext + "\n" + submission.url}
                    message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)
            else:
                collection.find_one_and_update({ 'doc_id': 'redditLinks'}, { '$set': { submission.subreddit_name_prefixed: '' }} )


def newscrawling():
    '''
    Args: website_link = string; link of website to be crawled
          link_class = string; class name for job link on website
    Returns: jobs_link = list; list of jobs
    '''
    newslink = collection.find_one({ "newsLink": { "$exists": True } })['newsLink']

    # get content of website and parse it
    website_request = requests.get('https://itc.ua/news', timeout=5)

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

    # global newslink
    if newslink != templink:
        collection.update_one({'newsLink': newslink}, {"$set": {'newsLink': templink}})
        parameters = {'chat_id': '230618475', 'text': msgtext + "\n" + templink}
        message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)


def reviewcrawling():
    '''
    Args: website_link = string; link of website to be crawled
          link_class = string; class name for job link on website
    Returns: jobs_link = list; list of jobs
    '''
    reviewlink = collection.find_one({ "reviewsLink": { "$exists": True } })['reviewsLink']

    # get content of website and parse it
    website_request = requests.get('https://itc.ua/articles', timeout=5)

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

    if reviewlink != templink:
        collection.update_one({'reviewsLink': reviewlink}, {"$set": {'reviewsLink': templink}})
        parameters = {'chat_id': '230618475', 'text': msgtext + "\n" + templink}
        message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)


def articlecrawling():
    '''
    Args: website_link = string; link of website to be crawled
          link_class = string; class name for job link on website
    Returns: jobs_link = list; list of jobs
    '''
    articlelink = collection.find_one({ "articleLink": { "$exists": True } })['articleLink']

    # get content of website and parse it
    website_request = requests.get('https://itc.ua/stati', timeout=5)

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

    if articlelink != templink:
        collection.update_one({'articleLink': articlelink}, {"$set": {'articleLink': templink}})
        parameters = {'chat_id': '230618475', 'text': msgtext + "\n" + templink}
        message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)



def videocrawling():
    '''
    Args: website_link = string; link of website to be crawled
          link_class = string; class name for job link on website
    Returns: jobs_link = list; list of jobs
    '''
    videolink = collection.find_one({ "videoLink": { "$exists": True } })['videoLink']

    # get content of website and parse it
    website_request = requests.get('https://itc.ua/video', timeout=5)

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

    if videolink != templink:
        collection.update_one({'videoLink': videolink}, {"$set": {'videoLink': templink}})
        parameters = {'chat_id': '230618475', 'text': msgtext + "\n" + templink}
        message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)


def blogcrawling():
    '''
    Args: website_link = string; link of website to be crawled
          link_class = string; class name for job link on website
    Returns: jobs_link = list; list of jobs
    '''
    blogslink = collection.find_one({ "blogsLink": { "$exists": True } })['blogsLink']
   
    # get content of website and parse it
    website_request = requests.get('https://itc.ua/blogs', timeout=5)

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

    if blogslink != templink:
        collection.update_one({'blogsLink': blogslink}, {"$set": {'blogsLink': templink}})
        parameters = {'chat_id': '230618475', 'text': msgtext + "\n" + templink}
        message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)


# schedule.every(1).second.do(aincrawler)

# def aincrawler():
#     '''
#     Args: website_link = string; link of website to be crawled
#           link_class = string; class name for job link on website
#     Returns: jobs_link = list; list of jobs
#     '''
#     ainlink = collection.find_one({ "ainLink": { "$exists": True } })['ainLink']

#     # get content of website and parse it
#     website_request = requests.get('https://ain.ua/post-list/', timeout=5)
#     website_content = BeautifulSoup(website_request.content, 'html.parser')
#     # extract job description
#     jobs_link = website_content.find_all(class_ = 'post-link')

#     if len(jobs_link) > 1:
#         print(jobs_link)
#         if ainlink != jobs_link[0]['href']:
#             collection.update_one({'ainLink': ainlink}, {"$set": {'ainLink': jobs_link[0]['href']}})
#             parameters = {'chat_id': '230618475', 'text': jobs_link[0].contents[0] + "\n" + jobs_link[0]['href']}
#             message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)


# schedule.every(1).second.do(minfincrawler)

# def minfincrawler():
#     '''
#     Args: website_link = string; link of website to be crawled
#           link_class = string; class name for job link on website
#     Returns: jobs_link = list; list of jobs
#     '''
#     minfinlink = collection.find_one({ "minfinLink": { "$exists": True } })['minfinLink']

#     # get content of website and parse it
#     website_request = requests.get('https://minfin.com.ua/ua/news/', timeout=5)
#     website_content = BeautifulSoup(website_request.content, 'html.parser')

#     jobs_link = website_content.find_all(class_ = 'item')

#     if minfinlink != jobs_link[0].contents[3].contents[1]['href']:
#         collection.update_one({'minfinLink': minfinlink}, {"$set": {'minfinLink': jobs_link[0].contents[3].contents[1]['href']}})
#         parameters = {'chat_id': '230618475', 'text': jobs_link[0].contents[3].contents[1].text + "\n" + 'https://minfin.com.ua'+jobs_link[0].contents[3].contents[1]['href']}
#         message = requests.post('https://api.telegram.org/bot1141601443:AAFu7u3KED3498Qa7XUlFWhXosCNA7qOMeU/sendMessage', data=parameters)


def runtele():
    with client:
        telegramclient.loop.run_until_complete(main())

schedule.every(1).second.do(newscrawling)
schedule.every(1).second.do(reviewcrawling)
schedule.every(1).second.do(articlecrawling)
schedule.every(1).second.do(videocrawling)
schedule.every(1).second.do(blogcrawling)
schedule.every(1).second.do(redditcrawling)
schedule.every(1).second.do(runtele)



# loop = asyncio.get_event_loop()
# loop.create_task(main())

while True:
    try:
        schedule.run_pending()

    except Exception as inst:
        print(type(inst), inst.args, inst)



