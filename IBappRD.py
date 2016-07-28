# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
from handler import *
from random import choice

account_sid = "AC28f07318663c937b3700b1addf93107f"
auth_token = "cd52fae81f08302ef37a2e505a192bf0"  
fromnumber = "+16314064378"
tonumber = "+12065662162" 
body_text = "Good Afternoon! PLEASE update your CAS project!"


client = TwilioRestClient(account_sid, auth_token)

def send(fromnumber, tonumber, body_text):
	print "Preparing to send sms text from %s to %s: %s" % (fromnumber, tonumber, body_text)

	message = client.messages.create(to=tonumber, 
									 from_=fromnumber, 
									 body=body_text)

	print "SMS text successfully sent!"

def send_media(fromnumber, tonumber, media_links):
	print "Preparing to send media text from %s to %s: %s" % (fromnumber, tonumber, media_links)

	message = client.messages.create(to=tonumber, 
									 from_=fromnumber, 
									 media_url=media_links)

	print "Media text successfully sent!"

send(fromnumber, tonumber, body_text)

media_links = ["http://quotes.lifehack.org/media/quotes/quote-Walt-Disney-walt-disney-dreams-36.png","http://brightdrops.com/wp-content/uploads/2014/11/waltdisneywhyworryquote.jpg","http://i.kinja-img.com/gawker-media/image/upload/kzelsaedog0otjsyxxz2.jpg","http://thedailyquotes.com/wp-content/uploads/2015/06/fun-to-do-the-impossible-walt-disney-daily-quotes-sayings-pictures.jpg","http://www.searchquotes.com/sof/images/picture_quotes/187991_20140416_161856_dori.jpg","http://www.brainyquote.com/photos/w/waltdisney131640.jpg","http://cdn.quotesgram.com/small/50/25/279587043-walt-disney-quotes-sayings-do-not-stress-change.jpg","http://www.goodmorningquote.com/wp-content/uploads/2015/09/motivational-quotes-about-fitness-and-health.jpg","https://s-media-cache-ak0.pinimg.com/564x/b8/5f/a7/b85fa7ab5577fc838ac4b931537b3e7b.jpg","http://multilingualbooks.com/wp/soundandvision/files/2014/04/french_quote.jpg","https://s-media-cache-ak0.pinimg.com/236x/ec/5b/b6/ec5bb6ea176240981a9f780414d395f6.jpg", "https://s-media-cache-ak0.pinimg.com/236x/09/b7/90/09b79051932708fb3ef49964ab4558fb.jpg"]

send_media(fromnumber, tonumber, choice(media_links))