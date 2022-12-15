
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Set up argument parser
parser = argparse.ArgumentParser()
parser.add_argument('csv_files', nargs='+')
args = parser.parse_args()

x = np.array([])
y = np.array([])

# Read data from all sensor files
for csv_file in args.csv_files:
    df = pd.read_csv(csv_file)
    x = np.append(x, pd.to_datetime(
        df['Time(dd/mm/yyyy)'], dayfirst=True).tolist())
    y = np.append(y, df['Carbon dioxide(ppm)'].tolist())

ind = np.argsort(x)
x_sorted = x[ind]
y_sorted = y[ind]

yma = pd.DataFrame(y_sorted).rolling(window=30).mean()

# Differences from moving average
diffs = y_sorted - yma[0]
diffs = diffs[~np.isnan(diffs)]

print("Standard deviation relative to total moving average = ", np.std(diffs))
print("quartiles: ", np.quantile(diffs, [0, 0.25, 0.5, 0.75, 1]))
print("95%: ", np.quantile(diffs, [0, 0.025, 0.975, 1]))

plt.hist(diffs, bins=100)
plt.show()

p = plt.plot(x_sorted, y_sorted, linestyle='', marker='o', markersize=0.5)
plt.plot(x_sorted, yma[0], color='k', alpha=0.4)
plt.show()
