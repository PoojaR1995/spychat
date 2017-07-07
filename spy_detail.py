# import statement for datetime module
from datetime import datetime



# class is created for removing the complication of list and dictonary
class Spy:


    # constructor
    def __init__(self, name, st, age, rating):

        self.name = name

        self.st = st

        self.age = age

        self.rating = rating

        self.is_online = True

        self.chats = []

        self.current_status_message = None

        self.updated_status_msg = None




# function created for showing messages of older chats
class ShowMessage:

    def __init__(self,message,sent_by_me):

        self.message = message

        #now is used for timestamping and it takes system`s current time as a initial input
        self.time = datetime.now()

        self.sent_by_me = sent_by_me




# spy itself

spy = Spy('jack sparrow', 'Mr.', 22, 5.6)




# friends added to the list of spy`s friend by simple command
friend_1 = Spy("james bond", 'Ms.', 5.0, 24)
friend_2 = Spy('george', 'Ms.', 6.5, 25)
friend_3 = Spy('john', 'Mr.', 6.8, 21)
friend_4 = Spy('carter', 'Mr.', 6.4, 32)




# list of spy`s friends

friends = [friend_1, friend_2, friend_3,friend_4]