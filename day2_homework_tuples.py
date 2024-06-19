# <!-- 1. Tuple Mastery in Python

# Objective: The aim of this assignment is to deepen your understanding of tuples in Python, along with their interaction with lists, dictionaries, and basic Python functionalities like functions, input handling, and string formatting. 
# By completing this assignment, you will enhance your skills in data structuring, manipulation, and application of tuples in practical scenarios. -->


# Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. 
# Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). 
# The function should loop through the list of itineraries and print a formatted string for each. 
# For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], the output should be:
# 
# "Itinerary 1: Alice - From New York to London"
# "Itinerary 2: Bob - From Tokyo to San Francisco"



travel_info = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco"), ("Libby", "Colorado", "Albania"), ("Todd", "Oklahoma", "Colorado")]

def tuple_mastery(travel_info):
    for index, itinerary in enumerate(travel_info): # Pull out the index and each item inside
        name, origin, destination = itinerary # Assign each item in the tupke a variable
        print(f"Itinerary {index + 1}: {name} - From {origin} to {destination}") # fancy print statement with all elements
    
tuple_mastery(travel_info)

# 2. Python Data Structure Challenges in Real-World Scenarios

# Objective: This assignment is designed to enhance your understanding and application of Python's core data structures - tuples, lists, and dictionaries - in real-world contexts. 
# By engaging with these tasks, you will practice manipulating these data structures, applying built-in Python methods, and implementing error handling in practical situations.

# Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.
# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.
# Existing Library Data:

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]


# Add functionality to insert new books into library.
# Ensure that adding a duplicate book is handled appropriately (hint: do a membership check to see if the new book is already in the library).

def library_system(book, author):
    new_book = (book, author) # Pair the entries together in tuple
    if new_book in library: #if its in the library already dont add it and let them know
        print("This book is already in the library")
    else:
        library.append(new_book) # If its not append the tuple into the list 
        print("Book has been added to the library")
    print(library)

library_system("Lord of the Rings", "J.R.R Tolkien")
library_system("1984","George Orwell")