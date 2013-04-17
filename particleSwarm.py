#!/usr/bin/python
"""
	particleSwarm.py
	------------------------------
	* Optimize a function by means of particle swarm optimization

	* Things to add: specify some limits for the optimization

	* Velocity is updated with current velocity, a component towards 
	the best solucion each individual has obtained so far, and a component
	towards the global best solution
"""
try:
	import numpy as np
except ImportError:
	print "Error: numpy not found"

def PSO( costFunction, v_size, population, iterations = 1000, limits = list(),  debug = True):
	# Constants and variables
	Vmax = 10	# Maximum speed
	c1 = 2 		# Learning factor
	c2 = 2		# Learning factor

	i = 0		# Current iteration

	# Create vector with the limits	
	if len(limits) == 0:
		limits = v_size * [1]

	limits_vector = np.vstack( limits)

	# Create initial random population
	swarm_pos = 2 * limits_vector * ( 0.5 * np.ones(( v_size, population)) - np.random.random((v_size, population)))

	swarm_v = np.zeros( (v_size, population))

	while i < iterations:
		# Find best
		costVector = costFunction( swarm)
		pBest = costVector.argmin()  # Index of the best particle
		bestValue = costVector.min() # Cost of the best particle

		# Update speed
		swarm_v = swarm_v + c1 * np.random.random( (v_size, population)) #* best individual position - current position

	return swarm

def main():	
	try:
		import pylab as plab
	except ImportError:
		print "PyLab is not installed."

	# Define a cost function
	def cost( theta):
		#return ( 1 - theta[0][0])**2 + 100*(theta[1][0] - theta[0][0]**2)**2
		return ( theta[0][0]**2 + theta[1][0]**2)

	pass

	data = PSO( cost, 2, 100 , limits = [20, 20])
	data1 = PSO( cost, 2, 100, limits = [50, 50])
	data2 = PSO( cost, 2, 100, limits = [100, 100])
	plab.plot( data[0].tolist(), data[1].tolist(), 'b.')
	plab.plot( data1[0].tolist(), data1[1].tolist(), 'g.')
	plab.plot( data2[0].tolist(), data2[1].tolist(), 'r.')
	plab.show()

if __name__ == '__main__':
	main()
