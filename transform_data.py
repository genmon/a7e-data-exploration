#!/usr/bin/env python3

import csv
import json

CONTEXT_LENGTH = 1024

INPUT = "./forecasts_predictions.csv"
OUTPUT_READINGS = "./docs/data/readings.js"
OUTPUT_FORECASTS = "./docs/data/forecasts.js"

readings = []
forecasts = []

# Use a context handler to open the file and parse it as a CSV
with open(INPUT, "r") as f:
    reader = csv.reader(f)
    # Skip the header
    next(reader)
    # Iterate over the rows
    for row in reader:
        timestamp = int(row[0]) * CONTEXT_LENGTH + int(row[1])
        # This row is either a reading or a forecast
        if row[3] == 'NaN':
            # This is a reading
            reading = float(row[2])
            readings += [(timestamp, reading)]
        else:
            # This is a forecast
            forecast = float(row[3])
            forecasts += [(timestamp, forecast)]


# Write the readings to a new JSON file
with open(OUTPUT_READINGS, "w") as f:
    f.write("export const readings =\n")
    f.write(json.dumps(readings, indent=2))
    f.write(";\n")

# Write the forecasts to a new JSON file
with open(OUTPUT_FORECASTS, "w") as f:
    f.write("export const forecasts =\n")
    f.write(json.dumps(forecasts, indent=2))
    f.write(";\n")
