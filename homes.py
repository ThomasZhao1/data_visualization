import csv

from matplotlib import pyplot as plt 

filename = 'homes.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	factors = [sell_price, living_space, room_num, beds, baths] = [],[],[],[],[]

	for row in reader:
		try:
			factors[0].append(int(row[0]))
			for x in range(1, len(factors)):
				factors[x].append(float(row[x+1]))
		except ValueError:
			pass


#Plot Data
colors = ['red', 'green', 'blue', 'purple']
fig = plt.figure(dpi = 128, figsize = (10,6))
for x in range(1, len(factors)):
	plt.scatter(sell_price, factors[x], c = colors[x-1], alpha = 0.3)

#Format Plot
plt.title("Home Data Analysis", fontsize = 24)
plt.xlabel('Selling Price', fontsize = 16)
plt.ylabel('Factors', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

#Show plot
plt.show()



