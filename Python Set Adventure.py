# Task 1: Flight Route Comparison
#  Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. 
# You have two sets of flight destinations, one for each airline. Write a Python program to find out:

# 1. Destinations that both airlines fly to.

# 2. Destinations unique to your airline.

# 3. Whether there are any destinations that neither airline shares.

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

same_routes = our_routes.intersection(competitor_routes)
unique_routes = our_routes.difference(competitor_routes)
no_share_routes = our_routes.symmetric_difference(competitor_routes)
print(same_routes)
print(unique_routes)
print(no_share_routes)