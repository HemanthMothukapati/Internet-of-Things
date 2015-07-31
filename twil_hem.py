from twilio.rest import TwilioRestClient 
 
def mes(text):
# put your own credentials here 
ACCOUNT_SID = "ACb1bfa2b1867c540129cb970a6b3c97b0" 
AUTH_TOKEN = "e29e98336bf81b5b6045b0b19b1f6e97" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
	to="3308108606", 
	from_="+13307524684", 
	body=text,  
    )
