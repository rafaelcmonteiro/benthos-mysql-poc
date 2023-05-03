import pymysql.cursors
import time

connection = pymysql.connect(
    host='localhost',
    user='user',
    password='pass',
    database='db',
    cursorclass=pymysql.cursors.DictCursor
)

current_time = time.ctime()
print(current_time)



# with connection:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO `kern_log` (`date_time`, `kernel_info`) VALUES (%s, %s)"
#         cursor.execute(sql, ('03-05-2023', 'DUMMY INFORMATION ABOUT KERNEL'))

#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()

#     with connection.cursor() as cursor:
#         # Read a single record
#         sql = "SELECT `date_time`, `kernel_info` FROM `kern_log` WHERE `date_time`=%s"
#         cursor.execute(sql, ('03-05-2023',))
#         result = cursor.fetchone()
#         print(result)