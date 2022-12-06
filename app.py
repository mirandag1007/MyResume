#import libraries and packages 
from flask import Flask, render_template

#create our application
app = Flask(__name__)

#directory
@app.route('/')
def home():
    return render_template('index.html')


