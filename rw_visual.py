import matplotlib.pyplot as plt 

from random_walk import RandomWalk

#Make a random walk and plot the points
#Keep making 
while True:
	rw = RandomWalk(50000)
	rw.fill_walk()

	#Set size of plot window
	plt.figure(dpi = 128, figsize = (10,6))

	plt.title("A Random Walk", fontsize = 24)

	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, 
		edgecolor = 'none', s = 15)

	#Emphasize first and last points
	plt.scatter(0,0, c='green', edgecolors = 'none', s = 50)
	plt.scatter(rw.x_values[-1],rw.y_values[-1], c='red', edgecolors = 'none', 
		s = 50)

	#Make both axes invisible
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)

	#Show graph (Should be last line of code)
	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break