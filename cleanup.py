import numpy as np
import pandas as pd
import datetime 
# import matplotlib
from sklearn.preprocessing import LabelEncoder

def time_to_sec(colomName,sec):
    global df
    colom = df[colomName]
    for index, time in enumerate(colom):
        time = time * sec
        time = np.trunc(time + np.copysign(0.0, time))
        df.at[index,colomName] = int(time)
    df = df.astype({colomName:"int32"})

#inleezen van de file
df = pd.read_csv('sleep_cycle_productivity2.csv')
# null values op vullen gebuert met f/b fill neet vortige of volgede waarde om null op te vullen of het gemidelde vallue van die colom 
mean_age = df['Age'].mean()
df['Age'].fillna(mean_age, inplace=True)
df['Total Sleep'].fillna(df['Total Sleep'].mean(), inplace=True)
df['Exercise(mins/day)'].fillna(df['Exercise(mins/day)'].mean(), inplace=True)
df['Caffeine Intake (mg)'].fillna(df['Caffeine Intake (mg)'].mean(), inplace=True)
df['Screen Time Before Bed (mins)'].fillna(df['Screen Time Before Bed (mins)'].mean(), inplace=True)
df['Work Hours (hrs/day)'].fillna(df['Work Hours (hrs/day)'].mean(), inplace=True)
df['SleepQ'].bfill(method='bfill', inplace=True)
df['Gender'].ffill(inplace=True)

#fearue engeniering 
df = df.drop_duplicates()
df = df.drop(columns="Date")
df = df.drop(columns="Person_ID")
df = df.drop(columns="Sleep Start Time")
df = df.drop(columns="Sleep End Time")
label_encoder = LabelEncoder()
df['Gender'] = label_encoder.fit_transform(df['Gender'])
time_to_sec("Work Hours (hrs/day)",3600)
time_to_sec("Total Sleep",3600)

time_to_sec("Screen Time Before Bed (mins)",60)
time_to_sec("Exercise(mins/day)",60)
df["Age"].value_counts

import matplotlib.pyplot as plot
# Visualize the dataframe
df.hist(bins=5, figsize=(20, 15))
plot.show()

# Visualize the correlation between two stats
x = 'Screen Time Before Bed (mins)'
y = 'Mood Score'
correlation = df[x].corr(df[y])

# Print the number of null values in df
print(df.isnull().sum())

# # Scatter plot to visualize the correlation
# df.plot(kind='hexbin', x=x, y=y, alpha=0.5)
# plot.title(f"Correlation between {x} and {y}")
# plot.xlabel(x)
# plot.ylabel(y)
# plot.show()