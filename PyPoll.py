# Output 1 = Total # of votes cast
# Output 2 = List of candidates that received votes
# Output 3 = # of votes per candidate
# Otput 4 = % of votes per candidate
# Output 5 = Declared winner
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
# outfile = open(file_to_save, "w")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
   
    # Print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    # for row in file_reader:
    #    print(row)

# Write some data to the file.
# outfile.write("Hello World, It's me!")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
     txt_file.write("Counties in the Election\n------------------------\n")
    # Write three counties to the file.
     txt_file.write("Arapahoe\nDenver\nJefferson")
    
# Close the file
# outfile.close()



# Close the file.
election_data.close()