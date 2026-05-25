import pandas as pd

# -----------------------------------
# LOAD FINAL DATASET
# -----------------------------------

df = pd.read_csv("data/final_zomato_dataset.csv")

# -----------------------------------
# BASIC DATASET INFO
# -----------------------------------

print("\nDATASET SHAPE:")
print(df.shape)

print("\nCOLUMN NAMES:")
print(df.columns)

# -----------------------------------
# KPI 1 — AVERAGE DELIVERY TIME
# -----------------------------------

avg_delivery_time = df['delivery_time_min'].mean()

print("\nAVERAGE DELIVERY TIME:")
print(round(avg_delivery_time, 2), "minutes")

# -----------------------------------
# KPI 2 — AVERAGE PICKUP DELAY
# -----------------------------------

avg_pickup_delay = df['pickup_delay_min'].mean()

print("\nAVERAGE PICKUP DELAY:")
print(round(avg_pickup_delay, 2), "minutes")

# -----------------------------------
# KPI 3 — TRAFFIC IMPACT
# -----------------------------------

traffic_analysis = df.groupby('traffic_density')[
    'delivery_time_min'
].mean()

print("\nTRAFFIC IMPACT:")
print(traffic_analysis)

# -----------------------------------
# KPI 4 — WEATHER IMPACT
# -----------------------------------

weather_analysis = df.groupby('weather')[
    'delivery_time_min'
].mean()

print("\nWEATHER IMPACT:")
print(weather_analysis)

# -----------------------------------
# KPI 5 — CITY PERFORMANCE
# -----------------------------------

city_analysis = df.groupby('city')[
    'delivery_time_min'
].mean()

print("\nCITY PERFORMANCE:")
print(city_analysis)

# -----------------------------------
# KPI 6 — VEHICLE PERFORMANCE
# -----------------------------------

vehicle_analysis = df.groupby('vehicle_type')[
    'delivery_time_min'
].mean()

print("\nVEHICLE PERFORMANCE:")
print(vehicle_analysis)

# -----------------------------------
# KPI 7 — DELIVERY CATEGORY COUNT
# -----------------------------------

delivery_category_count = df['delivery_category'].value_counts()

print("\nDELIVERY CATEGORY DISTRIBUTION:")
print(delivery_category_count)