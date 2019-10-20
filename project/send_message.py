# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:47:39 2019

@author: Eesh Gupta
"""

from twilio.rest import Client 

def sendSMS(to_phone, message,from_phone = "+17325851937", auth_token =None, acc_name = None): 
    '''
    input: 
        
    output: Sends message to the user
    '''

    
    acc_sid = 'AC8a64409324387f3229dceec5c893c38c'
    auth_token = 'ee699956f1b8b5102eb6d2ac19787c8f'
    
    client = Client(acc_sid, auth_token)
    
    message_ = client.messages \
                .create(
                     body=message,
                     from_=from_phone,
                     to=to_phone
                 )
    
    
"""
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC8a64409324387f3229dceec5c893c38c'
auth_token = 'ee699956f1b8b5102eb6d2ac19787c8f'
client = Client(account_sid, auth_token)

message_ = client.messages \
                .create(
                     body="Hi its eesh!",
                     from_='+17325851937',
                     to='+18482562066'
                 )

#print(message.sid)
"""