# -*- coding: utf-8 -*-
# @Author: sagar
# @Date:   2016-04-14 12:50:30
# @Last Modified by:   Sagar Ghai
# @Last Modified time: 2016-04-30 02:41:02
from twilio.rest import TwilioRestClient

# put your own credentials here
ACCOUNT_SID = ""
AUTH_TOKEN = ""

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    to="",
    from_="",
    body="Hey Nikki! :D"
)

print message.sid
