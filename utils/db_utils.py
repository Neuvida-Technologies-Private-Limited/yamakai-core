import pymysql
import env

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
    read_db(db_name, query):
        Returns the result after running a read query on the database.
    write_database(db_name, query):
        Runs a query to perform a write operation on the database and returns the results.
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
            raise Exception() from err

    def read_db(self, db_name, query):
        """
        Returns the result after running a read query on the database.

        Parameters:
                db_name (str): Name of the database to connect
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
            raise Exception() from err


    def write_database(self, db_name, query):
        """
        Runs a query to perform a write operation on the database and returns the results.

        Parameters:
                db_name (str): Name of the database to connect
                query (str): Read query to be ran on the database

        Returns:
                response (list): Response after running the query.
        """
        try:
            # Fetching the conn connection instance
            conn = DBUtils.init_connection()

            # Creating the cursor
            cur = conn.cursor()

            # Use all the SQL you like
            response = cur.execute(query)

            # Closing the connection
            conn.commit()

            # Closing the connection
            conn.close()

            return response

        except Exception as err:

            # Raising Exception
            raise Exception() from err
