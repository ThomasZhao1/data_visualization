import pygal

from die import Die 

#Create a die
die = Die()

#Make some rolls and store data in list
results = []

for roll_num in range(1000):
	result = die.roll()
	results.append(result)

#Analyse the results
frequencies  = []
for value in range(1, die.num_sides + 1):
	frequency = results.count(value)
	frequencies.append(frequency)

#Visualize the results
hist = pygal.Bar()
hist.title = 'Results of rolling a die 1000 times'
hist.x_labels = list(range(1,die.num_sides + 1))
hist.x_title = "Result"
hist.y_title = "Frequency of Occurence"

hist.add('Dice', frequencies)

#Save visualization
hist.render_to_file('die.visual.svg')