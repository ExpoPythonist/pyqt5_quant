#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
IG Markets REST API Library for Python
http://labs.ig.com/rest-trading-api-reference
By Lewis Barber - 2014 - http://uk.linkedin.com/in/lewisbarber/
"""

import requests
import json
import logging
import traceback
import pandas as pd
from telethon import TelegramClient, sync, events
import sys, requests
import time


class TelegramService:
    API_ID = 1239577
    API_HASH = '3687778bd345ba2f777489ee01df55a9'
    PHONE_NUMBER = '+79517633106'

    def __init__(self):
        self.API_KEY = 1239577
        self.API_HASH = '3687778bd345ba2f777489ee01df55a9'

    def send_code(self, phone_number):
        client = TelegramClient('Telegram Desktop 1.9.21', self.API_KEY, self.API_HASH)
        client.connect()
        try:
            # if not client.is_user_authorized():
            res = client.send_code_request(phone_number)
        except Exception as ex:
            return 400
        return res.__dict__

    def validate_code(self, phone_number, code, phone_code_hash):
        client = TelegramClient('Telegram Desktop 1.9.21', self.API_KEY, self.API_HASH)
        client.connect()
        try:
            # if not client.is_user_authorized():
            me = client.sign_in(phone=phone_number, code=code, password=None, bot_token=None, phone_code_hash=phone_code_hash)
        except Exception as ex:
            print('exxx ', str(ex))
            return str(ex)
        return me.__dict__

    def send_message(self):
        pass

    ########## PARSE_RESPONSE ##########

    def parse_response_without_exception(self, *args, **kwargs):
        """Parses JSON response
        returns dict
        no exception raised when error occurs"""
        response = json.loads(*args, **kwargs)
        return (response)

    def parse_response_with_exception(self, *args, **kwargs):
        """Parses JSON response
        returns dict
        exception raised when error occurs"""
        response = json.loads(*args, **kwargs)
        if 'errorCode' in response:
            raise (Exception(response['errorCode']))
        return (response)

    ############ END ############

    ########## ACCOUNT ##########

    def fetch_accounts(self):
        """Returns a list of accounts belonging to the logged-in client"""
        response = requests.get(self.BASE_URL + '/accounts', headers=self.LOGGED_IN_HEADERS)
        data = self.parse_response(response.text)
        if self.return_dataframe:
            data = pd.DataFrame(data['accounts'])
        return (data)
