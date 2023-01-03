
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import re

# Plot points and moving averages
def plot_all_data(dataframes, sensor_ids):
    for idx, df in enumerate(dataframes):
        x = pd.to_datetime(df['Time(dd/mm/yyyy)'], dayfirst=True)
        y = df['Carbon dioxide(ppm)']
        color = 'k' if sensor_ids[idx][0] == 'p' else None
        p = plt.plot(x, y, linestyle='', marker='o', color=color, markersize=0.5, label=sensor_ids[idx])

        # Plot moving average line using same color
        ma = y.rolling(window=10).mean()
        plt.plot(x, ma, color=p[0].get_color(), alpha=.5)

    plt.legend()
    plt.show()


# Plot rolling standard deviation of each sensor
def plot_rstd(dataframes, sensor_ids):
    for idx, df in enumerate(dataframes):
        x = pd.to_datetime(df['Time(dd/mm/yyyy)'], dayfirst=True)
        y = df['Carbon dioxide(ppm)']
        rstd = y.rolling(window=10).std()
        color = 'k' if sensor_ids[idx][0] == 'p' else None
        plt.plot(x, rstd, alpha=.5)

    plt.show()


# Set up argument parser
parser = argparse.ArgumentParser()
parser.add_argument('csv_files', nargs='+')
args = parser.parse_args()

# Read csv files into dataframes
dataframes = []
sensor_ids = []
for csv_file in args.csv_files:
    m = re.search('^(.*)/(.+)_(.*)T(.*)$', csv_file) # Expected to be in subdirectory
    if (m):
        sensor_ids.append(m.group(2))
    else:
        print("sensor name not found in pathname", csv_file)
    df = pd.read_csv(csv_file)
    dataframes.append(df)

#import pdb; pdb.set_trace()

# plt.style.use('dark_background')
plot_all_data(dataframes, sensor_ids)
#plot_rstd(dataframes, sensor_ids)
