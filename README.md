
# How reliable are my Aranet4 CO2 sensor measurements?

![seven sensors](sensors.jpg)
## Seven sensors for seven days
- Measure a residential hallway, with all sensors exposed to the same indoor air in parallel.  The number of people and pets in the house varied over time. There was occasional gas-flame cooking in a neighboring room.  Most activity did not occur in direct proximity to the sensors.
- Device settings:
    - Sensor hardware `rev 12`
    - Firmware `v0.4.14`
    - Measurement interval: `2 minutes`
- After seven days, downloaded `.csv` files from all seven sensors using Aranet4 app.
- Raw data is [here](data/week2)

## Let's plot a week of data

`$ python plot.py data/week2/*.csv`

![Full week](week2-plot.png)

![Zoomed](zoomed.png)

A zoomed-in section of this plot shows a 10-point (20 minute) moving average superimposed onto the individually measured points. It can be seen at a glance that measurements between different sensors vary from each other between zero and 100 ppm.

What is the rolling standard deviation for each sensor with respect to its 10-point moving average? 
![Rolling standard deviation](rolling-standard-deviation.png)
 Standard deviation of each sensor is typically around 10 ppm.

 ## Combining all the data

 How much do readings vary between all sensors?  If we take the differences between each reading and the moving average across all sensors at that time, we get a distribution that looks like this:

 ![Difference distribution](differences-distribution.png)

The standard deviation of these differences from the total rolling mean is ~22 ppm.

## Conclusion

We expect roughly 95% of Aranet4 measurements to be consistent between each other within +/- 22 ppm


## Feedback please!
Does this conclustion seem reasonable?  Check the data, and the code and let me know.

