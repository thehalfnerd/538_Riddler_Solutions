# -*- coding: utf-8 -*-
"""

author: @thehalfnerd
"""

import random
import matplotlib.pyplot as plt


# Module that runs one simulation
def one_simulation(n):
    # Create an array with length n where n is the number of seats on a plane.
    # Fill the array with the character e which indicates an empty seat on the plane
    plane_seats = ["e"] * n
    
    
    # Place the first person into a random spot on the plane
    # He will be labeled 0
    first_person_pos = random.randint(0, n-1)
    plane_seats[first_person_pos] = 0

    # Give the starting point for the next person which will be iterable
    person_number = 1
    
    while "e" in plane_seats:
        
        if plane_seats[person_number] == "e":
            plane_seats[person_number] = person_number 
        else:
            plane_seats[random.choice([i for i,x in enumerate(plane_seats) if x == "e"])] = person_number
        
        person_number +=  1
    
    if plane_seats[n-1] == n-1:
        return True
    else:
        return False

def main():
    seat_count = input('How many plane seats are there? ')
    sim_count = input('How many times do you want to run the program? ')   
    monte_carlo_list = []
    percent_list = []
    
    for i in range(sim_count):
        monte_carlo_list.append(one_simulation(seat_count))
        percent_list.append(monte_carlo_list.count(True)/float(len(monte_carlo_list)))
    
    plt.plot(range(sim_count), percent_list)
    plt.xscale('log')
    plt.grid(True)
    plt.yticks([ 0.1, 0.2, 0.3, 0.4, 0.5 , 0.6, 0.7, 0.8, 0.9, 1.0])
    plt.xlabel('Simulation Count')
    plt.ylabel('Percent of Simulations Finding Final Seat Unoccupied')
    plt.axis([1, sim_count, 0, 1])
    plt.show()
    
    print "Your seat was unoccupied in %f percent of %d simulations" % (100*percent_list[sim_count-1], sim_count)

main()


    