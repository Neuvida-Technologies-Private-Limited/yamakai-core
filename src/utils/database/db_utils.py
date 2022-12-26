"""
Class related to database utils.
"""
import pymysql
import env
from utils.exceptions import CustomError

class DBUtils:
    """
    A class to have utils for the database.

    ...

    Attributes
    ----------
    Methods
    -------
    __init_connection():
        Returns the mysql connection object.
    read_db(query):
        Returns the result after running a read query on the database.
    """

    def __init__(self):
        pass

    @staticmethod
    def __init_connection():
        """
        Returns the mysql connection object.

        Parameters:
        Returns:
                conn (pymysql.connections.Connection): connection object of sql
        """
        try:
            # Creating a connection
            conn = pymysql.connect(
                host=env.host,
                user=env.username,
                passwd=env.password,
                db=env.db_name,
                connect_timeout=5,
                cursorclass=pymysql.cursors.DictCursor,
            )

            return conn

        except Exception as err:

            # Raising Exception
            raise CustomError(str(err)) from err

    def read_db(self, query):
        """
        Returns the result after running a read query on the database.

        Parameters:
                query (str): Read query to be ran on the database

        Returns:
                result (list): Binary string of the sum of a and b
        """
        try:
            # Fetching the db connection instance
            conn = DBUtils.__init_connection()

            # Creating the cursor
            cur = conn.cursor()

            # Use all the SQL you like
            cur.execute(query)

            # result variable which will have all the rows
            result = cur.fetchall()

            # Closing the connection
            conn.close()

            return result

        except Exception as err:

            # Raising Exception
            raise CustomError(str(err)) from err
