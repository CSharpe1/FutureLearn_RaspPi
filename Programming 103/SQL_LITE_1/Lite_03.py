#! python3
import sqlite3
from random import randint
from time import time


conn = sqlite3.connect(r"C:\Users\charles.sharpe\OneDrive - Global Graphics PLC\Documents\1_CS\FutureLearn_RaspPi\Programming 103\SQL_LITE_1\computer_cards.db")


def read_all_cards():
    result = conn.execute("SELECT * FROM computer")
    return result.fetchall()

def pick_card():
    cards = read_all_cards()
    random_card = cards[randint(0, len(cards) - 1)]
    insert_picked(random_card[0])
    return random_card


def insert_picked(name):
    insert_sql = "INSERT INTO picked(name, time) VALUES ('{}', {})".format(name, time())
    conn.execute(insert_sql)
    conn.commit()


card = pick_card()
print(card)

conn.close()



