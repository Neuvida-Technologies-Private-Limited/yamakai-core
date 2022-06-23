import logging
from utils.db_utils import DBUtils
from analytics.user_queries import user_queries, repeat_users


# Setting up logging level to debug
logger = logging.getLogger(__name__).setLevel(logging.DEBUG)

def main():
    """Run all of the analytics tasks."""

#    try:
    # Create instance of utils class
    db_utils_instance = DBUtils()

    # Running all the queries of the user
    for key, value in user_queries.items():
        results = db_utils_instance.read_db("prod", value)

        # Printing the results
        for result in results:
            for key, value in result.items():
                print(key, ': ', value)

    # Running all the queries of the user usage
    for key, value in repeat_users.items():
        results = db_utils_instance.read_db("prod", value)

        # Printing the results
        for result in results:
                print(result)

if __name__ == '__main__':
    main()