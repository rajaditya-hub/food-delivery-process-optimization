import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------
# LOAD FINAL DATASET
# -----------------------------------

df = pd.read_csv("data/final_zomato_dataset.csv")

# -----------------------------------
# CHART 1 — TRAFFIC IMPACT
# -----------------------------------

traffic_analysis = df.groupby('traffic_density')[
    'delivery_time_min'
].mean()

plt.figure(figsize=(8,5))
traffic_analysis.plot(kind='bar')

plt.title("Traffic Density vs Average Delivery Time")
plt.xlabel("Traffic Density")
plt.ylabel("Average Delivery Time (min)")

plt.tight_layout()

plt.savefig("visuals/traffic_impact.png")

plt.close()

# -----------------------------------
# CHART 2 — WEATHER IMPACT
# -----------------------------------

weather_analysis = df.groupby('weather')[
    'delivery_time_min'
].mean()

plt.figure(figsize=(8,5))
weather_analysis.plot(kind='bar')

plt.title("Weather Conditions vs Delivery Time")
plt.xlabel("Weather")
plt.ylabel("Average Delivery Time (min)")

plt.tight_layout()

plt.savefig("visuals/weather_impact.png")

plt.close()

# -----------------------------------
# CHART 3 — DELIVERY CATEGORY
# -----------------------------------

delivery_category = df['delivery_category'].value_counts()

plt.figure(figsize=(6,6))
delivery_category.plot(kind='pie', autopct='%1.1f%%')

plt.title("Delivery Category Distribution")

plt.ylabel("")

plt.tight_layout()

plt.savefig("visuals/delivery_category.png")

plt.close()

# -----------------------------------
# CHART 4 — VEHICLE PERFORMANCE
# -----------------------------------

vehicle_analysis = df.groupby('vehicle_type')[
    'delivery_time_min'
].mean()

plt.figure(figsize=(8,5))
vehicle_analysis.plot(kind='bar')

plt.title("Vehicle Type vs Delivery Time")
plt.xlabel("Vehicle Type")
plt.ylabel("Average Delivery Time (min)")

plt.tight_layout()

plt.savefig("visuals/vehicle_performance.png")

plt.close()

print("Visualizations created successfully!")