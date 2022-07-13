import sqlite3
from threading import Lock
lock= Lock()

con = sqlite3.connect('messages.db', check_same_thread=False)
cur = con.cursor()

def createtable():
    lock.acquire(True)
    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS registers( 
            message text NOT NULL,
            topic text NOT NULL
        )
        '''
    )
    con.commit()
    lock.release()

def droptable():
    lock.acquire(True)
    cur.execute(
        '''
        DROP TABLE IF EXISTS registers
        '''
    )
    con.commit()
    lock.release()
    

def addmessage(new_message, new_topic):
    lock.acquire(True)
    cur.execute("insert into registers values (?, ?)", (new_message, new_topic))
    con.commit()
    lock.release()

def getmessagesbytopic(topic):
    lock.acquire(True)
    # search topics
    objs = []
    for result in cur.execute("SELECT * from registers WHERE topic=:tpc",{"tpc":topic}):
        obj = {
            "message": result[0],
            "topic": result[1]
        }
        objs.append(obj)
    lock.release()
    return objs