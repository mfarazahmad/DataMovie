import os
from flask_cors import CORS
from flask import Flask, jsonify
import analytics as parser

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():

    base_template = """<h1>Welcome to the Movie Stats Home Page!</h1>
                    <p>API Directory</p>
                    <ul>
                        <li>Get the top stats: /api/top_stats</li>
                        <li>Get the list of actors: /api/get_actors</li>
                        <li>Get a specific actors stats: /api/actorname</li>
                    </ul>"""

    return base_template

@app.route('/api/top_stats', methods=['GET'])
def top_stats():
    genre_stats = parser.topTenGenres()
    actor_stats = parser.topTenActors()
    director_stats = parser.topTenDirectors()

    stats = {'top_ten_genres': genre_stats, 'top_ten_actors': actor_stats, 'top_ten_directors':director_stats}

    return jsonify(stats)

@app.route('/api/get_actors', methods=['GET'])
def get_actors():
    stats = parser.actorList()
    return jsonify(stats)

@app.route('/api/<string:actorname>', methods=['GET'])
def actorStats(actorname):
    stats = parser.actorStats(actorname)
    return jsonify(stats)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)

"""
Starting
X Initialize Folder into a git repo
X Create virtualenv and install packages
X Checkout a branch from master per feature and merge them into master as you work. (Typical branch flow dev_feature -> qa -> prod)
X Plan app architecture into simple blueprint like folders based on function (No need to use flask blueprints)
Data Management
X Make a mongo db instance. (Store access creds as environment variables | Will add to path later)
X Use MongoEngine ORM to populate DB with CSV Data
X Write out data models for mongodb data
X Import data into data classes (ex. actor) for use.
API
X Create three routes. One for overall stats. One for stats based on actor name. One for a list of actor names.
Data Analytics
- Calculate analytics using data classes
Testing
- Do a pip freeze to make a requirements.txt file listing the dependencies of the app
- Write Unit Tests for Testing Database, Making a new Class, Testing out Anlytics Functions, Creating an app

Extra Features
-- Using actual templates using Jinja2 to show api info, with proper embedded css
-- Links on the home page using Flask's url_for to route to the routes listed
-- Securing API access with token or another form of Authentication ie. Oauth2
-- Secure the Local DB with Credentials

"""