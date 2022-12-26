"""
Class related to custom errors.
"""

class CustomError(Exception):
    """
    A class to represent a general custom error.

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
