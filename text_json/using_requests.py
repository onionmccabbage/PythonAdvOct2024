# we may access external APIs using the requests library
import requests # we may need to pip install requests

def getData():
    '''make a request to an API and expect to receive JSON'''
    apiURL = 'https://jsonplaceholder.typicode.com/photos'
    response = requests.get(apiURL) # we receive a response object, which includes any data
    # we can access many parts of the response object
    print(response.status_code, response.raw)
    res_j = response.json() # this will take the JSON and convert to a Python structure
    return res_j # we have a list of dictionaries

if __name__ == '__main__':
    r = getData()
    # print(r, type(r))
    print(r[42], type(r[42]))