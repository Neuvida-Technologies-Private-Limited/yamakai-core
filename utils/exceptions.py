class CustomError(Exception):
    """
    A class to represent a custom error.

    ...

    Attributes
    ----------
    message : str
        error message to show the user

    Methods
    -------
    """

    def __init__(self, message):

        super().__init__(message)
        self.message = message


    def __str__(self):

        return 'CustomError, {0} '.format(self.message)

