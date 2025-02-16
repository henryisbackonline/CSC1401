#----------------------------------------------
# Practice 2 (Lessons 2)
#
# Fill in the code for the functions below. main() is already set up
# to test your functions with a few different inputs.
# 
# The test() function will print 'OK' when your function 
# returns the expected output.
# 
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
#----------------------------------------------

#----------------------------------------------
# Examples: solutions provided
# 	The two examples below have been provided to demostrate how you should
#   complete the remainder of the quiz functions.  
#----------------------------------------------

# Use + operator to concatenate and return the two strings a and b
def a_plus_b(a, b):
	""" Concatenates two strings a and b, returns string
	"""
	ab = a + b
	return ab
    
# Calculate and return the area of a rectangle for any given width and length  
def area_rectangle(width, length):
	""" Calculates the area of a rectangle for any given width(w) and length(l),
	returns float
	"""
	area = 1.0 * width * length
	return area
    
    
#----------------------------------------------
# Part A:  Calculate
#   Write functions to compute answers for Exercise 1.4 Q1-3
#   Remember to add an appropriate docstring
#----------------------------------------------
import math

# Exercise 1.4 Question 1
# Calculate the volume of a sphere, given its radius:
#   return an integer value for the volume
#   Note: use math.pi to get the value of pi
def volume_sphere(r):
	""" Add appropriate docstring
	"""
	# your code here	
	return

# Exercise 1.4 Question 2
# Calculate and return the total wholesale cost for an order of books to the 
# nearest whole dollar, given:
#   quantity ordered, cover price, discount, shipping cost for 1st copy,
#   shipping cost for each additional copy
 
def wholesale_cost(quantity, price, discount, ship_first, ship_extra):
	""" Add appropriate docstring
	"""
	# your code here	
	return
    
# Exercise 1.4 Question 3
#   Calculate and return a runner's total run time in minutes given the distance and pace 
#   for each section of their run.  The function total_run_time should use 
#   the run_time function to calculate the time for each section of the run, 
#   and return their sum.
#   The units for pace is time/distance (8.15 per mile).
#
#   Run Details (from Lesson 1 Exercise 1.4 Question 3)
#   .... run 1 mile at an easy pace (8:15 per mile), 
#        then 3 miles at tempo (7:12 per mile) and 
#        1 mile at easy pace again
def run_time(distance, pace_minutes, pace_seconds):
	""" Add appropriate docstring
	"""
	# your code here	
	return

def total_run_time():
	""" Add appropriate docstring
	"""
   return time

   
#----------------------------------------------
# Part B:  Grid functions
#
# Rewrite the grid functions from Exerciese 2.3 per the instructions below.  
# NOTE: Function names have been changed from print_nnnnnn to str_nnnnnn.
#       The do_twice() and str_beam() functions have been provided as examples.
#        
# 
# For each function:
#   1) Instead of printing, each function should return a string
#   2) Instead of a set cell width, allow for variable width cells.
#----------------------------------------------

def do_twice(f, a):
	""" Add appropriate docstring
	"""
	twice = f(a)
	twice += f(a)
	return twice

def do_four(f, a):
	""" Add appropriate docstring
	"""
	# your code here	
	return

def str_beam(beam_width):
	""" Add appropriate docstring
	"""
	# add post to beginning of beam
	beam = '+'
	# create beam
	beam += ' -' * beam_width 
	# add end
	beam += ' '
	return beam

def str_post(beam_width):
	""" Add appropriate docstring
	"""
	# your code here	
	return
    
def str_beams(beam_width):
	""" Add appropriate docstring
	"""
	# your code here	
	return

def str_posts(beam_width):
	""" Add appropriate docstring
	"""
	# your code here	
	return

def str_row(beam_width):
	""" Add appropriate docstring
	"""
	# your code here	
	return

def str_grid(beam_width):
	""" Add appropriate docstring
	"""
	# your code here	
	return
    



def test(name, got, expected):
	""" Simple test() function, called in main().  Prints status of test. 
	If got doesn't match expected, error messages is displayed.
	"""
	if got == expected:
		print (name + ' - OK')
	else:
		print ('%s - X got: %s expected: %s' % (name, repr(got), repr(expected)))



def main():
	""" Test exercise functions above using test function
	"""
	print('Examples:\n')
	test('a_plus_b', a_plus_b('ban','ana'), 'banana')
	test('area_rectangle', area_rectangle(4, 6), 24) 

	print()
	print('Part A: Calculate\n')
	test('volume_sphere', volume_sphere(5), 523) 
	test('wholesale_cost', wholesale_cost(60, 24.95, 0.40, 3, .75), 945) 
	test('total_run_time', total_run_time(), 38.1)

	print()
	print('Part B: Grid functions\n')
	test('str_beam(3)', str_beam(3), '+ - - - ')
	test('str_beam(4)', str_beam(4), '+ - - - - ')
	test('str_post(3)', str_post(3), '|       ')
	test('str_post(4)', str_post(4), '|         ')
	test('str_beams(3)', str_beams(3), '+ - - - + - - - +\n')
	test('str_beams(4)', str_beams(4), '+ - - - - + - - - - +\n')
	test('str_posts(3)', str_posts(3), '|       |       |\n')
	test('str_posts(4)', str_posts(4), '|         |         |\n')
	row3  = '+ - - - + - - - +\n'
	row3 += '|       |       |\n'
	row3 += '|       |       |\n'
	row3 += '|       |       |\n'
	row3 += '|       |       |\n'
	test('str_row(3)', str_row(3), row3)
	row4  = '+ - - - - + - - - - +\n'
	row4 += '|         |         |\n'
	row4 += '|         |         |\n'
	row4 += '|         |         |\n'
	row4 += '|         |         |\n'
	test('str_row(4)', str_row(4), row4)
	grid3 = row3 + row3 + '+ - - - + - - - +\n'
	test('str_grid(3)', str_grid(3), grid3)
	grid4 = row4 + row4 + '+ - - - - + - - - - +\n'
	test('str_grid(4)', str_grid(4), grid4)
   

# Call the main() function
if __name__ == '__main__':
    main()


  