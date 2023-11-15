from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# contains definitions of tables and associated schema constructs
metadata = MetaData()

# create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# define a model class by inheriting from db.Model
    # Pet class declared as subclass of db.Model
class Pet(db.Model):

    # database table is named pets
    __tablename__ = 'pets'

    # database table has 3 columns
        # id column is the primary key
        # name and species column store a string
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
