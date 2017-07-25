#import malplotlib.pyplot as plt
import requests, urllib
from textblob import TextBlob
from keys import APP_ACCESS_TOKEN
from textblob.sentiments import NaiveBayesAnalyzer




#Token_Owner :'pooja_bharti_arya'
##Sandbox Users(if there account is public) : shiwanipahwa, jahnvee.sharma(public account)


'''
base_url used for every get or post function given by insta API

'''

BASE_URL = 'https://api.instagram.com/v1/'







'''
a: function for fetching our own details usint get function(mandatory)

'''

def self_info():


    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    # code used from the instagram api which is used for fetching data
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            # these print commands used for printing all the information regarding the user itself
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])

        else:
            print 'User does not exist!'

    else:
        print 'Status code other than 200 received!'







'''
b: function for fetching details of another user by using put function which accepts input from the user(mandatory)
'''

def get_user_id(insta_username):

    request_url =(BASE_URL +'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']

        else:
            return None
    else:
        print 'Status code other than 200 or 304 received!'
        exit()





'''
#c:function for fetching details of a user by its username(mandatory)

'''
def get_user_info(insta_username):


    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()

    # all the terms used for the url addressing or fetching
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])

        else:
            print 'There is no data for this user!'

    else:
        print 'Status code other than 200 received!'





'''
d: function for getting our own post(mandatory)

'''
def get_own_post():


    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()


    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print 'Post does not exist!'


    else:
        print 'Status code other than 200 received!'






'''
e: function for getting a recent post by another user(mandatory)

'''
def get_user_post(insta_username):


    user_id = get_user_id(insta_username)
    if user_id == None:


        print 'User does not exist!'
        exit()


    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()


    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print 'Post does not exist!'


    else:
        print 'Status code other than 200 received!'





'''
f: function for getting post_id of another user

'''

def get_post_id(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print 'There is no recent post of the user!'
            exit()
    else:
        print 'Status code other than 200 received!'
        exit()





'''
g: function for liking a post of another user by our insta_bot

'''
def like_a_post(insta_username):


    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)

    payload = {"access_token": APP_ACCESS_TOKEN}
    print 'POST request url : %s' % (request_url)

    post_a_like = requests.post(request_url, payload).json()

    if post_a_like['meta']['code'] == 200:
        print 'Like was successful!'
    else:
        print 'Your like was unsuccessful. Try again!'






'''
h: function for commenting on a another users post

'''
def post_a_comment(insta_username):


    media_id = get_post_id(insta_username)
    comment_text = raw_input("Your comment: ")

    payload = {"access_token": APP_ACCESS_TOKEN, "text" : comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)


    make_comment = requests.post(request_url, payload).json()


    if make_comment['meta']['code'] == 200:
        print "Successfully added a new comment!"
    else:
        print "Unable to add comment. Try again!"




'''
i: function for getting list of all the users who liked our post

'''
def get_like_list(insta_username):

   media_id = get_user_id(insta_username)
   request_url = (BASE_URL + 'media/%s/likes?access_token=ACCESS-TOKEN=%s') % (media_id,APP_ACCESS_TOKEN)
   print 'GET request url : %s' % (request_url)

   media_id = requests.get(request_url).json()



   if media_id['meta']['code'] == 200:

       if len(media_id['data']):
           return media_id['data'][0]['id']

       else:
           print 'There is no recent post of the user!'
           exit()

   else:
       print 'Status code other than 200 received!'
       exit()





'''
 j: (mandatory objective) getting a list of of media with a particular tag

'''


def hash_tag():
    i = 0

    tags = []

    tag_name = []

    while i < 3:

        tag = raw_input("enter the hashtag : ")

        request_url = ('https://api.instagram.com/v1/tags/%s?access_token=%s') % (tag, APP_ACCESS_TOKEN)

        tag_name.append(tag)

        print tag_name

        print 'GET request url : %s' % (request_url)

        hash_items = requests.get(request_url).json()

        if hash_items['meta']['code'] == 200:

            if len(hash_items['data']):

                print hash_items['data']['media_count']

                tags.append(hash_items['data']['media_count'])

                print tags

                i = i + 1


            else:

                print 'Status code other than 200 received!'

        else:
            exit()


def pie_chart():
    sizes = hash_tag()

    fig1, ax1 = plt.subplots()

    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

'''
delete negative comments
'''
def delete_negative_comment(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            #Here's a naive implementation of how to delete the negative comments :)
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print 'Negative comment : %s' % (comment_text)
                    delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (media_id, comment_id, APP_ACCESS_TOKEN)
                    print 'DELETE request url : %s' % (delete_url)
                    delete_info = requests.delete(delete_url).json()

                    if delete_info['meta']['code'] == 200:
                        print 'Comment successfully deleted!\n'
                    else:
                        print 'Unable to delete comment!'
                else:
                    print 'Positive comment : %s\n' % (comment_text)
        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'






'''
L: find user of your own choice or choose a post or user in very creative way
this function will allow you to search a user by its username
'''
def get_media_of_your_choice(insta_username):
    user_id =get_user_id(insta_username)
    if user_id ==None:
        print 'user does not exist'


    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
       if len(user_media['data']):
            post_number = raw_input('enter the number of post which you want:')
            post_number=int(post_number)
            x = post_number - 1
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url,image_name)
            print 'your image has been downloaded'
       else:
            print 'There is no recent post of the user!'
            exit()

    else:
        print 'Status code other than 200 received!'
        exit()


'''
m:for displaying all the comments on a post
'''
def list_of_comment(insta_username):
     list = list_of_comment(insta_username)
     print "Comments:"
     for i in list:
      print i[0]



#(main function) function for accessing all the functions created for diffenent

def start_bot():

    while True:

        print '\n'

        print 'welcome!! to our insta_bot app'

        print 'this is our menu choose any option\n'

        print "a.for self info\n"

        print "b.for getting user id of a user by username\n"

        print "c.for getting user info of a user\n"

        print "d. get the recent post our own \n"

        print "e.get recent post of a user\n"

        print "f.get media id of a user\n"

        print "g.for liking a post of a user\n"

        print "h.for making comment on the recent post of a user\n"

        print "i.for fetching a list of a comment of a user post\n"

        print "j.get a list of a tags of a particular media\n"

        print "k.Delete negative comments from the recent post of a user\n"

        print "l.choose the post of a user of your choice\n"

        print "m.for displaying all the comments on a post of a user\n"

        print "z.quit"




       #choices for the above function`s execution

        choice = raw_input("choose your option for further operations ")


        if choice == "a":

            self_info()



        elif choice == "b":

            insta_username = raw_input("Enter the username ")


            get_user_id(insta_username)



        elif choice == "c":

            insta_username = raw_input("Enter the username ")

            get_user_info(insta_username)



        elif choice == "d":

            insta_username = raw_input("owner of the access token: ")

            get_own_post()



        elif choice=="e":

           insta_username = raw_input("Enter the username of the user: ")

           get_user_post(insta_username)



        elif choice=="f":

           insta_username = raw_input("Enter the username of the user: ")

           get_post_id(insta_username)



        elif choice=="g":

           insta_username = raw_input("Enter the username of the user: ")

           like_a_post(insta_username)


        elif choice=="h":

           insta_username = raw_input("Enter the username of the user: ")

           post_a_comment(insta_username)



        elif choice=="i":

           insta_username = raw_input("Enter the username of the user: ")

           get_like_list(insta_username)



        elif choice == "j":

            insta_username = raw_input("Enter the username of the user: ")

            hash_tag()



        elif choice == "k":

            insta_username = raw_input("Enter the username of the user: ")

            delete_negative_comment(insta_username)

        elif choice == "l":

            insta_username = raw_input("Enter the username of the user: ")

            get_media_of_your_choice(insta_username)



        elif choice == "m":

            insta_username = raw_input("Enter the username of the user: ")

            list_of_comment(insta_username)



            exit()

        exit()


    else:

            print "wrong choice"


start_bot()