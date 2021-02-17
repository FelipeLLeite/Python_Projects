from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="felipelleite",
        password=getpass("enter your password: "),

    ) as connection:
        print(connection)
except Error as e:
    print(e)
