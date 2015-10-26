"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.

Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(name="Corvette", brand_name="Chevrolet").all()

# Get all models that are older than 1960.
Model.query.filter(Model.year > "1960").all()
# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > "1920").all()
# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like("Cor%")).all()
# Get all brands with that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == "1903", Brand.discontinued.is_(None)).all()
# Get all brands with that are either discontinued or founded before 1950.
##db.or_ if we didnt put this the default would be "AND" "OR Statement"
Brand.query.filter(db.or_(Brand.discontinued.isnot(None), Brand.founded < "1950")).all()
#getting an error: UnicodeEncodeError: 'ascii' codec can't encode character u'\xeb' in position 22: ordinal not in range(128)
# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != "Chevrolet").all()
#error: UnicodeEncodeError: 'ascii' codec can't encode character u'\xeb' in position 38: ordinal not in range(128)

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    model_info = Model.query.filter_by(year=year).all()

    for model in model_info:
        print "Model: %s, brand_name:%s, headquarters:%s" % (model.name, model.brand_name, model.brand.headquarters)
        #need to go over this problem for I didnt understand the last loop.


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''


    ##need help doing this one as well

# -------------------------------------------------------------------


# # Part 2.5: Advanced and Optional
# def search_brands_by_name(mystr):
#     pass


# def get_models_between(start_year, end_year):
    # pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
#return all vehicles that have the brand name ford. However it is missing .all, so right now
#its just a statement.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
#Answer- an association table manages relationships, this is were we are able to use 
#foreign keys and be able to navigate across tables once relationships are established.
