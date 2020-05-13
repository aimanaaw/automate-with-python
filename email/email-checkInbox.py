# IMAP to retrieve email
# import imaplib too complicated
import imapclient, pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.log('email@gmail.com', 'password')

conn.select_folder('INBOX', readonly=True)
# Specify folder and readonly argument to True so you don't accidentaly delete an email

# String inside a list passed into search method. Date must be in the below format
UIDs = conn.search(['SINCE 20-Aug-2015'])

# Translate the UIDs into emails
rawMessage = conn.fetch([UID], ['BODY[]', 'FLAGS'])

message = pyzmail.PyzMessage.factory(rawMessage[UID][b'BODY[]'])

# Look up the imapclient cheat sheet

message.get_subject() #gets the subject
message.get_addresses('from') #gets the sender's email address
message.get_addresses('from') #gets the recepient's email address
message.text_part #tells you if a text part is present
message.htmp_part #tells you if a html part is present
message.get_payload().decode('UTF-8')

conn.list_folders() #returns a list of tuples where the third item is the folder

# to delete emails
# conn.select_folder('INBOX', readonly=False)
# UID1 = conn.search(['ON 24-Aug-2015'])


# conn.delete_messages([UID1/UIDs])