import requests
from linkedin_auth import auth, headers

# https://docs.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/sign-in-with-linkedin
# basic API requests
def user_info(headers):
    '''
    Get user information from Linkedin
    '''
    response = requests.get('https://api.linkedin.com/v2/emailAddress?q=members&projection=(elements*(handle~))', headers = headers)
    user_info = response.json()
    return user_info

if __name__ == '__main__':
    credentials = 'credentials.json'
    access_token = auth(credentials) # Authenticate the API
    headers = headers(access_token) # Make the headers to attach to the API call.
    user_info = user_info(headers) # Get user info
    print(user_info)    