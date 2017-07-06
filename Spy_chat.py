from practice import spy,Spy,ChatMessage

#for encoding and decoding message inside the image
from steganography.steganography import Steganography

#for date and time
from datetime import datetime


#empty friend list
FRIENDS =[]

#default status list
STATUS_MESSAGES = ['Online','Available','Unavailable','Busy','At work','In a meeting','At the gym']

#function for  created account
def start_chat(spy):

    if spy.rating > 4.5:
        print"great ace!"
    elif spy.rating >3.5 :
        print "you are one of good ones"
    elif spy.rating >2.5 :
        print"you can always do better"
    else:
        print"we can always use somebody to help in the office"

    print "Authentication complete \n Welcome %s age: %d and rating : %.1f .Proud to be have you onboard\n" % (spy.name ,spy.age ,spy.rating)


    # loop which show the option to select
    while True:
        ch=raw_input(" Choose 1) Add a status update \n2) Add a friend \n3) Send a secret message \n4) Read a secret message \n5) Read chats from a user \n6) Close application")
        ch =int(ch)
        if(ch > 0 and ch <= 6):
            if(ch ==1):
                add_status()

            elif (ch == 2):
                n = add_friend()
                print " You have %d friends" % n
            elif (ch == 3):
                send_message()
            elif (ch == 4):
                read_message()
            elif (ch == 5):
                read_chat_history()
            elif (ch == 6):
                break
        else:
            print "wrong choice"


#function to update a status
def add_status():
    updated_status_message = None


    status = raw_input("Do you  want to \n1> choose from the older status updates  \n2> create a new status update \nSelect :")
    status = int(status)
    if status == 2:
        new_status_message = raw_input("What status message do you want to set? ")

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif status == 1:

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'
    print "Your updated status %s" % updated_status_message

#function to add a new friend
def add_friend():
    new_friend = Spy('', '', 0, 0.0)
    new_friend.name= raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")
    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = int(raw_input("Age?"))
    new_friend.rating= float(raw_input("Spy rating?"))

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        FRIENDS.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
    return len(FRIENDS)

#function to choose a friend
def select_a_friend():
    item_position = 1

    for friend in FRIENDS:
        print '%d. %s aged %d with rating %.2f is online' % (item_position , friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_position = item_position + 1

    friend = raw_input("Choose A FRIEND  from your friend List")
    friend = int(friend) - 1
    return friend

#function to send messages to selected user
def send_message():
    friend_choice = select_a_friend()
    original_image = raw_input("What is the name of the image?")
    output_path = "C:\Users\User-hp\Desktop\output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)
    new_chat = ChatMessage(text,True)
    FRIENDS[friend_choice].chats.append(new_chat)
    print "Your secret message image is ready!"

#function to read messages of selected user
def read_message():
    sender = select_a_friend()
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    new_chat = ChatMessage(secret_text,False)
    FRIENDS[sender].chats.append(new_chat)
    print "Your secret message has been saved!"

#function to display char history
def read_chat_history():

    read_for = select_a_friend()
    print '\n6'
    for chat in FRIENDS[read_for].chats:
        if chat.sent_by_me:     
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), FRIENDS[read_for].name, chat.message)

#Program start here:

print "lets get started"
user = int(raw_input(" CHOOSE TYPE OF USER \n1-Default user \n-2 Create new user "))

if (user == 2):
    spy.name =raw_input("Welcome to spychat  tell your spy name first:")
    if len(spy.name) > 0:
        print"welcome "+spy.name + " Glads to have you with us"
        spy.salutation =raw_input("Should i call you Mr. or Ms?\n")
        spy.name +" .I'd like to know a little bit more about you before we proceed\n"


        spy.is_online = True
        spy.age= int (raw_input("what is your age"))

        if spy.age > 12 and spy.age <40:
            spy.rating=int( raw_input("what is your rating?"))

        else:
            print "Enter age between 12 - 40 years"
        #calling of function
        start_chat(spy)
    else:
        print " Please enter valid name"


else:
    start_chat(spy)




