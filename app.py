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
    director_stats = parser.topTenDirectors()

    stats = {'top_ten_genres': genre_stats, 'top_ten_directors':director_stats}

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