import pymysql
import env

class DBUtils:
    """
    This class contains the utilities regarding database
    """

    def __init__(self):
        pass

    @staticmethod
    def __init_connection():
        """
        Returns the mysql connection object.

                Parameters:
                        a (int): A decimal integer
                        b (int): Another decimal integer

                Returns:
                        binary_sum (str): Binary string of the sum of a and b
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


    # Read the database
    def read_db(self, db_name, query):
        """
        Returns the sum of two decimal numbers in binary digits.

                Parameters:
                        a (int): A decimal integer
                        b (int): Another decimal integer

                Returns:
                        binary_sum (str): Binary string of the sum of a and b
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
        input: query(string)
        output: response
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
            raise Exception(message) from err
