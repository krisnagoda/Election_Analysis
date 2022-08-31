# Data required for Module 3

# Total number of votes cast

# A complete list of candidates who received votes

# Total number of votes each candidate received

# Percentage of votes each candidate won

# The winner of the election based on popular vote


# Module 3 Challange 

# The voter turnout for each county

# The percentage of votes from each county out of the total count

# The county with the highest turnout


# Pseudocode

# Open the data file located here Resources/election_results.csv

# Write down the names of all the candidates

# Add a vote count for each candidate

# Get the total votes for each candidate

# Get the total votes cast for the election

# code

import csv

import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)