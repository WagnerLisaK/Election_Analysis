# Output 1 = Total # of votes cast
# Output 2 = List of candidates that received votes
# Output 3 = # of votes per candidate
# Output 4 = % of votes per candidate
# Output 5 = Declared winner

# Add dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Declare a list for candidate names.
candidate_options = []

# Declare a dictionary for each candidate's votes.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
   
    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file and add to the total vote count.
    for row in file_reader:
        total_votes +=1
    
        # Print the candidate name from each row.
        candidate_name = row[2]

        # If candidate name is not in the list, add it.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Begin tracking subject candeidate's vote count.
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] +=1
    
    # Save results to text file.
    with open(file_to_save, "w") as txt_file:
    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
        #Print the final vote count to the terminal. 
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)
        
        for candidate_name in candidate_votes:
            # Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]
            # Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100
            # with open(file_to_save, "w") as txt_file:
            # Print out each candidate's name, vote count, and percentage of votes to the terminal.
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            # Save the candidate results to our text file.with open(file_to_save, "w") as txt_file:
            txt_file.write(candidate_results)

# Close the file.
election_data.close()

        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count.
        #if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
        #   winning_count = votes
        #   winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name.
        #   winning_candidate = candidate_name

    #winning_candidate_summary = (
    #    f"-------------------------\n"
    #    f"Winner: {winning_candidate}\n"
    #    f"Winning Vote Count: {winning_count:,}\n"
    #    f"Winning Percentage: {winning_percentage:.1f}%\n"
    #    f"-------------------------\n")
    
    #print(winning_candidate_summary)

# Write some data to the file.
# outfile.write("Hello World, It's me!")

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
 #    txt_file.write("Counties in the Election\n------------------------\n")
    # Write three counties to the file.
 #    txt_file.write("Arapahoe\nDenver\nJefferson")
    
# Close the file
# outfile.close()

