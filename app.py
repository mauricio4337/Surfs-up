# IMPORT DEPENDENCIES

import datetime as dt
import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


####################
# SQL DATABASE SETUP
####################

engine = create_engine("sqlite:///hawaii.sqlite")
# Reflect existing database into a model
Base = automap_base()
# Reflect tables
Base.prepare(engine, reflect=True)
# Save references to each table 
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create session from python to our DB
session = Session(engine)


####################
# FLASK SETUP
####################
app = Flask(__name__)
@app.route('/')

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:<br/>
    /api/v1.0/precipitation<br/>
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/temp/start/end
    ''')

if __name__ == 'main':
    app.run(debug=True)

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Return the precipitation data for the previous year
    # Calculate the date one year from the last date in data set.
    prev_year = dt.date(2017, 8, 3) - dt.timedelta(days=365)
    # Perform a query to retrieve the data and precipitation scores
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()

    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

@app.route("/api/v1.0/stations")
def stations():
    # Return a list of stations
    results = session.query(Station.station).all()

    station = list(np.ravel(results))

    return jsonify(stations = station)


@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
                filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps = temps)
    
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
    
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


    # Save the query results as a Pandas DataFrame and set the index to the date column
    #df = pd.DataFrame(results, columns=['date', 'precipitation'])
    #df.set_index(df['date'], inplace=True)



#def hello_world():
#	return 'Hello world'
