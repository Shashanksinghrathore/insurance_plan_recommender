import tweepy
import csv
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler


import urllib
import facebook
import requests
import json
#import csv


from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage


from lxml import html, etree
#import requests
import re
import os
import sys
import unicodecsv as csv
import argparse
#import json

import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import xgboost as xgb


consumer_key = "d3OjrMvopgLYQVz09N2SDrqLa"
consumer_secret = "68fNEgmlIEfZCqkOVv2EGwAm8Kpunkxh6HgHwYrKm4zHdwhn4R"
access_key = "976133803226869760-e5w54HPlOu133IGqoMUZDsvhneazNOm"
access_secret = "MKrnc0JkuqEKRxpjBYb8sHuLiZLW3Bt9rPx2hk6n59toh"

auth = OAuthHandler(consumer_key,consumer_secret)
api = tweepy.API(auth)
auth.set_access_token(access_key,access_secret)

class tweetListener(StreamListener):

    def on_data(self,data):
        print data
        return True
    def on_error(self,status):
        print status

api = tweepy.API(auth)
twitterStream = Stream(auth,tweetListener())
sname = "linkinpark"
#takehandle = api.user_timeline(screen_name = sname)
#test = api.users.lookup(screen_name=sname) 
test = api.lookup_users(user_ids=["#twiter_user_id"])
for user in test:
    print user.screen_name
    print user.name
    print user.description
    print user.followers_count
    print user.statuses_count
    print user.url
    print user.location
    print user.created_at
    print user.geo_enabled
    print user.verified
    print user.time_zone
    


def get_all_tweets(screen_name, tcount):
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    ntweets = 200
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0 and  ntweets < tcount:
        print "getting tweets before %s" % (oldest)
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        ntweets = ntweets + 200
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        
        print "...%s tweets downloaded so far" % (len(alltweets))
    
    #transform the tweepy tweets into a 2D array that will populate the csv    
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"),tweet.retweet_count,tweet.favorite_count,tweet.coordinates, tweet.geo, tweet.lang, tweet.place, tweet.retweet_count, tweet.source] for tweet in alltweets]
    
    #write the csv    
    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text","retweet_count","favorite_count","coordinates","geo","lang","place","retweet_count", "source"])
        writer.writerows(outtweets)
        print "Write Completed."
    pass


if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("linkinpark",200)
    # Define these once; use them twice!
    strFrom = 'helloworld.sup13@gmail.com'
    strTo = 'gkranthi.kiran.99@gmail.com'

    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'test message'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)

    # We reference the image in the IMG SRC attribute by the ID we give it below
    msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>Nifty!', 'html')
    msgAlternative.attach(msgText)

    # This example assumes the image is in the current directory
    fp = open('image.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    # Send the email (this example assumes SMTP authentication is required)
    import smtplib
    #smtp = smtplib.SMTP()
    #smtp.connect('smtp.gmail.com',587)
    #mail = smtplib.SMTP('smtp.gmail.com', 587)
    #smtp.login('helloworld.sup13@gmail.com', 'imfinehbu')
    #smtp.sendmail(strFrom, strTo, msgRoot.as_string())
    #smtp.quit()


    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login('helloworld.sup13@gmail.com', 'imfinehbu')
    mail.sendmail(strFrom, strTo, msgRoot.as_string())
    mail.quit()




    token = 'EAADDFenkkWMBAEMi5HZAWB88R6qcPVvgdZCXFOxJZBh61EhTvoxskFQZAo3cjWGIFocZAgK0deewLMvFd3KCgkilVziuqEE2q86wHyjJx14C3S3KZCJOXD2ZBikrDyDtnPB3AWJvW2RdW8FMu1w3RLiiDNU7hWZCsLYZD'

    graph = facebook.GraphAPI(access_token=token, version=2.7)


    def get_all_pages(posts):
       allposts=[]
       allposts = posts['data']
       while(1):
          try:
             next_page_url=posts['paging']['next']  #get url for next page
          except KeyError:
             break
          posts = requests.get(next_page_url).json()
          allposts += posts['data']
       return allposts
       


    def get_post_likes(post):
       mylikes=[]
       try:
         likes=graph.get_connections(post['id'],"likes")
         mylikes = get_all_pages(likes)
       except:
         pass 
       return mylikes


    def get_liked_pages():
       mypages=[]
       pages = graph.get_connections('me',connection_name='likes')
       mypages = get_all_pages(pages)
       return mypages

    def get_user_posts():
       myposts=[]

       #get my posts on page 1
       posts = graph.get_connections('me',connection_name='posts')
       #visit all pages
       myposts = get_all_pages(posts)
       H1 = []
       for n in range(150):
           row = []
           row.append(myposts[n]["id"])
           row.append(myposts[n]["created_time"])
           try:
              row.append(myposts[n]["message"])
           except KeyError:
              #row.append(myposts[n]["story"])
              share = "_Shared_story/link"
              row.append(unicode(share,"utf-8"))
           H1.append(row)
       for m in range(20):
           for n in range(3):
               print H1[m][n]
           print "\n"
       '''
       for m in range(10):
          post_ids = []
          post_ids = H1[m][0]
          post_created_time = []
          post_created_time = H1[m][1]
          post_message = []
          post_message = unicode(H1[m][2],"utf-8")
       '''
       #p.agent_info = u' '.join((agent_contact, agent_telno)).encode('utf-8')
       
       with open('user_fb_posts.csv','wb') as f:
          writer = csv.writer(f)
          writer.writerow(["id","created_time","message"])
          for m in range(150):
             item = H1[m][2].encode("utf-8")
             row = [H1[m][0],H1[m][1],item]#   str(H1[m][0]),str(H1[m][1])
             writer.writerow(row)
          print "Write Completed.3"
       pass
       '''
       print type(H1[2][2])
       item = H1[2][2].encode("utf-8")
       print item
       '''
       return myposts


    def get_user_details():
       #graph api does not allow to access all fields at once...so you have to list the fields you require!
       user = graph.get_object('me',fields='name,id,email,education,friends,age_range,birthday')
       name = graph.get_object('me',fields='name')
       id = graph.get_object('me',fields='id')
       name = name["name"]
       print "Name -" ,name
       id = id["id"]
       print "Id - ",id

       email = graph.get_object('me',fields='email')
       email = email["email"]
       print "Email - ",email

       '''
       I've not parsed this as this is none of my concern rn. :)
       #PARSE THIS!!
       education = graph.get_object('me',fields='education')
       education = education["education"]
       print "Education - ",education
       '''
       
       age_range = graph.get_object('me',fields='age_range')
       age_range_max = int(age_range["age_range"]["max"])
       age_range_min = int(age_range["age_range"]["min"])
       age_avg = (int(age_range["age_range"]["max"]) + int(age_range["age_range"]["min"]))/2
       print "Estimated Age - ",age_avg
       
       birthday = graph.get_object('me',fields='birthday')
       birthday = birthday["birthday"]
       print "Birthday - ",birthday

       about = graph.get_object('me',fields='about')
       about = about["about"]
       print "About - ",about

       #Check permission for this - 
       #address = graph.get_object('me',fields='address')
       #address = address["address"]
       #print "Address - ",address

       work = graph.get_object('me',fields='work')
       work_position = work["work"][0]["position"]["name"]
       work_location = work["work"][0]["location"]["name"]
       work_start_date = work["work"][0]["start_date"]
       work_employer = work["work"][0]["employer"]["name"]
       print "Work Details - \n"
       print "Work Place - ",work_employer
       print "Work Position - ",work_position
       print "Work StartDate - ",work_start_date
       print "Work Location - ",work_location
       
       #DONE - 
       relationship_status = graph.get_object('me',fields='relationship_status')
       relationship_status = relationship_status["relationship_status"]
       print "Relationship Status - ",relationship_status
          
       tagged_places = graph.get_object('me',fields='tagged_places')
       tagged_data = tagged_places["tagged_places"]["data"]
       #Store the ids in an array and iterate using for loop
          
       H0 = []
       for n in range(8):
          row = []
          row.append(tagged_data[n]["id"])
          row.append(tagged_data[n]["created_time"])
          row.append(tagged_data[n]["place"]["name"])
          row.append(tagged_data[n]["place"]["location"]["latitude"])
          row.append(tagged_data[n]["place"]["location"]["longitude"])
          row.append(tagged_data[n]["place"]["location"]["city"])
          row.append(tagged_data[n]["place"]["location"]["zip"])
          row.append(tagged_data[n]["place"]["location"]["country"])
          H0.append(row)
       for m in range(8):
          for n in range(8):
             print H0[m][n]
          print "\n"
          for m in range(8):
             tagged_places_ids = []
             tagged_places_ids = H0[m][0]
             tagged_places_created_time = []
             tagged_places_created_time = H0[m][1]
             tagged_places_name = []
             tagged_places_name = H0[m][2]
             tagged_places_location = []
             tagged_places_location = str(H0[m][3])+ "," + str(H0[m][4])
             tagged_places_city = []
             tagged_places_city = H0[m][5]
             tagged_places_zip = []
             tagged_places_zip = H0[m][6]
             tagged_places_country = []
             tagged_places_country = H0[m][7]

          
       gender = graph.get_object('me',fields='gender')
       gender = gender["gender"]
       print "Gender - ",gender

       hometown = graph.get_object('me',fields='hometown')
       hometown = hometown["hometown"]["name"]
       print "Hometown - ",hometown
       
       location = graph.get_object('me',fields='location')
       location = location["location"]["name"]
       print "Location - ",location
       
       details = [name,id,email,age_avg,birthday,about,work_position,work_location,work_start_date,work_employer,relationship_status,tagged_data,gender,hometown,location]#,education,address
       with open('user_fb_details.csv','wb') as f:
          writer = csv.writer(f)
          writer.writerow(["name","id","email","estimated_age","birthday","about","work_position","work_locaiton","work_start_date","work_employer","relationship_status","tagged_places","gender","hometown","location"])#,"education","address"
          writer.writerow(details)
          print "Write Completed.1"
       pass

       with open('user_fb_tagged_places.csv','wb') as f:
          writer = csv.writer(f)
          writer.writerow(["id","date_time","place_name","latitude","longitude","place_city","place_zip","place_country"])
          writer.writerows(H0)
          print "Write Completed.2"
       pass
       
       return user

    url = "https://graph.facebook.com/me?access_token=EAADDFenkkWMBAMBJgKl7ZBYPSP7AyIYG3iDcrOZAv5aq2sqNCmYaZCye5aaATaPPD65nK5dJzEL3aWIU2hv5EhS4y0FUpiKG5QNoL76keSjAgHfIoZAwtaeasWXQSkuwxiY5RLTShD68AFZCMCQjTZAn2ZAR26jxzTM3uduMYTPpFZBvYJmq0sI3peenCnuFfTsZD"

    response = urllib.urlopen(url)
    uid = json.loads(response.read())
    #print "User ID - ",uid

    print "User Details - "
    user_details = get_user_details()
    print "User Posts(150 limit)"
    user_posts_info = get_user_posts()



    def parse(keyword, place):

            headers = {	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                                    'accept-encoding': 'gzip, deflate, sdch, br',
                                    'accept-language': 'en-GB,en-US;q=0.8,en;q=0.6',
                                    'referer': 'https://www.glassdoor.com/',
                                    'upgrade-insecure-requests': '1',
                                    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36',
                                    'Cache-Control': 'no-cache',
                                    'Connection': 'keep-alive'
            }

            location_headers = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.01',
                    'accept-encoding': 'gzip, deflate, sdch, br',
                    'accept-language': 'en-GB,en-US;q=0.8,en;q=0.6',
                    'referer': 'https://www.glassdoor.com/',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36',
                    'Cache-Control': 'no-cache',
                    'Connection': 'keep-alive'
            }
            data = {"term": place,
                            "maxLocationsToReturn": 10}

            location_url = "https://www.glassdoor.co.in/findPopularLocationAjax.htm?"
            try:
                    # Getting location id for search location
                    print("Fetching location details")
                    location_response = requests.post(location_url, headers=location_headers, data=data).json()
                    place_id = location_response[0]['locationId']
                    job_litsting_url = 'https://www.glassdoor.com/Job/jobs.htm'
                    # Form data to get job results
                    data = {
                            'clickSource': 'searchBtn',
                            'sc.keyword': keyword,
                            'locT': 'C',
                            'locId': place_id,
                            'jobType': ''
                    }

                    job_listings = []
                    if place_id:
                            response = requests.post(job_litsting_url, headers=headers, data=data)
                            # extracting data from
                            # https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=true&clickSource=searchBtn&typedKeyword=andr&sc.keyword=android+developer&locT=C&locId=1146821&jobType=
                            parser = html.fromstring(response.text)
                            # Making absolute url 
                            base_url = "https://www.glassdoor.com"
                            parser.make_links_absolute(base_url)

                            XPATH_ALL_JOB = '//li[@class="jl"]'
                            XPATH_NAME = './/a/text()'
                            XPATH_JOB_URL = './/a/@href'
                            XPATH_LOC = './/span[@class="subtle loc"]/text()'
                            XPATH_COMPANY = './/div[@class="flexbox empLoc"]/div/text()'
                            XPATH_SALARY = './/span[@class="green small"]/text()'

                            listings = parser.xpath(XPATH_ALL_JOB)
                            for job in listings:
                                    raw_job_name = job.xpath(XPATH_NAME)
                                    raw_job_url = job.xpath(XPATH_JOB_URL)
                                    raw_lob_loc = job.xpath(XPATH_LOC)
                                    raw_company = job.xpath(XPATH_COMPANY)
                                    raw_salary = job.xpath(XPATH_SALARY)

                                    # Cleaning data
                                    job_name = ''.join(raw_job_name).strip('–') if raw_job_name else None
                                    job_location = ''.join(raw_lob_loc) if raw_lob_loc else None
                                    raw_state = re.findall(",\s?(.*)\s?", job_location)
                                    state = ''.join(raw_state).strip()
                                    raw_city = job_location.replace(state, '')
                                    city = raw_city.replace(',', '').strip()
                                    company = ''.join(raw_company).replace('–','')
                                    salary = ''.join(raw_salary).strip()
                                    job_url = raw_job_url[0] if raw_job_url else None

                                    jobs = {
                                            "Name": job_name,
                                            "Company": company,
                                            "State": state,
                                            "City": city,
                                            "Salary": salary,
                                            "Location": job_location,
                                            "Url": job_url
                                    }
                                    job_listings.append(jobs)

                            return job_listings
                    else:
                            print("location id not available")

            except:
                    print("Failed to load locations")    


    print("Fetching job details")
            scraped_data = parse(keyword, place)
            print("Writing data to output file")

            with open('%s-%s-job-results.csv' % (keyword, place), 'wb')as csvfile:
                    fieldnames = ['Name', 'Company', 'State',
                                              'City', 'Salary', 'Location', 'Url']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,quoting=csv.QUOTE_ALL)
                    writer.writeheader()
                    if scraped_data:
                            for data in scraped_data:
                                    writer.writerow(data)
                    else:
                            print("Your search for %s, in %s does not match any jobs"%(keyword,place))


    model = pickle.load(open("model.dat","rb"))
    #Here the test array will have variables from the data mined through social media sites like Facebook, Twitter, Glassdoor
    #test = [age,salary,gender,relationship_status,education,employment_status] #one hot coding
    #test = [51,331751,male,married,g,unemployed]
    test = [51,331751,0,1,1,0,0,0,1,0,0,0,1]

    pred = model.predict(test)
    result_var = y_pred[0]
    with open('model_result.txt', 'w') as f:
        f.write(result_var.astype(str))
    
    #pickle.dump(fin_model, open("model.dat","wb"),protocol=2)
    
