from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///F1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# need db to import models
import models


# home route
#This is what sends you to the home page.
@app.route('/')
def home():
    return render_template('home.html', page_title='Home')

# list all the Teams
#By Clicking this  
@app.route('/all_teams')
def all_teams():
    teams = models.team.query.all()
    return render_template('all_teams.html', page_title="All Teams", teams=teams)

# details of one team
@app.route('/team/<int:id>')
def teams(id):
    team = models.team.query.filter_by(id=id).first()
    drivers = models.driver.query.all()
    team_drivers = []
    for driver in drivers:
      if driver.team == id:
        team_drivers.append(driver)
      elif team == None:
        return render_template("404.html", page_title="ERROR")
    name = team.name
    return render_template('team.html', page_title=name, team=team, drivers=team_drivers)

# list all the Drivers
@app.route('/all_drivers')
def all_drivers():
    drivers = models.driver.query.all()
    return render_template('all_drivers.html', page_title="All Drivers", drivers=drivers)

#details of one driver Fail, This is a copy of the details of one team but found it easier just to add the teams in the data base where you cant click on the team to take you too the team because it was easier to do it that way.
'''@app.route('/driver/<int:id>')
def drivers(id):
    driver = models.driver.query.filter_by(id=id).first()
    teams = models.team.query.all()
    driver_teams = []
    for team in teams:
      if team.driver == id:
        driver_teams.append(team)
    name = driver.name
    return render_template('driver.html', page_name=name, driver=driver, teams=driver_teams)'''

# details of one driver
@app.route('/driver/<int:id>')
def driver(id):
    driver = models.driver.query.filter_by(id=id).first()
    if driver == None:
        return render_template("404.html", page_title="ERROR")
    name = driver.name
    return render_template('driver.html', page_title=name, driver=driver)

# list all the tracks
@app.route('/all_tracks')
def all_tracks():
    tracks = models.track.query.all()
    return render_template('all_tracks.html', page_title="All Tracks", tracks=tracks)

# details of one track
@app.route('/track/<int:id>')
def track(id):
    track = models.track.query.filter_by(id=id).first()
    if track == None:
        return render_template("404.html", page_title="ERROR")
    name = track.name
    return render_template('track.html', page_title=name, track=track)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
