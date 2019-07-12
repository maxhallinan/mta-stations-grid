#!/usr/bin/env python
import csv
import json
import math
import sys 

with open("./stations.csv") as source_file, \
        open("./points.json", "w") as target_file:
    reader = csv.reader(source_file, delimiter=",")
    # writer = csv.writer(target_csv, delimiter=",")

    # skip header row
    next(reader)

    points = {}

    for r in reader:
        id = r[0]
        x = abs(float(r[9]))
        y = abs(float(r[10]))

        coordinates = {}
        coordinates['x'] = x
        coordinates['y'] = y
        point = {}
        point['id'] = id
        point['coordinates'] = coordinates

        points[id] = point

    json.dump(points, target_file)
