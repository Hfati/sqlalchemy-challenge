from flask import Flask, jsonify
import pandas as pd
import numpy as np
from sqlHelper import SQLHelper

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
sql = SQLHelper()

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation_orm<br/>"
        f"/api/v1.0/precipitation_raw<br/>"
        f"/api/v1.0/2016-08-23<br/>"
        f"/api/v1.0/2016-08-23/2016-12-31"
    )

# SQL Queries
@app.route("/api/v1.0/precipitation_orm")
def passengers_orm():
    data = sql.query_precipitation_orm()
    return(jsonify(data))

@app.route("/api/v1.0/precipitation_raw")
def passengers_raw():
    data = sql.query_precipitation_raw()
    return(jsonify(data))

# start should be in format 2016-08-23
@app.route("/api/v1.0/<start>")
def tobs_start_orm(start):
    data = sql.query_tobs_start_orm(start)
    return(jsonify(data))

# start should be in format 2016-08-23
@app.route("/api/v1.0/<start>/<end>")
def tobs_start_end_raw(start, end):
    data = sql.query_tobs_start_end_raw(start, end)
    return(jsonify(data))


# Run the App
if __name__ == '__main__':
    app.run(debug=True)
