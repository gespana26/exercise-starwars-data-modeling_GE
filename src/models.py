import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    Id_user = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    Last_name = Column(String(50), nullable=False)
    Email = Column(String(60), nullable=False, unique=True)
    Username = Column(String(30), nullable=False, unique=True)
    Password = Column(String(30), nullable=False, )
    Creation_= Column(String(30), nullable=False, )

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    Id = Column(Integer, primary_key=True)
    Id_user = Column(Integer, ForeignKey('user.Id_user'))
    Id_people = Column(Integer, ForeignKey('people.Id_people'))
    Id_planet = Column(Integer, ForeignKey('planet.Id_planet'))
    Id_starship = Column(Integer, ForeignKey('starships.Id_starship'))



class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    Id_people = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    Gender = Column(Integer)
    Birth_year = Column(Integer)
    Eye_color = Column(Integer)
    Hair_color = Column(Integer)
    Mass = Column(String(50))
    Skin_color = Column(String(50))
    Homeworld = Column(Integer)
    Id_planet = Column(Integer, ForeignKey('planet.Id_planet'))
    Id_starship = Column(Integer, ForeignKey('starships.id_starship'))


class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    Id_planet = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False, unique=True)
    Diameter = Column(Integer)
    Rotation_period = Column(Integer)
    Orbital_period = Column(Integer)
    Population = Column(Integer)
    Climate = Column(String(50))
    Terrain = Column(String(50))
    Id_people = Column(Integer)



class Starships(Base):
    __tablename__ = 'starships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    Id_starship = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False, unique=True)
    Model = Column(String(50), nullable=False, unique=True)
    Starship_class = Column(String(100))
    Manufacturer = Column(String(100))
    Cost_in_credits = Column(Integer)
    Length = Column(Float)
    Crew = Column(Integer)
    Passengers = Column(Integer)
    Max_atmosphering_speed = Column(Integer)
    Hyperdrive_rating = Column(Float)
    Cargo_capacity = Column(String(250), nullable=False)
    Consumables = Column(String(250), nullable=False)



def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram1.png')
