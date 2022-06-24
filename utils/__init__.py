"""
Create the classes which are common and are frequently used.

Connect to the data base and perform basic crud operations.

Classes:

    DBUtils

Functions:
    __init_connection()
    read_db(db_name: string, query: string) -> list
    write_database(db_name: string, query: string)

"""
__all__ = ['db_utils', 'error', 'exceptions']
