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
- [x] Initialize Folder into a git repo
- [x] Create virtualenv and install packages | Flask, Pandas, PyMongo, & MongoEngine are key here
- [x] Checkout a branch from master per feature and merge them into master as you work. (Typical branch flow dev_feature -> qa -> prod)
- [x] Created 3 branches far_data_access, far_analytics far_testing and merged them in however only pushed master to github
- [x] Plan app architecture into simple blueprint like folders based on function (No need to use flask blueprints)

### Data Management
- [x] Make a mongo db instance. (Store access creds as environment variables | Will add to path later)
- [x] Use MongoEngine ORM to populate DB with CSV Data
- [x] Write out data models for mongodb data
- [x] Import data into data classes (ex. actor) for use.

### REST API
- [x] Create route for overall top ten stats. 
- [x] Create route for stats based on actor name. 
- [x] Create route for a list of actor names.

### Data Analytics
- [x] Top Genres in Decreasing Order of Profitability
- [x] Top Directors in Decreasing Order of Profitability
- [x] Calculate a actor's most profitable movie

### Testing
- [x] Do a pip freeze to make a requirements.txt file listing the dependencies of the app
- [x] Write Unit Tests for Testing Database, Making a new Class, Testing out Anlytics Functions, Creating an app

### Extra Features (Future)
 - [ ]  Fix unicode random character issues for fields like movie and actor names before importing the data into the database.
 - [ ]  Using actual templates using Jinja2 to show api info, with proper embedded css
 - [ ]  Links on the home page using Flask's url_for to route to the routes listed
 - [ ]  Securing API access with token or another form of Authentication ie. Oauth2
 - [ ]  Secure the Local DB with Credentials