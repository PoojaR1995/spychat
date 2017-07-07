# import statements for this app instead of creating all files in a single file
from spy_detail import spy, Spy, ShowMessage, friends

# this import is used for sending a secret message in the form of image
from steganography.steganography import Steganography

import string
from termcolor import *
import colorama



# these are the existing messages of the spy
STATUS_MESSAGES = ["hello i m spy member of this spy_club","i have miles to go"]



# welcome message
print "welcome spy! Let\'s get started"


#question asked by the spy_chat app for the spy
question = "Do you want to continue as " + spy.st + " " + spy.name + " (Y/N) "
print "Authentication complete. Welcome " + spy.name + " good to see you again"

existing = raw_input(question)





#1 this function is used for adding status and updating with the existing one
def add_status():

    # if there is no status exists
    updated_status_message = None


    # if status message is not none
    if spy.current_status_message != None:

        print "Your current status message is %s \n"% (spy.current_status_message)


    else:
        print "You don't have any status message currently \n"

    default = raw_input("select from the existing status (y/n)? ")



     # this will change the lower case letters into uppser case letters itself
    if default.upper() == "N":
        new_status_message = raw_input("What's on your mind right now ? ")

        # if user enters the valid status rather then leaving it blank
        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message


    #this default upper function is used to convert lower case letters into upper case letter as the requirments are not satisfied by the user
    elif default.upper() == "Y":

        item_position = 1


        for message in STATUS_MESSAGES:
            print "%d. %s" % (item_position, message)
            item_position = item_position + 1

        # if the user selects from existing status
        message_selection = int(raw_input("\nChoose from the above messages:  "))

         #used for the fetching the exact value and the reason is due to the zero page indexing
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print "Press y or n."



    # if your status is updated
    if updated_status_message:
        print "Your updated status is : %s" % (updated_status_message)


    # this is only a message used when user doesnot have any message for the selection
    else:
        print "you dont have any current message"

    return updated_status_message





#2 this function is used for adding a friend into your existing friends
def add_friend():


    friend = Spy('','',0,0.0)


    friend.name = raw_input("Enter your friends name : ")

    friend.st = raw_input("Mr. or Ms.: ")


    friend.name = friend.st+ " " + friend.name

    friend.age = raw_input("Age? ")

    friend.age = int(friend.age)

    friend.rating = raw_input("Spy rating ")

    friend.rating = float(friend.rating)


    # this function added to compute the length of these attributes
    if len(friend.name) > 0 and friend.age > 12 and friend.rating >= spy.rating:

        friends.append(friend)
        print "Your Friend is Added!"

    else:
        print "Invalid entery."

    # used for storing these details of the  spy friend into a list
    return len(friends)



#3 this function is used for selection of the friends from the existing list

def select_a_friend():
    item = 0

    for friend in friends:
        print "%d. %s %s of_age %d with_rating %.2f is_online" % (item +1, friend.st, friend.name, friend.age, friend.rating)
        item = item + 1

    # for selecting a friend
    friend_choice = raw_input("select a friend")


    # this statement used because the zero page indexing is used
    friend_position = int(friend_choice) - 1

    return friend_position




#4 this function is used for sending a secret message
def send_message():

     # for the selection of friend
    choose_friend = select_a_friend()


    original_image = raw_input("What is the name of the image ? ")
    output_path = "output.jpg"
    text = raw_input("input your secret message you want to send")


    # edge cases if user enters a invalid input such as blank space
    Invalidchar = set(string.punctuation.replace("_", " "))
    if any(char in Invalidchar for char in text):
        print "Invalid, The secret message should not contain spaces !"


     # when your message is ready for sending
    else:
        print "your secret message is ready and has been encoded in the image"

    # for encoding the message into that image
    Steganography.encode(original_image, output_path, text)

    new_chat = ShowMessage(text,True)

    friends[choose_friend].chats.append(new_chat)

    print "great! your message is ready"



#5 this function is used for reading all the messages from our spy friend
def read_message():

    # the friend who is sender
    message_sender = select_a_friend()

    #output path of the image
    output_path = raw_input("What is the name of the file ?")


    #for the decoding purpose of secret message
    secret_text = Steganography.decode(output_path)

    #if there is no message in it
    if len(secret_text) == 0:
        print "heh dude!! there is no message in it"


    #if any of these message is printed
    elif secret_text.upper() == "SOS" or secret_text.upper() == "Save me" or secret_text.upper()== "Need your help ":

        print "the secret message is : " + secret_text
        print "Wait ! I'll be right there rightaway !"


    else:
        print "Your secret message i.e '" +secret_text + "' has been saved !"


    new_chat = ShowMessage(secret_text, False)

    friends[message_sender].chats.append(new_chat)

    # used for splitig the words of the messages
    words= secret_text.split(" ")

    print len(words)




#6 this function is used for reding the chat history from old chats

def read_chat_history():

    # select a friend who`s chat you want to read
    read = select_a_friend()


    for message in friends[read].chats:

        if message.sent_by_me:

         cprint (message.time.strftime("%d %B %Y"), 'green')

         cprint ('You said :', 'red')

         print message.message


        else:

             cprint(message.time.strftime("%d %B %Y"), 'blue')

             cprint(friends[read].name, 'red')

             print message.message




#7 this function is used for starting chat with your friends on spy_chat app

def start_chat(spy):

    # spy_name with salutation
    spy.name = spy.st + " " + spy.name

     # this constraint is used for checking the age entered by the user is valid or not

    if spy.age > 12 and spy.age < 50:


        print "Spy authenticated. Welcome " + spy.name + " , of age: "+ str(spy.age) + " and rating : " + str(spy.rating) + ". we are happy to see you...!! !"

        show_menu = True

        # for the choices provided for the spy
        while show_menu:
            menu_choices = "What do you want to do ? \n 1. Add a status update \n 2. Add a friend \n 3. select a friend \n 4. send a secret message \n 5. Read a secret message  \n 6.read chat history from older chats  \n 7.exit application"
            menu_choice = raw_input(menu_choices)


            # choices with all functions
            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)


                if menu_choice == 1:
                    spy.current_status_message = add_status()


                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print "You have %d friends!" % (number_of_friends)


                elif menu_choice == 3:
                    select_a_friend()


                elif menu_choice == 4:
                   send_message()


                elif menu_choice == 5:
                    read_message()


                elif menu_choice == 6:
                    read_chat_history()


                else:
                    print "Invalid entry"
                    show_menu = False

    else:
        print 'you are not eligible'




if existing == "Y" or existing == "y":
    start_chat(spy)

 # if the spy is not existing one
else:

    spy = Spy('','',0,0.0)

    spy.name = raw_input("Enter a valid name: ")


    # if something is entered y the user
    if len(spy.name) > 0:

         # if user enters a special character (edge case)

         if set('[~!@#$%^&*()_+{}":;\']+$ " "').intersection(spy.name):

             print "Invalid name."

         else:
             print "Valid name!"


             spy.st = raw_input("Mr. or Ms.: ")

             spy.age = int(raw_input("What is your age ?"))

             spy.rating = float(raw_input("What is your spy rating?"))


             if spy.rating > 4.5:
                 print 'Great!! you one of the best spy!'

             elif spy.rating > 3.5 and spy.rating <= 4.5:
                 print 'You are one of the good ones'

             elif spy.rating >= 2.5 and spy.rating <= 3.5:
                 print 'You are average one'


             else:
                 print 'We need somebody to help in the office.'


             start_chat(spy)

    else:
        print 'Please add a valid spy name !'
