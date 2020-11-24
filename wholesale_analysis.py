# Import dependencies
import os
import csv

# Create file paths to open data and save text file
file_to_load = os.path.join("Resources", "UCD - WHOLESALE.csv")

file_to_save = os.path.join("Analysis", "wholesale_results.txt")

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

# Create variables to hold winning buyer
top_buyer = ""
top_buyer_count = 0
top_buyer_percentage = 0

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

with open(file_to_save, "w") as text_file:
    
    # Create an introduction
    introduction= (
        f"\n Wholesale Results \n"
        f"-------------------------\n"
        f"\n Summary: Data taken from wholesale transactions from 2018-2020 \n"
        f"\n-------------------------\n"
    )

    # Print out introduction
    #print(introduction)

    # Write introduction into text_file
    text_file.write(introduction)
    
    # Loop through buyer_dictionary to pull out each key-value pair
    for buyer in buyer_dictionary:

        # Pull out the value for each corresponding key
        ws_buyer = buyer_dictionary[buyer]

        # Calculate the percetage for each wholesale buyer
        ws_buyer_percentage = ws_buyer / total_entries * 100

        print(f"{buyer}: {ws_buyer_percentage:.2f}% ({ws_buyer:,})\n")

        # Find top buyer
        if (ws_buyer > top_buyer_count) and (ws_buyer_percentage > top_buyer_percentage):

            # Attach values to variables
            top_buyer = buyer

            top_buyer_count = ws_buyer

            top_buyer_percentage = ws_buyer_percentage

    top_buyer_summary = (
        f"\n-----------------------------\n"
        f"Top Buyer: {top_buyer}\n"
        f"Top Buyer Count: {top_buyer_count:,}\n"
        f"Top Buyer Percentage: {top_buyer_percentage:.1f}%\n"
    )

    # Print out summary
    print(top_buyer_summary)

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