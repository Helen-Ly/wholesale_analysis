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


with open(file_to_load, "r") as wholesale_data:

    # Create variable for total entry
    total_entries = 0

    # Show header
    header = next(wholesale_data)
    print(header)

    # Create a for loop to count each entry
    for entry in wholesale_data:

        # Variable for buyer
        buyer = entry[2]

        # Add count to total_entries
        total_entries += 1
    
    # Print out total entries
    print(total_entries)




######################################
# Determine unique vehicles sold
# Determine how many were sold for each model
# Determine percentage told
# Determine top sold vehicle
######################################

######################################
# Write out results to text file
######################################