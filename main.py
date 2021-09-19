from detect_car import capture_plate
import pandas as pd

# Path to video
input_path = "Resources/Videos/Traffic1.mp4"

# 2D Matrix of license plates [[license, date]]
license_plates = capture_plate(input_path)

df = pd.read_csv("lookup_table.csv")

# Matches license plate to owner
for i in range(len(df)):
    for j in range(len(license_plates)):
        if df.iloc[i]['License Plate'] == license_plates[j][0]:
            df.loc[i, 'Most Recent Date'] = str(license_plates[j][1])
            print(f"Charging {df.iloc[i]['Owner']}...")

# Saves the time to the csv
df.to_csv("lookup_table.csv", index=False)
