#!/usr/bin/python
"""
	particleSwarm.py
	------------------------------
	* Optimize a function by means of particle swarm optimization

	* Things to add: specify some limits for the optimization

	* Velocity is updated with current velocity, a component towards 
	the best solucion each individual has obtained so far, and a component
	towards the global best solution.
"""
try:
	import numpy as np
except ImportError:
	print "Error: numpy not found"

def PSO( costFunction, v_size, population, iterations = 1000, limits = list(),  debug = False):
	# Constants and variables
	Vmax = 10	# Maximum speed
	c1 = 2 		# Learning factor
	c2 = 2		# Learning factor

	i = 0		# Current iteration

	# Create vector with the limits	
	if len(limits) == 0:
		limits = v_size * [1]

	limits_vector = np.vstack( limits)

	# Storage for the particles
	particles_p = list()
	particles_v = list()

	pBest = list()
	pBest_value = list()

	gBest = None
	gBest_value = None

	# Create initial random population
	for index in range(0, population):
		particles_p.append( 2 * limits_vector * ( 0.5 * np.ones(( v_size, 1)) - np.random.random((v_size, 1))) )
		particles_v.append( np.zeros( (v_size, 1) ) )
		
		pBest.append( particles_p[-1] )
		pBest_value.append( costFunction( pBest[-1]) )
	
	#Set an initial value for the best element:
	gBest = pBest[0]
	gBest_value = pBest_value[0]
	
	# Main loop
	# -------------------------------------------------------------------------------------------
	# While current iteration lower that max iterations and current cost is higher that threshold
	while i < iterations:
		# Find local best & global best
		for index in range( 0, population):
			cost = costFunction( particles_p[index] )
	
			# Find personal best
			if cost < pBest_value[index]:
				pBest_value[index] = cost
				pBest[index] = particles_p[index]

			# Find global best
			if cost < gBest_value:
				gBest_value = cost
				gBest = particles_p[index]


		# Update speed
		for index in range(0, population):
			particles_v[index] = particles_v[index] + c1 * np.random.random(1)[0] * ( pBest[index] - particles_p[index]) + c2 * np.random.random(1)[0] * ( gBest - particles_p[index])
			particles_p[index] = particles_p[index] + particles_v[index]
							
			
		# swarm_v = swarm_v + c1 * np.random.random( (v_size, population)) #* best individual position - current position
		i += 1

	if debug:
		return particles_p, pBest, gBest
	else:
		return gBest

def main():	
	try:
		import pylab as plab
	except ImportError:
		print "PyLab is not installed."

	# Define a cost function
	def cost( theta):
		return ( 1 - theta[0][0])**2 + 100*(theta[1][0] - theta[0][0]**2)**2
		#return ( theta[0][0]**2 + theta[1][0]**2)

	pass

	swarm, pBest, gBest = PSO( cost, 2, 20, 200 , limits = [20, 20], debug = True)

	print 'Best individual is: (' + str( gBest[0][0]) + ',' + str( gBest[1][0] ) + ')'

	plotswarm = [ [], []]
	plotpBest = [ [], []]
	plotgBest = [ [], []]
	
	for thing in swarm:
		plotswarm[0].append( thing[0] )
		plotswarm[1].append( thing[1] )

	for thing in pBest:
		plotpBest[0].append( thing[0] )
		plotpBest[1].append( thing[1] )

		
	plab.plot( plotswarm[0], plotswarm[1], 'b*')
	plab.plot( plotpBest[0], plotpBest[1], 'y*')
	plab.plot( gBest[0], gBest[1], 'r*')
	plab.show()

if __name__ == '__main__':
	main()
