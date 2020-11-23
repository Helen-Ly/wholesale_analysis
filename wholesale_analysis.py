# Import dependencies
import os
import csv

# Open and pull data
file_to_load = os.path.join("Resources", "UCD - WHOLESALE.csv")

######################################
# Count  total vehicles sold within the 2 year time frame
# Get list of unique buyers
# Determine how many times each buyer purchased from us
# Determine percentage for buyers
# Determine top buyer
######################################

# Create variable for total entry
total_entries = 0

# Create list for unique buyers
buyer_name = []

# Create dictionary for each buyer
buyer_dictionary = {}

with open(file_to_load, "r") as wholesale_data:

    # Read the dat
    file_reader = csv.reader(wholesale_data)

    # Show header 
    header = next(file_reader)
    print(header)

    # Create a for loop to count each entry
    for row in file_reader:

        # Add count to total_entries
        total_entries += 1

        # Variable to pull out buyer name
        buyer = row[2]

        # Append to the buyer_name list
        if buyer not in buyer_name:

            # Append buyer
            buyer_name.append(buyer)

            # Initialize buyer dictionary
            buyer_dictionary[buyer] = 0

        # Add count for buyer in dictionary
        buyer_dictionary[buyer] += 1

            
    
    # Print out total entries
    print(total_entries)

    # Print out buyer_name list
    print(buyer_name)

    # Print out buyer_dictionary
    print(buyer_dictionary)




######################################
# Determine unique vehicles sold
# Determine how many were sold for each model
# Determine percentage told
# Determine top sold vehicle
######################################

######################################
# Write out results to text file
######################################