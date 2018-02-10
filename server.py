""" BookRecs App """
from jinja2 import StrictUndefined 
from flask import Flask, render_template, request, flash, redirect, jsonify, url_for
from flask_debugtoolbar import DebugToolbarExtension 
#import model 

app = Flask(__name__)

#This is required to use my Flask sessions and the debug toolbar
app.secret_key = "ABC"

#This is in case Jinja2 fails, it will raise an error
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True 

########### Application routes ############

@app.route('/')
def home():
    """ Homepage """

    return render_template("home.html")



if __name__ == "__main__":
# We have to set debug=True here, since it has to be True at the point
# that we invoke the DebugToolbarExtension 
    app.debug = False

# NOTE: Will set up connection to db later
    # connect_to_db(app)

# User the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0", debug=True)