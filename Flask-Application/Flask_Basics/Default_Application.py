from flask import Flask

app = Flask(__name__)

# Basic
@app.route('/') # http://127.0.0.1:5000/
def index():
    return "<h1>Hello Puppy!</h1>"

# Basic Route
@app.route('/information') # http://127.0.0.1:5000/information
def info():
    return "<h1>Puppies are cute!!</h1>"

# Dynamic Routing
@app.route('/puppy/<name>') # http://127.0.0.1:5000/puppy/<name>
def dynamicPage(name):
    return "<h1>This is a page for {}</h1>".format(name)

if __name__ =='__main__':
    app.run()