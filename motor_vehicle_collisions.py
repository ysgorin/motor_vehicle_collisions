# Dependencies
import pandas as pd

# Import CSV and convert to Pandas DataFrame
file_path = "Motor_Vehicle_Collisions_-_Crashes.csv"
crashes_df = pd.read_csv(file_path)

# Add Month-Day-Year Columns
crashes_df[['MONTH', 'DAY', 'YEAR']] = crashes_df['CRASH DATE'].str.split('/', expand=True)

crashes_df = crashes_df[['CRASH DATE', 'MONTH', 'DAY', 'YEAR', 'CRASH TIME', 'BOROUGH', 'ZIP CODE', 'LATITUDE',
       'LONGITUDE', 'LOCATION', 'ON STREET NAME', 'CROSS STREET NAME',
       'OFF STREET NAME', 'NUMBER OF PERSONS INJURED',
       'NUMBER OF PERSONS KILLED', 'NUMBER OF PEDESTRIANS INJURED',
       'NUMBER OF PEDESTRIANS KILLED', 'NUMBER OF CYCLIST INJURED',
       'NUMBER OF CYCLIST KILLED', 'NUMBER OF MOTORIST INJURED',
       'NUMBER OF MOTORIST KILLED', 'CONTRIBUTING FACTOR VEHICLE 1',
       'CONTRIBUTING FACTOR VEHICLE 2', 'CONTRIBUTING FACTOR VEHICLE 3',
       'CONTRIBUTING FACTOR VEHICLE 4', 'CONTRIBUTING FACTOR VEHICLE 5',
       'COLLISION_ID', 'VEHICLE TYPE CODE 1', 'VEHICLE TYPE CODE 2',
       'VEHICLE TYPE CODE 3', 'VEHICLE TYPE CODE 4', 'VEHICLE TYPE CODE 5']]

crashes_df.to_csv('motor_vehicle_collisions - date separated.csv', index=False)
