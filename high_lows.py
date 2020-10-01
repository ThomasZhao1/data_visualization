import csv

from matplotlib import pyplot as plt 
from datetime import datetime

filename = 'death_valley_2014.csv'

#Get dates, low and high temperature from file
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	dates, highs, lows = [], [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[0], '%Y-%m-%d')
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(current_date, 'has missing data')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

#Plot Data
fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(dates, highs, c = 'red', alpha = 0.5)
plt.plot(dates, lows, c = 'blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'green', alpha = 0.1)

'''
for x in range(1, len(highs)-1):
	plt.scatter(highs.index(highs[x]), highs[x], c = 'black', s = 20)


plt.scatter(highs.index(highs[0]), highs[0], c = 'blue', s = 20)
plt.scatter(highs.index(highs[-1]), highs[-1], c = 'red', s = 20)
'''


#Format Plot
plt.title("Daily Temperature of Death Valley 2014", fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

#Show plot
plt.show()



