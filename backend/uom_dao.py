from utils import (create_connection,create_cursor,close_connection,
                   close_cursor,commit_dml,execute_query) 
# We are using () to import so that we can safely write these in another 
# line without getting error

def get_uom(user:str , password:str, host:str, database:str)->list:
    """
    Get the list of all records in user
    Args:
        user: username
        password: password for the database
        host:  ip address of host
        database: database name 
    Returns:
       list containing all records
    """
    conn=create_connection(user,password,host,database)
    cursor=create_cursor(conn)
    query="select * from uom"
    cursor=execute_query(query)
    response = []
    for (uom_id, uom_name) in cursor:
        response.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })
    close_cursor(cursor)
    close_connection(conn)
    return response



