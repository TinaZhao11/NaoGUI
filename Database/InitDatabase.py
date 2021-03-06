'''This project is created by Zeyu Zhao
This package contains the Database and some Initial Operation for Databse
This InitDatabase file used to create the Database for project'''
import sqlite3

conn = sqlite3.connect('animation.db')
c = conn.cursor()
# Create table for database animation.db
def creeatTable():
    c.execute("create table if not exists robotinfo (id integer primary key, ip varchar(20), port integer)")
    c.execute("create table if not exists steplist (name text, leglist text, steplist text,length integer, id integer primary key)")
    c.execute("create table if not exists musiclist (name text, beatlist text, length integer, id integer primary key)")
    c.execute("create table if not exists animation (name text, list text,listline integer, id text primary key)")

if __name__ == '__main__':
    creeatTable()
