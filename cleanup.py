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

df = pd.read_csv('sleep_cycle_productivity.csv')
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