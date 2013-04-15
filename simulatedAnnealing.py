#!/usr/bin/python
"""
	simulatedAnnealing.py
	------------------------------
	* Optimize a function by means of simulated annealing
"""

# Import NumPy
try:
	import numpy as np	
except ImportError:
	print "Error: NumPy is not installed"
	exit()


def simulatedAnnealing( costFunction, theta, T_init, T_end, cool_rate, iterations, debug = False):
	n = 0
	m = theta.size
	temp = float(T_init)
	alpha = 2 * 0.5 # Maximun random displacement
	initialCost = costFunction(theta)

	# Debug
	if debug:
		costHistory = [ initialCost ]
		tempHistory = [ T_init]
		positions = [ [theta[0][0]], [theta[1][0]] ]


	while (temp > T_end and n < iterations):
		# Calculate the new random movement
		rand_move = alpha *(0.5*np.ones( (m, 1)) - np.random.random( (m, 1) ) )
		#angle = 2 * np.pi * np.random.random( (1, 1))[0][0]
		#rand_move = np.array( [ [np.cos( angle)], [np.sin(angle)]])
		
		currentCost = costFunction( theta + rand_move )
		costMove = currentCost - initialCost

		# Check if the movement will be accepted at this temperature
		if acceptMovement( costMove, temp):
			theta += rand_move
			initialCost = currentCost
		
		# Cooling
		# Linear cooling
		temp = T_init - ( (T_init-T_end) / float(iterations) ) * n;
		
		# Geometric cooling
		#temp = T_init * (cool_rate)**(n)

		# Register debug data
		if debug:	
			costHistory.append( initialCost)
			tempHistory.append( temp)
			positions[0].append( theta[0][0])
			positions[1].append( theta[1][0])

		n+=1

	if debug:
		return theta, costHistory, tempHistory, positions
	else:
		return theta

def acceptMovement( costMove, temp, k = 1):
	return  costMove < 0 or (costMove >= 0 and np.random.random(1)[0] < np.exp( -costMove / (k * temp)))



def main():

	try:
		import pylab as plab
	except ImportError:
		print "PyLab is not installed."

	# Define a cost function
	def cost( theta):
		#return ( 1 - theta[0][0])**2 + 100*(theta[1][0] - theta[0][0]**2)**2
		return ( theta[0][0]**2 + theta[1][0]**2)

	
	# Initial guess
	#theta = np.array( [ [0.], [0.] ])
	theta = 100* (0.5* np.ones( (2,1)) - np.random.random( (2, 1)) )

	# Run the simulated annealing
	theta , costHistory, tempHistory , pos = simulatedAnnealing( cost, theta, 2000, 0, 0.999, 15000, True)

	# Result:
	print "Point: " + str(theta[0][0]) + ' , ' + str( theta[1][0] )
	print "Cost: " + str( costHistory[-1] )

	# Print results:
	if True:
		plab.figure()
		plab.plot( range(0,len(costHistory)), costHistory, 'b.')
		plab.title( "Cost over time")
	
	if True:
		plab.figure()
		plab.plot( range(0,len(tempHistory)), tempHistory, 'r.')
		plab.title( "Temperature over time")
	if True:
		plab.figure()
		plab.plot( pos[0][:5000], pos[1][:5000], 'g.')
		plab.plot( pos[0][5000:10000], pos[1][5000:10000], 'y.')
		plab.plot( pos[0][10000:], pos[1][10000:], 'k.')
		plab.plot( pos[0][-1], pos[1][-1], 'b*')
		plab.plot( pos[0][0], pos[1][0], 'r*')
		plab.title( "Travel")

	plab.show()

if __name__ == '__main__':
	main()
