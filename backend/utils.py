
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html

import mysql.connector
from typing import Any
import logging

def create_connection(user:str , password:str, host:str, database:str)-> Any:
    """
    Usage : Used to connect to database
    Args:
        user: username
        password: password for the database
        host:  ip address of host
        database: database name 
    Returns:
        Connecion object of mysql database
    """
    try:

        connection=mysql.connector.connect(user=user,password=password,
                                       host=host,database=database)
        print("The connection successfully established")

    except Exception as e:
        logging.error(f"error in establishing connection {e}")
        raise e
    
    return connection

def close_connection(connection)->None:
    """
    Usage: Use to close the database connection
    Args:
        connection: Database connection object
    Returns: None
    """
    try:

        connection.close()
        print("Connection was successfully closed")
    except Exception as e:
        logging.error(f"The was error in closing connection {e}")
        raise e

def create_cursor(connection:Any)->Any:
    """
    Usage: use to crate cursor
    Args:
        connection: database connection object
    Returns:
        cursor object
    """
    try:
        cursor=connection.cursor()
        print("Cursor created successfully")
        return cursor
    except Exception as e:
        logging.error(f"Not able to create cursor {e}")
        raise e

def close_cursor(cursor:Any)->None:
    """
    Usage: Use to close cursor 
    Args:
        cursor : cursor object
    Returns:
        None 
    """
    try:
        cursor.close()
        print("Successfully closed the cursor")
    except Exception as e:
        logging.error(f"Unable to close cursor {e}")
        raise e


def commit_dml(cursor:Any)->None:

    """
    Used to commit the changes done by DML command to the database.
    Args:
        cursor: cursor object
    Returns:
        None
    
    """
    try:
        cursor.commit()
        print("Committed succesfully to the database")
    except Exception as e:
        logging.error(f"Unable to commit {e}")
        raise e

def execute_query(query:str,cursor:Any)->Any:
    """
    used to execute any query:
    Args:
        query:query to be exceuted
        cursor: Cursor object
    Returns:
        list of all values returned
    """
    answer=cursor.execute(query)
    return answer


