import urllib
import facebook
import requests
import json
import csv

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
