# we may need to pip install flask
from flask import Flask
import sys

def main():
    '''here is a simple Flask implementation'''
    app = Flask(__name__)
    # we then declare routes for our web server
    # any non-specific route will assume 'GET'
    @app.route('/') # the route to the root of our server
    def root():
        return f'Welcome to {__name__} Flask server. You are at the root'
    @app.route('/about')
    def about():
        msg = ' '.join(sys.argv)
        return f'This is the about page. Arguments are: {msg}' # this is a plain string
    @app.route('/web')
    def web():
        page = f'''
<h3>Welcome</h3>
<p>This is some HTML content</p>
<ul>
<li>server: {sys.argv[0]}</li>
<li>path: /web</li>
</ul>
'''
        return page
    # mini-challenge: write a route which returns the JSON for creatures (loaded from a file)
    @app.route('/creatures')
    def creatures():
        # read in some JSON
        with open('creatures.json', 'rt') as fin:
            c = fin.read()
        return c

    # we must remember to run the server
    app.run()



if __name__ == '__main__':
    main()