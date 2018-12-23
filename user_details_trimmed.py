import urllib
import facebook
import requests
import json

token = 'EAADDFenkkWMBAEMi5HZAWB88R6qcPVvgdZCXFOxJZBh61EhTvoxskFQZAo3cjWGIFocZAgK0deewLMvFd3KCgkilVziuqEE2q86wHyjJx14C3S3KZCJOXD2ZBikrDyDtnPB3AWJvW2RdW8FMu1w3RLiiDNU7hWZCsLYZD'

graph = facebook.GraphAPI(access_token=token, version=2.7)

class excp(Exception):
   def __init__(self,msg):
      self.msg = msg
   def handle1(self):
      print("error_occured")

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
          #row.append(myposts[n]["message"])
          row.append(" _Shared Story ")
       H1.append(row)
   for m in range(150):
       for n in range(3):
           print H1[m][n]
       print "\n"
       
   for m in range(150):
      post_ids = []
      post_ids = H1[m][0]
      post_created_time = []
      post_created_time = H1[m][1]
      post_message = []
      post_message = H1[m][2]
   
   return myposts

def get_all_location():
   allloc = []
   locations = graph.get_object('me',fields='tagged_places')#,fields='name,id,email,education,friends,age_range,birthday,relationship'
   
   
def get_user_details():
   #graph api does not allow to access all fields at once...so you have to list the fields you require!
   user = graph.get_object('me',fields='relationship_status')#,fields='name,id,email,education,friends,age_range,birthday,relationship'
   print user
   name = graph.get_object('me',fields='name')
   id = graph.get_object('me',fields='id')
   print "Name -" ,name["name"]
   print "Id - ",id["id"]

   #DONE - 
   relationship_status = graph.get_object('me',fields='relationship_status')
   relationship_status = relationship_status["relationship_status"]
   print "Relationship Status - ",relationship_status
   '''
   #Check permission for this - 
   address = graph.get_object('me',fields='address')
   address = address["address"]
   print "Address - ",address
   '''
   '''
   tagged_places = graph.get_object('me',fields='tagged_places')#{created_id, place}
   print tagged_places
   tagged_data = tagged_places["tagged_places"]["data"]
   print tagged_data[0]["id"],tagged_data[0]["created_time"],tagged_data[0]["place"]["location"]
   print tagged_data[7]["id"],tagged_data[7]["created_time"],tagged_data[7]["place"]["location"]
   #print tagged_data
   #Store the ids in an array and iterate using for loop
   #for n in range(15):
    #  print tagged_data[n]["id"]
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
   
   '''
   '''
   tagged_places = graph.get_object('me',fields='tagged_places')
   tagged_data = tagged_places["tagged_places"]["data"]
   #Store the ids in an array and iterate using for loop
   
   H0 = []
   for n in range(10):
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
   for m in range(10):
       for n in range(8):
           print H0[m][n]
       print "\n"
   for m in range(10):
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
   '''
   #saveFile = 
   return user
url = "https://graph.facebook.com/me?access_token=EAADDFenkkWMBAEMi5HZAWB88R6qcPVvgdZCXFOxJZBh61EhTvoxskFQZAo3cjWGIFocZAgK0deewLMvFd3KCgkilVziuqEE2q86wHyjJx14C3S3KZCJOXD2ZBikrDyDtnPB3AWJvW2RdW8FMu1w3RLiiDNU7hWZCsLYZD"

response = urllib.urlopen(url)
uid = json.loads(response.read())
#print uid

user = get_user_details()
#user_posts = get_user_posts()

