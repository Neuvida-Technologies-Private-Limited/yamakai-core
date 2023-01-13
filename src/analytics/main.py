"""
Run user related queries for analytics.
"""
import logging
import pandas as pd
import pymysql

# Setting up logging level to debug
logging.basicConfig(level=logging.DEBUG)
# Params required for utils
host = "database-free-dev.cqdonlctukeo.ap-south-1.rds.amazonaws.com"
username = "admin"
password = "qtD8FErYcLYTaQypzBNz"
db_name = "prod"

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
                host=host,
                user=username,
                passwd=password,
                db=db_name,
                connect_timeout=5,
                cursorclass=pymysql.cursors.DictCursor,
            )

            return conn

        except Exception as err:

            print(err)

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

            print(err)

user_queries = {
    "Total Signups": "select count(*) as 'Total Signups' from access_user",
    "Total Signups SSO": "select count(*) as 'Total Signups SSO' \
                        from access_user where is_sso=1",
    "Total Signups Phone": "select count(*) as 'Total Signups \
                            PHONE' from access_user where phone \
                            IS NOT NULL",
    "Total Signups Email": "select count(*) as 'Total Signups EMAIL' from access_user \
                            where email IS NOT NULL and is_sso = 0",
    "Total Signups SSO (%)": "select (select count(*) from access_user \
                            where is_sso=1) \
                            / (select count(*) from access_user) * 100 \
                            as 'Total Signups SSO (%)'",
    "Total Signups Phone (%)": "select (select count(*) from access_user where phone \
                            IS NOT NULL) \
                            / (select count(*) from access_user) * 100 as \
                            'Total Signups PHONE (%)'",
    # "Total Signups Email (%)": "select (select count(*) from access_user where email IS NOT \
    #                             NULL and is_sso=0) / (select count(*) from access_user) * \
    #                             100 as 'Total Signups EMAIL (%)' \
    #                             NULL and is_sso=0) (select count(*) from access_user) * \
    #                             100 as 'Total Signups EMAIL (%)'",
    "Total signups count": "SELECT count(if(is_sso = 1,1,null)) as SSO_count, \
                                   count(case when email is not null then 1 else null end) as email_count, \
                                   count(case when phone is not null then 1 else null end) as phone_count \
                            FROM access_user",
    "Monthly Signups count": "SELECT MONTH(created_at), \
                                     count(if(is_sso = 1,1,null)) as SSO_count, \
                                     count(case when email is not null then 1 else null end) as email_count, \
                                     count(case when phone is not null then 1 else null end) as phone_count \
                              FROM access_user \
                              GROUP BY MONTH(created_at) \
                              ORDER BY MONTH(created_at)",
     "Weekly signups count": "SELECT WEEK(created_at), \
                                     count(if(is_sso = 1,1,null)) as SSO_count, \
                                     count(case when email is not null then 1 else null end) as email_count, \
                                     count(case when phone is not null then 1 else null end) as phone_count \
                              FROM access_user \
                              GROUP BY WEEK(created_at) \
                              ORDER BY WEEK(created_at) DESC", 
    "Daily Signups":"SELECT DATE(created_at) AS DAY, \
                          COUNT(id) AS 'Daily signups' \
                          FROM access_user \
                          GROUP BY DATE(created_at)\
                          ORDER BY DAY DESC\
                           LIMIT 30;",
     "weekly signups":"SELECT WEEK(created_at) AS Week, \
                          COUNT(id) AS 'Weekly signups' \
                          FROM access_user \
                          GROUP BY WEEK(created_at)\
                          ORDER BY Week DESC\
                           LIMIT 4;",                      
    "Weekly active users":"SELECT WEEK(created_at) AS WEEK, \
                           COUNT(DISTINCT created_by_id) AS WAU \
                           FROM utils_gpt3outputs \
                           GROUP BY WEEK(created_at) \
                           ORDER BY WEEK DESC \
                           LIMIT 52;",
    "Monthly active users":"SELECT MONTH(created_at) AS MONTH, \
                           COUNT(DISTINCT created_by_id) AS MAU \
                           FROM utils_gpt3outputs \
                           GROUP BY MONTH(created_at) \
                           ORDER BY MONTH DESC;",
     "Total generations by week":"SELECT WEEK(created_at) AS WEEK, \
                                         COUNT(id)  \
                                  FROM utils_userinputs \
                                  GROUP BY WEEK(created_at) \
                                  ORDER BY WEEK DESC \
                                  LIMIT 52;",
     "Total generations by month":"SELECT MONTH(created_at) AS MONTH, \
                            COUNT(id) \
                            FROM utils_userinputs\
                            GROUP BY MONTH(created_at) \
                            ORDER BY MONTH DESC;",                                             
    "I/O Template":"SELECT a.user_id_id AS user_id, \
                    a.template_name AS template,\
                    a.input,\
                    b.output \
                    FROM utils_userinputs AS a \
                    JOIN utils_gpt3outputs AS b ON a.id  = b.user_input_id_id \
                    WHERE a.template_name = 'SUBJECT_LINE' \
                    ORDER BY a.user_id_id",
    "Total signups":"SELECT COUNT(DISTINCT id) AS 'Total signups' \
                     FROM access_user;",
    "Power users":  "SELECT b.id,\
	                        b.repeat_days,\
                            au.phone,\
                            au.email, \
                            au.first_name,\
                            au.last_name \
                     FROM (SELECT id, COUNT(*) repeat_days \
	                       FROM (SELECT DATE(created_at) AS date, \
                                        created_by_id AS id \
                                 FROM utils_gpt3outputs \
                                 GROUP BY DATE(created_at),created_by_id \
                                 ORDER BY date DESC) a \
                           GROUP BY id \
                           HAVING COUNT(*) > 1 \
                           ORDER BY id) b \
                     JOIN access_user AS au ON b.id = au.id",
     "Power_Users-templates":"SELECT b.id,\
	                                 b.repeat_days,\
                                     au.phone,\
                                     au.email, \
                                     au.first_name,\
                                     au.last_name,\
                                     uu.template_name \
                              FROM (SELECT id, COUNT(*) repeat_days \
	                                FROM (SELECT DATE(created_at) AS date, \
                                                 created_by_id AS id \
                                          FROM utils_gpt3outputs \
                                          GROUP BY DATE(created_at),created_by_id \
                                          ORDER BY date DESC) a \
                                     GROUP BY id \
                                     HAVING COUNT(*) > 1 \
                                     ORDER BY id) b \
                              JOIN access_user AS au ON b.id = au.id\
                              LEFT JOIN utils_userinputs uu ON b.id = uu.user_id_id",
      "template-use-all-time": "SELECT template_name, COUNT(id) AS template_use\
                                FROM utils_userinputs \
                                GROUP BY template_name\
                                ORDER BY template_use", 
      "template-use-monthly":"SELECT MONTH(created_at), template_name, COUNT(id) AS template_use \
                              FROM utils_userinputs \
                              GROUP BY MONTH(created_at),template_name \
                              ORDER BY MONTH(created_at),template_use",
      "template-use-weekly":"SELECT WEEK(created_at), template_name, COUNT(id) AS template_use \
                              FROM utils_userinputs \
                              GROUP BY WEEK(created_at),template_name \
                              ORDER BY MONTH(created_at) DESC,template_use",
      "user-no-usage":"SELECT id, email, phone, first_name, last_name \
                       FROM access_user \
                       WHERE id NOT IN (SELECT au.id \
				                FROM access_user au \
				                JOIN utils_userinputs uu ON au.id = uu.user_id_id)",                                                                                                                                                     
}

def main():
    '''
    Run the analytics queries for the user.

    Parameters:
    Returns:
    '''

#
    # Create instance of utils class
    db_utils_instance = DBUtils()

    # Running all the queries of the user
    for key, value in user_queries.items():
        results = db_utils_instance.read_db(value)

        res = []
        # Printing the results
        for result in results:
            res.append(result)

        df = pd.DataFrame(res)
        print(df)
        #df.to_excel('power-users.xlsx')   
            #for key, value in result.items():

                # Logging the results
                #logging.info(str(key))
                #logging.info(str(value))

    #Running all the queries of the repeated users
    # for key, value in repeat_users.items():
    #     results = db_utils_instance.read_db(value)

    #     # Logging the keys
    #     logging.info(str(key))

    #     # logging the results
    #     for result in results:
    #         logging.info(result)

if __name__ == '__main__':
    main()
