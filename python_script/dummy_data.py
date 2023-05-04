#!/bin/env python
import pymysql.cursors
from essential_generators import DocumentGenerator
import time

connection = pymysql.connect(
    host='mysql',
    user='user',
    password='pass',
    database='db',
    cursorclass=pymysql.cursors.DictCursor
)

# Getting current time.
current_time = time.ctime()

# Generate Phrase for dummy data load.
gen = DocumentGenerator()
sentence = gen.sentence()

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `kern_log` (`time`, `kernel_info`) VALUES (%s, %s)"
        cursor.execute(sql, (current_time, sentence))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `time`, `kernel_info` FROM `kern_log`"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)