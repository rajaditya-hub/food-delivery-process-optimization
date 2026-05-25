import pandas as pd
import numpy as np

# -----------------------------------
# LOAD DATASET
# -----------------------------------

file_path = "data/Zomato Dataset.csv"

df = pd.read_csv(file_path)
# -----------------------------------
# VIEW DATASET
# -----------------------------------

print("\nFIRST 5 ROWS:\n")
print(df.head())

print("\nDATASET SHAPE:\n")
print(df.shape)

print("\nCOLUMN NAMES:\n")
print(df.columns)

# -----------------------------------
# CHECK MISSING VALUES
# -----------------------------------

print("\nMISSING VALUES:\n")
print(df.isna().sum())

# -----------------------------------
# HANDLE MISSING VALUES
# -----------------------------------

# Fill age with median
df['Delivery_person_Age'] = df['Delivery_person_Age'].fillna(
    df['Delivery_person_Age'].median()
)

# Fill ratings with mean
df['Delivery_person_Ratings'] = df['Delivery_person_Ratings'].fillna(
    df['Delivery_person_Ratings'].mean()
)

# Remove rows with missing order time
df = df.dropna(subset=['Time_Orderd'])

# Fill weather with mode
df['Weather_conditions'] = df['Weather_conditions'].fillna(
    df['Weather_conditions'].mode()[0]
)

# Fill traffic density with mode
df['Road_traffic_density'] = df['Road_traffic_density'].fillna(
    df['Road_traffic_density'].mode()[0]
)

# Fill multiple deliveries with median
df['multiple_deliveries'] = df['multiple_deliveries'].fillna(
    df['multiple_deliveries'].median()
)

# Fill festival with "No"
df['Festival'] = df['Festival'].fillna("No")

# Fill city with mode
df['City'] = df['City'].fillna(
    df['City'].mode()[0]
)

# -----------------------------------
# VERIFY CLEANING
# -----------------------------------

print("\nMISSING VALUES AFTER CLEANING:\n")
print(df.isna().sum())

# -----------------------------------
# REMOVE INVALID COORDINATES
# -----------------------------------

df = df[
    (df['Restaurant_latitude'] != 0) &
    (df['Restaurant_longitude'] != 0)
]

# -----------------------------------
# SAVE CLEANED DATASET
# -----------------------------------

output_path = "data/cleaned_zomato_dataset.csv"

df.to_csv(output_path, index=False)

print("\nCLEANED DATASET SAVED SUCCESSFULLY!")
print(f"\nSaved at: {output_path}")