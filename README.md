# IMDB Data Analytics App
- This a REST API made using Flask that returns different interesting pieces of information using the IMDB dataset

### Requirements
- Python 3.x.x
- Flask
- MongoEngine

### Clone Repo & Run the App
git clone git@github.com:DataMovie.git
cd DataMovie
python app.py

______

## My Steps to Develop this App

### Starting
X Initialize Folder into a git repo
X Create virtualenv and install packages | Flask, Pandas, PyMongo, & MongoEngine are key here
X Checkout a branch from master per feature and merge them into master as you work. (Typical branch flow dev_feature -> qa -> prod)
X Plan app architecture into simple blueprint like folders based on function (No need to use flask blueprints)

### Data Management
X Make a mongo db instance. (Store access creds as environment variables | Will add to path later)
X Use MongoEngine ORM to populate DB with CSV Data
X Write out data models for mongodb data
X Import data into data classes (ex. actor) for use.

### REST API
X Create route for overall top ten stats. 
X Create route for stats based on actor name. 
X Create route for a list of actor names.

### Data Analytics
X Top Genres in Decreasing Order of Profitability
X Top Directors in Decreasing Order of Profitability
X Calculate a actor's most profitable movie

### Testing
X Do a pip freeze to make a requirements.txt file listing the dependencies of the app
- Write Unit Tests for Testing Database, Making a new Class, Testing out Anlytics Functions, Creating an app

### Extra Features (Future)
-- Fix unicode random character issues for fields like movie and actor names before importing the data into the database.
-- Using actual templates using Jinja2 to show api info, with proper embedded css
-- Links on the home page using Flask's url_for to route to the routes listed
-- Securing API access with token or another form of Authentication ie. Oauth2
-- Secure the Local DB with Credentials