#!/usr/bin/env python
# -*- coding: utf-8 -*-.

import sqlite3
import random

VOCA_DICT = {
    'id': ''
    ,'words': ''
    ,'category': ''
    ,'kanji': ''
    ,'type': ''
    ,'desciption':''
    ,'dependency':''
    ,'example':''
    ,'lesson':''
}

DBPATH='Nihongo.db'

voca_conn = None
voca_curr = None

def voca_db_init():
    try:
        global voca_conn
        global voca_curr
        voca_conn = sqlite3.connect(DBPATH)
        voca_curr = voca_conn.cursor()
    except Exception as e:
        print 'Fail to initDB(%s)' % DBPATH
        raise

def random_voca_test():
    # get voca counts
    voca_curr.execute("SELECT COUNT(*) FROM vocabulary")
    voca_counts = voca_curr.fetchone()[0]
    print 'VOCA_COUNTS:', voca_counts

    random.seed()
    rand_int = random.randint(1, voca_counts)
    print 'RAND_INT:', rand_int

    voca_row = VOCA_DICT.copy()
    voca_curr.execute("SELECT %s FROM vocabulary WHERE id='%s'" % (', '.join(sorted(voca_row.keys())), rand_int))
    #print voca_curr.fetchone()
    for key, value in zip(sorted(voca_row.keys()), voca_curr.fetchone()):
        print '%s => %s' % (key, value)
        voca_row[key] = value

    # get user input
    response = raw_input('Please Enter Answer: ')
    print response

if __name__ == '__main__':
    voca_db_init()
    random_voca_test()
    voca_conn.close()
