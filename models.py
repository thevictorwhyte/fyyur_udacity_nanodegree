from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
# from datetime import datetime
from utils import filter_past_shows

db = SQLAlchemy()
migrate = Migrate()

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=True)
    image_link = db.Column(db.String(500), nullable=True)
    facebook_link = db.Column(db.String(120), nullable=True)
    website = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, nullable=True, default=False)
    seeking_description = db.Column(db.String(), nullable=True)
    genres = db.Column(db.String(120), nullable=False)
    shows = db.relationship('Show', backref='venue', lazy=True)
   

    def __repr__(self):
        return f'<Venue {self.id} {self.name}>'

    def details_for_venue_page(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'state': self.state,
            'address': self.address,
            'phone': self.phone,
            'image_link': self.image_link,
            'facebook_link': self.facebook_link,
            'seeking_talent': self.seeking_talent,
            'seeking_description': self.seeking_description,
            'genres': json.loads(self.genres),
            'all_shows': [Show.artist_details(Show.query.get(show.id)) for show in self.shows],
            
        }

    

    
class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=True)
    image_link = db.Column(db.String(500), nullable=True)
    genres = db.Column(db.String(120), nullable=False)
    facebook_link = db.Column(db.String(120), nullable=True)
    website_link = db.Column(db.String(120), nullable=True)
    # Additions
    seeking_venue = db.Column(db.Boolean, nullable=True, default=False)
    seeking_description = db.Column(db.String(), nullable=True)
    shows = db.relationship('Show', backref='artist', lazy=True)

    def __repr__(self):
        return f'<Artist {self.id} {self.name}>'
    
class Show(db.Model):
    __tablename__ = 'Show'

    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'))
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'))
    start_time = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return f'<Show {self.id} {self.start_time}>'
    
    def artist_details(self):
        return {
            'artist_id': self.artist_id,
            'artist_name': Artist.query.get(self.artist_id).name,
            'artist_image_link': Artist.query.get(self.artist_id).image_link,
            'start_time': self.start_time.strftime("%m/%d/%Y, %H:%M:%S")
        }
