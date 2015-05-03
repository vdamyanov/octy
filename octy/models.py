from octy import db

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), unique=True)
  linkedin_profile = db.relationship('LinkedinProfile', backref='user', uselist=False)

  # def __init__(self, email, linkedin_profile):
  #     self.email = email
  #     self.linkedin_profile = linkedin_profile

  # def __repr__(self):
  #     return '<User %r>' % self.username

class LinkedinProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    email = db.Column(db.String(120))
    firstname = db.Column(db.String(128)) # In consideration of Mr. Kim-Jong Sexy Glorious Beast Divine Dick Father Lovely Iron Man Even Unique Poh Un Winn Charlie Ghora Khaos Mehan Hansa Kimmy Humbero Uno Master Over Dance Shake Bouti Bepop Rocksteady Shredder Kung Ulf Road House Gilgamesh Flap Guy Theo A*** H*** Im Yoda Funky Boy Slam Duck Chuck Jorma Jukka Pekka Ryan Super Air Ooy Rusell Salvador Alfons Molgan Akta Papa Long Nameh Ek
    lastname = db.Column(db.String(128))
    headline = db.Column(db.String(255))