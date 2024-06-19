# 1. Python Sets Adventure
# Objective: The aim of this assignment is to deepen your understanding and application of Python sets in various scenarios, ranging from basic operations to advanced manipulations and best practices. 
# You will correct given codes, use sets in everyday contexts, and tackle challenges that require creative thinking and problem-solving. **Task 1: Flight Route Comparison** 
# Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. 
# You have two sets of flight destinations, one for each airline. Write a Python program to find out: 
# 
# 1. Destinations that both airlines fly to. 
# 2. Destinations unique to your airline. 
# 3. Whether there are any destinations that neither airline shares. 
# 
# **Example Code:**

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# find simiilar use .intersection
# unique use .difference
# ones that niether one share

def flight_destination(our_routes, competitor_routes):
    similar_flights = our_routes.intersection(competitor_routes) #find the similarities
    print(similar_flights)
    unique_flights = our_routes.difference(competitor_routes) #find the unique specific to our routes
    print(unique_flights)
    unshared_flights = our_routes.symmetric_difference(competitor_routes) # find the unique beween both routes
    print(unshared_flights)

flight_destination(our_routes, competitor_routes)


# 2. Set Operations in Data Analysis

# Objective: The aim of this assignment is to enhance your skills in using Python sets for data analysis tasks. You will apply various set operations to handle real-world data scenarios, focusing on their practical application and efficiency.

# Task 1: Duplicate Entries Cleanup You are given a list of customer IDs, some of which are duplicated. 
# Write a Python function to remove duplicates and display the unique customer IDs.
# Example Code:

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

# Expected Outcome: A set of unique customer IDs, ensuring no duplicates. For instance, {'C001', 'C002', 'C003', 'C004'}.

def remove_dup(customer_ids):
    customer_ids_set = set(customer_ids) # sets dont have duplicates so when you change it to a set they are removed.
    print(customer_ids_set)
    customer_ids = sorted(customer_ids_set) #looks like when you sort them it automatically turns it back into a list. 
    print(customer_ids)

remove_dup(customer_ids)