"""
PHYS 50733 Assignment #2
Problem #1 Special Relativity
Asks for distance x in light years
and the ratio of the ship's velocity
v to the speed of light c. Returns the 
time in years it takes a spaceship to 
reach its destination in the rest
frame of an observer on Earth, and 
in the frame attached to the ship.
@author:  Cameron Langer
"""
from math import sqrt
x=float(input("Enter the distance between Earth and the other planet in light years: "))
beta=float(input("Enter the ratio of the velocity v to the speed of light c: "))
gamma=1.0/sqrt(1-beta*beta)
delta_t0=x/beta          # time interval in ship's frame is proper time
delta_t=gamma*delta_t0   # time interval in earth's frame
print ("The time interval in the spaceship frame is: {:0.2f} years".format(delta_t0))
print ("The time interval in the Earth's frame is: {:0.2f} years".format(delta_t))

# output of program for x=10 light years, v/c=0.9
#
# Enter the distance between Earth and the other planet in light years: 10
#
# Enter the ratio of the velocity v to the speed of light c: 0.9
# The time interval in the spaceship frame is: 11.11 years
# The time interval in the Earth's frame is: 25.49 years
#
# output of program for x=10 light years, v/c=0.98
#
# Enter the distance between Earth and the other planet in light years: 10
#
# Enter the ratio of the velocity v to the speed of light c: 0.98
# The time interval in the spaceship frame is: 10.20 years
# The time interval in the Earth's frame is: 51.28 years
#
# output of program for x=10 light years, v/c=0.999
#
# Enter the distance between Earth and the other planet in light years: 10
# 
# Enter the ratio of the velocity v to the speed of light c: 0.999
# The time interval in the spaceship frame is: 10.01 years
# The time interval in the Earth's frame is: 223.89 years

