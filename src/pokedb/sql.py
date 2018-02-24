import builtins
import sqlalchemy

from sqlalchemy import create_engine,desc
from sqlalchemy.orm import sessionmaker

from pokedb.classes import Base,Account,Prefix,Observation,Name,Score,Season,Word

engine = create_engine('sqlite:///%s' % 'pokedb.db')

def connectdb():
    DBSession = sessionmaker(bind=engine)
    session=DBSession()
    return(session)

def createdb():
    Base.metadata.create_all(engine)

def insert_account(session,nickname,auth_token,date_now,country_code):
    new_account = Account(nickname=nickname, auth_token=auth_token,
                          date_joined=date_now, date_last_seen=date_now,
                          country_code=country_code,active=True)
    session.add(new_account)
    session.commit()
    return(new_account)


def find_account(session,nickname):
    account_q=session.query(Account).filter(Account.nickname==nickname)
    if account_q.count() > 0:
        return(account_q.first())
    else:
        return None

def insert_prefix(session,inet6num,name_id,date_now,season_id):
    return()

def check_prefix(session,inet6num):
    # returns (account_id, season_id, date_seen)
    return()


