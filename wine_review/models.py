from .app import db

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,func

dbfile = os.path.join('raw_data/wine_reviews.sqlite')
engine = create_engine(f"sqlite:///{dbfile}")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save references to each table
wine_reviews = Base.classes.reviews 
# Create our session (link) from Python to the Database
session = Session(engine)