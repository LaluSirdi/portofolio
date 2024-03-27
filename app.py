import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/contact", methods=["POST"])
def contact_post():
    if request.method == 'POST':
        name = request.form.get('name_give')
        email = request.form.get('email_give')
        message = request.form.get('message_give')
        
        doc = {
            'name': name,
            'email': email,
            'message': message
        }
        db.contacts.insert_one(doc)
        
        return jsonify({'msg':'data saved!'})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
