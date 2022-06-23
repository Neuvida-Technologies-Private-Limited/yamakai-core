class CustomError(Exception):
    """
    To be used on invalid request data
    message should be user friendly as it will be shown to the users
    """

    def __init__(self, message):

        super().__init__(message)
        self.message = message


    def __str__(self):

        return 'CustomError, {0} '.format(self.message)

