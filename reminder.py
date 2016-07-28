# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
from handler import *
from random import choice

account_sid = "AC28f07318663c937b3700b1addf93107f"
auth_token = "cd52fae81f08302ef37a2e505a192bf0"  
fromnumber = "+16314064378"
tonumber = "+12065662162" 
body_text = "Hello"


client = TwilioRestClient(account_sid, auth_token)

def send(fromnumber, tonumber, body_text):
	print "Preparing to send sms text from %s to %s: %s" % (fromnumber, tonumber, body_text)

	message = client.messages.create(to=tonumber, 
									 from_=fromnumber, 
									 body=body_text)

	print "SMS text successfully sent!"