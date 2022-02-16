import psycopg2
from psycopg2 import Error
import os


db_user = os.environ.get("DB_USER")
db_pw = os.environ.get("DB_PW")
db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_name = os.environ.get("DB_NAME")
#################################################################################
def createT():
#hhhhhhjjjjjjj
    try:
        connection = psycopg2.connect(
                                      user=db_user,
                                      password=db_pw,
                                      host=db_host,
                                      port=db_port,
                                      database=db_name
                                     )
        cursor = connection.cursor()
    # SQL query to create a new table
        create_table_query = '''CREATE TABLE voteevent
              (ID INT PRIMARY KEY     NOT NULL,
              YES           INT    NOT NULL,
              NO         INT    NOT NULL); '''
    # Execute a command: this creates a new table
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully in PostgreSQL ")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            return True
        else:
            return False
#################################################################################
def checkT(table_name):
    table = table_name
    try:
        connection = psycopg2.connect(
                                      user=db_user,
                                      password=db_pw,
                                      host=db_host,
                                      port=db_port,
                                      database=db_name
                                     )
        cursor = connection.cursor()
        # SQL query to check table exist
        cursor.execute(f"""SELECT EXISTS(SELECT relname 
                                       FROM pg_class
                                       WHERE relname = {table});""")
        
        
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if not cursor.fetchone()[0]:
            createT()
            print(f"Table {table} Created")
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            return True
        else:
            return False

#################################################################################



#################################################################################



#################################################################################





#################################################################################









