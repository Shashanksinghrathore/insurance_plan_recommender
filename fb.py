import urllib
import facebook
import requests
import json

token = 'EAADDFenkkWMBANKbZBt2tSQ3D0TjLWi1wr7iIvVkQeVy6KSz83xHSkJNC4T1JwGhi3wOvZCe72pMeQOLDP32dZB4ASIGhp4e3RBZBPT2xN9VUCiZBacOvsjdBa6KEMLc0OXjvEe0XMqQWSo4mMjA9mOCQA0IcMFWdUZCtvegytdAJeeVl5ngW8uOZBcCkzeHyMZD'

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
   return myposts


def get_user_details():
   #graph api does not allow to access all fields at once...so you have to list the fields you require!
   user = graph.get_object('me',fields='name,id,email,education,friends,age_range,birthday')
   name = graph.get_object('me',fields='name')
   id = graph.get_object('me',fields='id')
   print "Name -" ,name
   print "Id - ",id

   email = graph.get_object('me',fields='email')
   print "Email - ",email

   education = graph.get_object('me',fields='education')
   print "Education - ",education

   age_range = graph.get_object('me',fields='age_range')
   print "Age Range - ",age_range

   birthday = graph.get_object('me',fields='birthday')
   print "Birthday - ",birthday

   about = graph.get_object('me',fields='about')
   print "About - ",about

   address = graph.get_object('me',fields='address')
   print "Address - ",address

   work = graph.get_object('me',fields='work')
   print "Work Places - ",work

   relationsip_status = graph.get_object('me',fields='relationship_status')
   print "Relationship Status - ",relationsip_status

   tagged_places = graph.get_object('me',fields='tagged_places{created_id, place}')
   print "Tagged Places - ",tagged_places

   gender = graph.get_object('me',fields='gender')
   print "Gender - ",gender

   hometown = graph.get_object('me',fields='hometown')
   print "Hometown - ",hometown

   location = graph.get_object('me',fields='location')
   print "Location - ",location

   return user

url = "https://graph.facebook.com/me?access_token=EAADDFenkkWMBAMBJgKl7ZBYPSP7AyIYG3iDcrOZAv5aq2sqNCmYaZCye5aaATaPPD65nK5dJzEL3aWIU2hv5EhS4y0FUpiKG5QNoL76keSjAgHfIoZAwtaeasWXQSkuwxiY5RLTShD68AFZCMCQjTZAn2ZAR26jxzTM3uduMYTPpFZBvYJmq0sI3peenCnuFfTsZD"

response = urllib.urlopen(url)
uid = json.loads(response.read())
#print uid

user = get_user_details()
