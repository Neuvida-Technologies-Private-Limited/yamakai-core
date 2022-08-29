"""
Run user related queries for analytics.
"""
import logging
import pandas as pd
from utils.db_utils import DBUtils
from analytics.user_queries import user_queries#,repeat_users

# Setting up logging level to debug
logging.basicConfig(level=logging.DEBUG)


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
        #print(df)
        df.to_excel('template-weekly-usage.xlsx')   
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
