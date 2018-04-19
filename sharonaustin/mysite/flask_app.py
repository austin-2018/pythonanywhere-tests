from flask import Flask, request
#import cgi
import os
import jinja2
#add path for templates, specifies where templates will be stored
#make a new file system path by joining the location of the current file with the templates directory
template_dir = os.path.join(os.path.dirname(__file__),
    'templates')
#initializes jinja engine using the templates directory
#template loader knows where the templates live in the file system and load them into applications memory
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))
#added request object which will allow us to access the data in request user
app = Flask(__name__)
#below does not work in Pythonanywhere
#app.config['DEBUG'] = True
#above does not work in Pythonanywhere

#set up global element in form
form = """
<!doctype html>
    <html>
        <body>
            <div style="display: block;margin: 0px auto;text-align:center;"><!-- form wrapper -->
                <form action="/hello" method="post">
                    <label for="first-name">First Name</label>
                    <input id="first-name" type="text" name="first_name" />
                    <input type="submit" />
                </form>
            </div>
        </body>
    </html>

"""
@app.route('/')
def index():
    template = jinja_env.get_template('base.html')
    return template.render()
@app.route('/hello', methods=['POST'])
def hello():
    #For a GET method only first_name = request.args.get('first_name') note that it uses PARENS not BRACKETS
    first_name = request.form['first_name'] #for post method accessing a dictionary like method so brackets
    template = jinja_env.get_template('greeting.html')
    #return '<h3>Hello  ' + first_name + '</h3><br />'
    return template.render(name=first_name)
