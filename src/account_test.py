#!/usr/bin/env python3

import datetime
import os
import pokedb
from pokedb.sql import *
from datetime import date, timedelta

our_account='Tweety'
auth_token='bla'
country_code='nl'

createdb()
session=connectdb()


date_now=datetime.datetime.now()


#account=find_account(session,our_account)
#if account is not None:
#    print("Found account")
#else:
#    print("Found no account: inserting")
#    account=insert_account(session,our_account,auth_token,date_now,country_code)

account1=insert_account(session,'Tweety','bird',date_now-timedelta(days=5),"NL")
account2=insert_account(session,'Sylvester','cat',date_now-timedelta(days=6),"BE")

date1=datetime.datetime.strptime('2018-02-01 00:00', '%Y-%m-%d %H:%M')
date2=datetime.datetime.strptime('2018-03-01 00:00', '%Y-%m-%d %H:%M')
date3=datetime.datetime.strptime('2018-04-01 00:00', '%Y-%m-%d %H:%M')


season1=insert_season(session,'February Season',date1,date2)
season2=insert_season(session,'March Season',date2,date3)

