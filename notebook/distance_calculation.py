import pandas as pd
import numpy as np
from math import radians, cos, sin, sqrt, atan2

# -----------------------------------
# LOAD FEATURED DATASET
# -----------------------------------

df = pd.read_csv("data/featured_zomato_dataset.csv")

# -----------------------------------
# HAVERSINE FUNCTION
# -----------------------------------

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in KM

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c

# -----------------------------------
# CALCULATE DISTANCE
# -----------------------------------

df['distance_km'] = df.apply(
    lambda row: haversine(
        row['restaurant_lat'],
        row['restaurant_long'],
        row['delivery_lat'],
        row['delivery_long']
    ),
    axis=1
)

# -----------------------------------
# CREATE DELIVERY EFFICIENCY
# -----------------------------------

df['delivery_efficiency'] = (
    df['distance_km'] / df['delivery_time_min']
)

# -----------------------------------
# SAVE FINAL DATASET
# -----------------------------------

df.to_csv("data/final_zomato_dataset.csv", index=False)

print("Distance calculation completed successfully!")