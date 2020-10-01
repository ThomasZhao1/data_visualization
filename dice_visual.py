import pygal

from die import Die 

#Create a die
die_1 = Die()
die_2 = Die()

#Make some rolls and store data in list
results = []

for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

#Analyse the results
frequencies  = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result + 1):
	frequency = results.count(value)
	frequencies.append(frequency)

#Visualize the results
hist = pygal.Bar()
hist.title = 'Results of rolling 2 dice 1000 times'
hist.x_labels = list(range(2, max_result + 1))
hist.x_title = "Result"
hist.y_title = "Frequency of Occurence"

hist.add('Dice Sum', frequencies)

#Save visualization
hist.render_to_file('dice.visual.svg')