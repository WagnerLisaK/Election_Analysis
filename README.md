# Election_Analysis

## Project Overview
A Colorado Board of Elections employee gave me the following tasks to complete the election audit of a recent local congressional election.

1.  Calculate the total number of votes cast.
2.  Get a complete list of candidates who received votes.
3.  Caluculate the total number of votes each candidate received.
4.  Calculate the percent of votes each candidate won.
5.  Determine the winner of the election based on popular vote.

## Resources
 - Data Source: election_results.csv
 - Software:  Python 3.7.6; Visual Studio Code 1.57.1

## Election-Audit Results
The analysis of the election shows that:
- There were 369,711 votes cast in the election.

- The counties and their results are:
  - Arapahoe:  6.7%  (24,801)
  - Denver:  82.8%  (306,055)
  - Jefferson:  10.5%  (38,855)

  - **DENVER county had the largest number of votes.**

- The candidates and results were:
  - Charles Casper Stockham, receiving 23.0% (85,213) of the votes.
  - Diana DeGette, receiving 73.8% (272,892) of the votes.
  - Raymon Anthony Doane, receiving 3.1% (11,606) of the votes.
  
- **The winner of the election was: Diana DeGette**, who received **73.8%** of the vote, with **272,892** total votes.

## Election-Audit Summary
When modified, this script can be used for ANY election, with any number of candidates and any number or counties.  This script could also be modified to be used with ANY type of voting scenario, such as Student Elections, Car Show Voting, Food/Restaurant Voting, etc.

For example, using this script for Car Show voting ...
 1. Replace the **Candidate-referencing** variables with **Car Yr/Make/Model** variables.
 2. Replace the **County-referencing** variables with **Car Award** variables, such as "Crowd Favorite", "Mustang GT 2010-2015", and "Mustang GT 2016-2021".

For Food/Restaurant voting ...
 1. Replace the **Candidate-referencing** variables with **specific restaurant name** variables.
 2. Replace the **County-referencing** variables with **Category Choice** variables, such as "Best Outdoor Dining", "Best Indoor Dining", "Best Take-out".

Then ***throughout the entire code***, replace the "old" variables with the "new" variables a shown in the example below:

![CodeChanges.png](https://github.com/WagnerLisaK/Election_Analysis/blob/main/Resources/CodeChanges.png)

The following are the assumptions:
 1. There is a "Resources" folder containing the "election_results.csv" file which contains the voting results.
    - The results are formatted the same as the existing data in the file (same columns, etc)
 2. There is an "Analysis" folder containing the "election_analysis.txt" file which will contain the analysis.

**********************************************************************
CHALLENGE  SUBMISSION  NOTES:

Below is a screen shot of the terminal output:

![Terminal_Output.png](https://github.com/WagnerLisaK/Election_Analysis/blob/main/Resources/Terminal_Output.png)

Below is a screen shot of the txt_file output:

![Write_Output.png](https://github.com/WagnerLisaK/Election_Analysis/blob/main/Resources/Write_Output.png)


Submitted by Lisa K Wagner (07/05/2021)
