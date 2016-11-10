import numpy as np
import matplotlib.pyplot as plt
import random
import copy

def random_point2d(formula, x_range):
	x = np.array(x_range)
	y = eval(formula)
	target_y = copy.copy(y);
	plt.plot(x,target_y,'b')
	for i in range(len(y)):
		y[i] = y[i] + random.uniform(-500,500); #generating random y value
	print x
	print y
	gradient_descent(x, y, 0, 0, .000302) # 1 : x, 2 : y, 3 : initial w1, 4 : initial w2, 5 : learning rate
										  # Equation : y = w1*x + w2

def gradient_descent(x, y, w1, w2, learning_rate):
	N = len(x)
	temp_w1, temp_w2 = copy.copy(w1), copy.copy(w2)
	total_iteration = 50000
	for iteration in range(1,total_iteration): #iteration loop
		ddw1, ddw2 = 0.0, 0.0 
		for i in range(N):
			ddw1 -= (2.0/N)*(x[i] * (y[i] - (temp_w1 * x[i] + temp_w2))) # ddw1 : partial derivative for p
			ddw2 -= (2.0/N)*(y[i] - (temp_w1 * x[i] + temp_w2))
		temp_w1 = temp_w1 - learning_rate * ddw1						 #update w1, w2
		temp_w2 = temp_w2 - learning_rate * ddw2

		cost = sum([(yi - (xi * temp_w1 + temp_w2)) ** 2 for xi, yi in zip(x, y)]) / N # compute cost in each iteration
		
		if iteration % 100 == 0:
			print 'cost : ', cost, '    w1 : ', temp_w1, '    w2 : ', temp_w2
	
	minima_w1, minima_w2 = temp_w1, temp_w2
	ny = np.array(N)
	predicted_y = [None] * len(y) # [[] for _ in len(y)]
	for i in range(len(y)):
		predicted_y[i] = minima_w1 * x[i] + minima_w2; # Result 

	#plotting stuff

	plt.scatter(x,y)
	plt.plot(x,predicted_y,'r')
	plt.show()

random_point2d('x * -40 + 700', range(0, 100)) #first parameter : equation, second parameter : value of x 
