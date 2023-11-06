class Email:
    #methods within the class
    def __init__(self, from_address, subject_line, email_contents):
        self.from_address = from_address
        self.subject_line = subject_line
        self.email_contents = email_contents
        self.has_been_read = False
        self.is_spam = False

    def mark_as_read(self):
        self.has_been_read = True

    def mark_as_spam(self):
        self.is_spam = True

inbox = []        
# METHOD FUNCTIONS #
# need to add email first in order to retrieve it

def add_email(from_address, subject_line, email_contents):
    email = Email(from_address, subject_line, email_contents)
    inbox.append(email) #each email sent is appended to inbox
    
def list_messages_from_sender(sender_address):
    index=-1 #so first indexed email will be of index 0
    for email in inbox: #iterating inside the inbox
        if email.from_address==sender_address: #get emails from a specific sender address
            index += 1
            strr= f'{index} {email.subject_line}' #prints index and subject line of email from specific sender address
            print(strr)
           
        elif email.from_address!=sender_address:
            strr="Address not found in inbox. "
            print(strr)        
        

def get_email(sender_address, index):
    for email in inbox:
        if email.from_address == sender_address:
            email.mark_as_read()
            print(inbox[index].email_contents) #emails from a specific sender are in inbox and are retrieved from a given index

def mark_as_spam(sender_address, index):
    for email in inbox:
        if email.from_address == sender_address:
            inbox[index].mark_as_spam() #calls function defined in class methods

def get_unread_emails():
    unread_emails = []
    for email in inbox:
        if not email.has_been_read:
            unread_emails.append(email.subject_line)
    print("\n".join(unread_emails))

def get_spam_emails():
    spam_emails = []
    for email in inbox:
        if email.is_spam:
            spam_emails.append(email.subject_line)
    print("\n".join(spam_emails)) #each email displayed on a new line 

def delete(sender_address, index):
    for email in inbox:
        if email.from_address == sender_address:
            email.mark_as_read()
            del inbox[index]

usage_message = '''
Welcome to the email system! What would you like to do?

s - send email.
l - list emails from a sender.
r - read email.
m - mark email as spam.
gu - get unread emails.
gs - get spam emails.
d - delete email.
e - exit this program.
'''
user_choice = ""

while True: #program runs indefinitely
    user_choice = input(usage_message).strip().lower()
    if user_choice == "s":
        # Send an email (Create a new Email object)
        sender_address = input("Please enter the address of the sender\n:")
        subject_line = input("Please enter the subject line of the email\n:")
        email_contents = input("Please enter the contents of the email\n:")

        # Now add the email to the Inbox
        from_address= sender_address
        add_email(from_address, subject_line, email_contents) #function called and runs on parameters inputted by user

        # Print a success message
        print("Email has been added to inbox.")

        pass
    elif user_choice == "l":
        # List all emails from a sender_address
        sender_address = input("Please enter the address of the sender\n:")

        # Now list all emails from this sender
        list_messages_from_sender(sender_address)
        

    elif user_choice == "r":
        # Read an email
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")

        # Step 2: show all emails from this sender (with indexes)
        list_messages_from_sender(sender_address)       
            
        # Step 3: ask the user for the index of the email
        index = int(input("Please enter the index of the email that you would like to read\n:"))

        # Step 4: display the email
        get_email(sender_address, index)
        

        pass
    elif user_choice == "m":
        # Mark an email as spam
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")

        # Step 2: show all emails from this sender (with indexes)
        list_messages_from_sender(sender_address)       

        # Step 3: ask the user for the index of the email
        index = int(input("Please enter the index of the email to be marked as spam\n:"))

        # Step 4: mark the email as spam
        mark_as_spam(sender_address, index)

        # Step 5: print a success message
        print("Email has been marked as spam")

        pass
    elif user_choice == "gu":
        # List all unread emails
        get_unread_emails()
   
        pass
    elif user_choice == "gs":
        # List all spam emails
        get_spam_emails()
   
        pass
    elif user_choice == "e":
        print("Goodbye")
        break
    elif user_choice == "d":
        # Delete an email
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")

        # Step 2: show all emails from this sender (with indexes)
        list_messages_from_sender(sender_address) 

        # Step 3: ask the user for the index of the email
        index = int(input("Please enter the index of the email to be deleted\n:"))

        # Step 4: delete the email
        delete(sender_address, index)

        # Step 5: print a success message
        print("Email has been deleted")

        pass
    else:
        print("Oops - incorrect input")
    
