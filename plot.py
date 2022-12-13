
import argparse
import pandas as pd
import matplotlib.pyplot as plt


# Plot points and moving averages
def plot_all_data(dataframes):
    for df in dataframes:
        x = pd.to_datetime(df['Time(dd/mm/yyyy)'], dayfirst=True)
        y = df['Carbon dioxide(ppm)']
        p = plt.plot(x, y, linestyle='', marker='o', markersize=0.5)

        # Plot moving average line using same color
        ma = y.rolling(window=10).mean()
        plt.plot(x, ma, color=p[0].get_color(), alpha=.5)

    plt.show()


# Plot rolling standard deviation of each sensor
def plot_rstd(dataframes):
    for df in dataframes:
        x = pd.to_datetime(df['Time(dd/mm/yyyy)'], dayfirst=True)
        y = df['Carbon dioxide(ppm)']
        rstd = y.rolling(window=10).std()
        plt.plot(x, rstd, alpha=.5)

    plt.show()


# Set up argument parser
parser = argparse.ArgumentParser()
parser.add_argument('csv_files', nargs='+')
args = parser.parse_args()

# Read csv files into dataframes
dataframes = []
for csv_file in args.csv_files:
    df = pd.read_csv(csv_file)
    dataframes.append(df)

plt.style.use('dark_background')
#plot_all_data(dataframes)
plot_rstd(dataframes)
