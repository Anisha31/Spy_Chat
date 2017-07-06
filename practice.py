from datetime import datetime
#CLASS Spy for storing values of spy_user
class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

#class for keeping record of meassage and time
class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

#values of default
spy = Spy('anisha' , 'ms',21 , 4.2)
