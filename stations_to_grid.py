#!/usr/bin/env python
import csv
import math

# for example
grid_scale_x = 316
grid_scale_y = 400

with open("./stations.csv") as source_csv, \
        open("./points.csv", "w") as target_csv:
    reader = csv.reader(source_csv, delimiter=",")
    writer = csv.writer(target_csv, delimiter=",")

    # skip header row
    next(reader)

    originals = []
    original_xs = []
    original_ys = []

    for r in reader:
        id = r[0]
        original_x = abs(float(r[9]))
        original_y = abs(float(r[10]))

        original_xs.append(original_x)
        original_ys.append(original_y)
        originals.append((id, original_x, original_y))

    min_x = min(original_xs)
    max_x = max(original_xs)

    min_y = min(original_ys)
    max_y = max(original_ys)

    original_scale_x = max_x - min_x
    original_scale_y = max_y - min_y

    dimensioned  = []
    dimensioned_xs = []
    dimensioned_ys = []

    for o in originals:
        id = o[0]
        original_x = o[1]
        original_y = o[2]

        dimensioned_x = math.floor(original_x / original_scale_x * grid_scale_x)
        dimensioned_y = math.floor(original_y / original_scale_y * grid_scale_y)

        dimensioned_xs.append(dimensioned_x)
        dimensioned_ys.append(dimensioned_y)
        dimensioned.append((id, dimensioned_x, dimensioned_y))

    dimensioned_x_min = min(dimensioned_xs)
    dimensioned_y_min = min(dimensioned_ys)

    points = []

    for d in dimensioned:
        id = d[0]
        point_x = int(d[1] - dimensioned_x_min)
        point_y = int(d[2] - dimensioned_y_min)

        writer.writerow([id, point_x, point_y])

    
