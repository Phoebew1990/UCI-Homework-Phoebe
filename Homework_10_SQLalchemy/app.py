import numpy as np
from flask import Flask,jsonify
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func ,inspect
from dateutil.relativedelta import relativedelta
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
inspector = inspect(engine)

one_year = dt.date(2017, 8, 23) - relativedelta(months=12)



#Flask setup
app = Flask(__name__)

@app.route("/")
def home():
    
    return (
    f"All available routes:<br/>"
    f"/api/v1.0/precipitation<br/>"
    f"/api/v1.0/stations<br/>"
    f"/api/v1.0/tobs<br/>"
    f"/api/v1.0/start<br/>"
    f"/api/v1.0/start/end<br/>")
    
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Save the query results as a Pandas DataFrame and set the index to the date column
    results = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date > one_year).all()

    session.close()

    prcp = list(np.ravel(results))
  
    
    return jsonify(prcp)


@app.route("/api/v1.0/stations")
def station():
    results = session.query(Measurement.station).distinct(Measurement.station).all()

    session.close()

    station = list(np.ravel(results))
  
    
    return jsonify(station)



@app.route("/api/v1.0/tobs")
def tobs():
    active = session.query(Measurement.station,func.count(Measurement.id)).group_by(Measurement.station).order_by(func.count(Measurement.id).desc()).all()
    most_active = active[0][0]
    result = session.query(Measurement.date,Measurement.tobs).filter(Measurement.station == most_active).filter(Measurement.date > one_year).all()
    session.close()

    tobs = list(np.ravel(result))
  
    
    return jsonify(tobs)

@app.route("/api/v1.0/<start>")
def start(start):
    start = dt.datetime.strptime(start,'%Y-%m-%d')
    

    result = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).filter(Measurement.date>= start).all()
    
    session.close()

    start_trip = list(np.ravel(result))
  
    
    return jsonify(start_trip)


@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):
    start = dt.datetime.strptime(start,'%Y-%m-%d')
    end = dt.datetime.strptime(end,'%Y-%m-%d')
    #period = start - dt.timedelta(days = 365)
    #period_end = end - dt.timedelta(days = 365)

    result = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).filter(Measurement.date>= start).filter(Measurement.date<= end).all()
    
    session.close()

    start_end_trip = list(np.ravel(result))
  
    
    return jsonify(start_end_trip)





if __name__ == "__main__":
    app.run(debug=True)

    
