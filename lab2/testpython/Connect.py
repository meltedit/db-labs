import psycopg2

# Function that returns connection to DB
def makeConnect():
    return psycopg2.connect(
        user="postgres",
        password="123",
        host="localhost",
        database="postgres",
    )


# Function that closes connection to DB
def closeConnect(connection):
    connection.commit()
    connection.close()