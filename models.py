from main import db

class driver(db.Model):
    __tablename__ = 'driver'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable = False)
    number = db.Column(db.Integer)
    team_name = db.Column(db.String(250))
    nationality = db.Column(db.String(50))
    races = db.Column(db.Integer)
    wins = db.Column(db.Integer)
    podiums = db.Column(db.Integer)
    image = db.Column(db.String)
    team = db.Column(db.Integer, db.ForeignKey('team.id'))
    number_image = db.Column(db.String)
    flag = db.Column(db.String)
    team_image = db.Column(db.String)
    fact = db.Column(db.String)
  


class team(db.Model):
    __tablename__ = 'team'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable = False)
    hq = db.Column(db.String(250))
    chief = db.Column(db.String(250))
    team_image = db.Column(db.String)
    car = db.Column(db.String)
    position = db.Column(db.String)

class track(db.Model):
    __tablename__ = 'track'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable = False)
    gp = db.Column(db.String)
    description = db.Column(db.String(500))
    image = db.Column(db.String)
    races = db.Column(db.Integer)
    built = db.Column(db.Integer)
    country = db.Column(db.String)
    location = db.Column(db.String)
    flag = db.Column(db.String)
    lap = db.Column(db.String)