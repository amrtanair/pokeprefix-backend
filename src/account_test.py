#!/usr/bin/env python3

import datetime
import os
import pokedb
from pokedb.sql import *
from datetime import date

our_account='Tweety'
auth_token='bla'
country_code='nl'

createdb()
session=connectdb()


date_now=datetime.datetime.now()

account=find_account(session,our_account)
if account is not None:
    print("Found account")
else:
    print("Found no account: inserting")
    account=insert_account(session,our_account,auth_token,date_now,country_code)



