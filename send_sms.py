from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC3abcf7a4c4c0f1c3706b95f2f54b8b5d"
auth_token  = "1c23fbe3fa6e9f0833948d8b0efa9b8f"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="My name is Roselma. :)",
    to="+557597417523",    # Replace with your phone number
    from_="+554139075460") # Replace with your Twilio number
print message.sid
