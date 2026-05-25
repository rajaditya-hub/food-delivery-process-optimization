import pandas as pd
import numpy as np

# -----------------------------------
# LOAD CLEANED DATASET
# -----------------------------------

df = pd.read_csv("data/cleaned_zomato_dataset.csv")
print(df.columns)

# -----------------------------------
# RENAME COLUMNS
# -----------------------------------

df.rename(columns={
    'ID': 'order_id',
    'Delivery_person_ID': 'rider_id',
    'Delivery_person_Age': 'rider_age',
    'Delivery_person_Ratings': 'rider_rating',
    'Restaurant_latitude': 'restaurant_lat',
    'Restaurant_longitude': 'restaurant_long',
    'Delivery_location_latitude': 'delivery_lat',
    'Delivery_location_longitude': 'delivery_long',
    'Order_Date': 'order_date',
    'Time_Orderd': 'order_time',
    'Time_Order_picked': 'pickup_time',
    'Weather_conditions': 'weather',
    'Road_traffic_density': 'traffic_density',
    'Vehicle_condition': 'vehicle_condition',
    'Type_of_order': 'order_type',
    'Type_of_vehicle': 'vehicle_type',
    'multiple_deliveries': 'multiple_deliveries',
    'Festival': 'festival',
    'City': 'city',
    'Time_taken (min)': 'delivery_time_min'
}, inplace=True)

# -----------------------------------
# CONVERT TIME COLUMNS
# -----------------------------------

# -----------------------------------
# HANDLE MIXED TIME FORMATS
# -----------------------------------

def convert_time(value):
    try:
        # If value is numeric (Excel decimal time)
        if isinstance(value, (float, int)):
            return pd.to_datetime(value, unit='D', origin='1899-12-30')

        # Otherwise parse normal HH:MM format
        return pd.to_datetime(value, format='%H:%M')

    except:
        return pd.NaT

df['order_time'] = df['order_time'].apply(convert_time)
df['pickup_time'] = df['pickup_time'].apply(convert_time)

# Remove rows where conversion failed
df = df.dropna(subset=['order_time', 'pickup_time'])

# -----------------------------------
# CREATE PICKUP DELAY
# -----------------------------------

df['pickup_delay_min'] = (
    df['pickup_time'] - df['order_time']
).dt.total_seconds() / 60

# -----------------------------------
# FIX NEGATIVE TIME VALUES
# -----------------------------------

df['pickup_delay_min'] = df['pickup_delay_min'].apply(
    lambda x: x + 1440 if x < 0 else x
)

# -----------------------------------
# CREATE DELAY CATEGORY
# -----------------------------------

def classify_delay(time):
    if time < 20:
        return 'Fast'
    elif time < 40:
        return 'Moderate'
    else:
        return 'Delayed'

df['delivery_category'] = df['delivery_time_min'].apply(classify_delay)

# -----------------------------------
# SAVE FEATURED DATASET
# -----------------------------------

df.to_csv("data/featured_zomato_dataset.csv", index=False)

print("Feature engineering completed successfully!")