# -*- coding: utf-8 -*-
# @Author: sagar
# @Date:   2016-04-23 21:49:11
# @Last Modified by:   Sagar Ghai
# @Last Modified time: 2016-04-30 02:56:20

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from twilio.rest import TwilioRestClient

# put your own credentials here
ACCOUNT_SID = ""
AUTH_TOKEN = ""

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'landslides-26a900b3717d.json', scope)

gc = gspread.authorize(credentials)

sh = gc.open_by_url(
    '')

worksheet = sh.sheet1
list_of_lists = worksheet.get_all_values()

for i in list_of_lists:

    message = client.messages.create(
        to="",
        from_="",
        body="Hey Nikki! :D"
    )
