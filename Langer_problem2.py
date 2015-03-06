"""
PHYS 50733 Assignment #2
Problem #2 Mass formula
Asks for the mass number A
and the atomic number Z.
Returns the binding energy B 
and the binding energy per 
nucleon, B/A in MeV. 

@author: Cameron Langer
"""
a_1,a_2,a_3,a_4=15.67,17.23,0.75,93.2
A=int(input("Enter the mass number A: "))
Z=int(input("Enter the atomic number Z: "))
if A%2==1:              # A is odd
    a_5=0.0             
elif Z%2==1:            # A is even and Z is odd      
    a_5=-12.0
else:                   # A and Z are both even
    a_5=12.0
B=a_1*A-a_2*A**(2.0/3.0)-a_3*Z*Z*A**(-1.0/3.0)-a_4*(A-2*Z)*(A-2*Z)/A-a_5*A**(-1.0/2.0)
print("The binding energy is: {:0.2f} MeV".format(B))
print("The binding energy per nucleon is: {:0.2f} MeV".format(B/A))
    
# output of program for A=58,Z=28
#
# Enter the (integer) mass number A: 58
#
# Enter the (integer) atomic number Z: 28
# The binding energy is: 490.78 MeV
# The binding energy per nucleon is: 8.46 MeV
#
# output of program for A=59,Z=28
#
# Enter the mass number A: 59
#
# Enter the atomic number Z: 28
# The binding energy is: 498.14 MeV
# The binding energy per nucleon is: 8.44 MeV

# output of program for A=58,Z=27
#
# Enter the mass number A: 58
#
# Enter the atomic number Z: 27
# The binding energy is: 485.31 MeV
# The binding energy per nucleon is: 8.37 MeV

    