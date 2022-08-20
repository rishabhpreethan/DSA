#HARD

#871
# A car travels from a starting position to a destination which is target miles east of the starting position.
# There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.
# The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.
# Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.
# Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.


# Example 1:
# Input: target = 1, startFuel = 1, stations = []
# Output: 0
#---------
# Explanation: We can reach the target without refueling.

# Example 2:
# Input: target = 100, startFuel = 1, stations = [[10,100]]
# Output: -1
#---------
# Explanation: We can not reach the target (or even the first gas station).

# Example 3:
# Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
# Output: 2
#---------
# Explanation: We start with 10 liters of fuel.
# We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
# Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
# and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
# We made 2 refueling stops along the way, so we return 2.


from heapq import heappush
from heapq import heappop


def minRefuelStops(target, startFuel, stations):
        fuel, heap, count = startFuel, [], 0       
        
        stations.append([target, 0])                   

        while stations:
            if fuel >= target: return count                        

            while stations and stations[0][0] <= fuel: 
                _, liters = stations.pop(0)
                heappush(heap,-liters)

            if not heap: return -1                      
            fuel-= heappop(heap)

            count+= 1

print(minRefuelStops(100,1,[[10,100]]))     #Example 2