# we may need to pip install flask
from flask import Flask
import sys

def main():
    '''here is a simple Flask implementation'''
    app = Flask(__name__)
    # we then declare routes for our web server
    # any non-specific route will assume 'GET'
    @app.route('/') # the route to the root of our server
    @app.route('/<locale>') # the route to the root of our server
    def root(locale='en'):
        return f'Welcome to {__name__} Flask server. You are at the root'
    @app.route('/hello') # is it useful to provide several routes to the same content
    @app.route('/ciao')  # maybe services have several product names
    @app.route('/wotcha')# or even common mispellings
    def welcome():
        return 'Welcome to the web server'

# we may need to access parts of the URL: often the REST arguments
    @app.route('/greet')
    @app.route('/greet/<name>') # if we have optional REST parameters, we must pass them in to the function
    def greet(name='Timnit'):
        '''return a page that handles REST parameters'''
        content = f'<h2>Greetings {name}'
        return content
    
    # Flask lets us use HTML templates for content. We may pass REST parameters to the template
    # Flask expects to use a folder called 'templates'

    

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