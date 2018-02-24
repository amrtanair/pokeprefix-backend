#!/usr/bin/env python3

import datetime
import os
import pokedb
from pokedb.sql import *
from datetime import date

our_account='Tweety'
auth_token='bla'
country_code='nl'

#createdb()
session=connectdb()

word_list=give_random_name(session)

print("%s" % id2name(session,word_list[0],word_list[1],word_list[2]))
