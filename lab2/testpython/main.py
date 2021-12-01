import psycopg2
import Connect
from Menu import Menu

try:
    # Making connection
    connection = Connect.makeConnect()
    # Creating cursor to control DB
    cursor = connection.cursor()
    # Controller call
    Menu.mainmenu()

except (Exception , psycopg2.Error) as error :
        print ("PostgreSQL Error: ",error)
finally:
    # Closing connection
    cursor.close()
    connection.close()
    print("Po0stgreSQL connection is closed")
    