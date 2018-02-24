import builtins
import sqlalchemy
import random

from sqlalchemy import create_engine,desc,func
from sqlalchemy.orm import sessionmaker

from pokedb.classes import Base,Account,Prefix,Observation,Name,Score,Season,Adjective,Color,Noun

engine = create_engine('sqlite:///%s' % 'data/pokedb.db')
check_distance = 6

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

def insert_prefix(session,inet6num,date_now,season_id):
    new_prefix = Prefix(inet6num=inet6num,
                        date_seen_first=date_now, date_seen_last=date_now,
                        season_first_seen_id=season_id)
    session.add(new_prefix)
    session.commit()
    return(new_prefix)
    
    return()

def find_prefix(session,inet6num):
    prefix_q = session.query(Prefix).filter(prefix==inet6num)
    if prefix_q.count() > 0:
        return(prefix_q.first())
    else:
        return None

def do_location_check(session,location,radius):
    # This is a stub; will check if there are points within $radius of
    # $location
    return False

def insert_season(session,name,date_start,date_end):
    new_season = Season(name=name,period_start=date_start,period_end=date_end)
    session.add(new_season)
    session.commit()
    return(new_season)

def insert_name(session,word_1_id,word_2_id,word_3_id,prefix_id,account_id):
    new_name = Name(word_1_id=word_1_id, word_2_id=word_2_id,
                    word_3_id=word_3_id, prefix_id=prefix_id,
                    account_id=acount_id)
    session.add(new_name)
    session.commit()
    return(new_name)

def find_name(word_1_id,word_2_id,word_3_id):
    name_q=session.query(Name).filter(Name.word_1_id==word_1_id).filter(Name.word_2_id==word_2_id).filter(Name.word_3_id==word_3_id)
    if name_q.count() > 0:
        return(name_q.first())
    else:
        return None

def insert_word(name):
    new_word = Word(name=name)
    session.add(new_word)
    session.commit()
    return(new_word)

def insert_observation(prefix_id,season_id,account_id,location,points,points_reason):
    new_observation = Observation(prefix_id=prefix_id, season_id=season_id,
                                  account_id=account_id, location=location,
                                  points=points,points_reason=points_reason)
    session.add(new_observation)
    session.commit()
    return(new_observation)

def report_season_score(session,season_id,account_id):
    season_score_q=session.query(Score).filter(Score.account_id==account_id).filter(Score.season_id==season_id)
    if season_score_q.count() > 0:
        return(season_score.first().value)
    else:
        return(0)

def report_global_score(session,account_id):
    global_score=0
    global_score_q=session.query(Score).filter(Score.account_id==account_id)
    for row in global_score_q.all():
        global_score=global_score+row.value()
    return(global_score)

def add_score(session,account_id,season_id):
    new_score = Score(account_id=account_id,season_id=season_id,value=value)
    session.add(new_score)
    session.commit()
    return(new_score)

def give_random_name(session):
    #adjective_max = session.query(func.max(Adjective.id)).first().scalar()
    #color_max = session.query(func.max(Color.id)).scalar()
    #noun_max = session.query(func.max(Noun.id)).scalar()
    adjective_max = 45
    color_max= 142
    noun_max = 40
    adjective_rand=random.randint(1,adjective_max)
    color_rand = random.randint(1,color_max)
    noun_rand = random.randint(1,noun_max)
    return([adjective_rand,color_rand,noun_rand])

def id2name(session,adjective_id,color_id,noun_id):
    adjective_q =session.query(Adjective).filter(Adjective.id==adjective_id)
    color_q = session.query(Color).filter(Color.id==color_id)
    noun_q = session.query(Noun).filter(Noun.id==noun_id)
    return("%s%s%s" % (adjective_q.first().text,color_q.first().text,noun_q.first().text))

def count_score(account_id,word1_id,word2_id,word3_id,inet6num,location):
    session_score = 0
    session_reason = ""
    if report_global_score(session,account_id) > 0:
        session_score = session_score + 5
        session_reason = "Existing User"
    else:
        session_score = session_score + 10
        session_reason = "Newbie"
    if find_prefix(session,inet6num) is not None:
        session_score = session_score + 5
        session_reason = session_reason + " Seen Prefix"
    else:
        session_score = session_score + 10
        session_reason = session_reason + " UnSeen Prefix"
    if do_location_check(session,location,check_distance) == True:
        session_score = session_score + 5
        session_reason = session_reason + " Discovered Location"
    else:
        session_score = session_score + 10
        session_reason = session_reason + " UnDiscovered Location"
    if find_name(word_1_id,word_2_id,word_3_id) is True:
        session_score = session_score + 10
        session_reason = session_reason + " New Prefix Name"
    else:
        session_score = session_score + 5
        session_reason = session_reason + " Used Prefix Name"

# Other score awarding for Using someone else's name needs to be designed
    return(account_id,session_score,session_reason) 
