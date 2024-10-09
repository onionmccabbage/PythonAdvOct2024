# we may need to pip install flask
from flask import Flask

def main():
    '''here is a simple Flask implementation'''
    app = Flask(__name__)
    # we then declare routes for our web server
    # any non-specific route will assume 'GET'
    @app.route('/') # the route to the root of our server
    def root():
        return f'Welcome to {__name__} Flask server. You are at the root'

    # we must rememver to run the server
    app.run()



if __name__ == '__main__':
    main()