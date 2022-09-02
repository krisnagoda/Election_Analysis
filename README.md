# Election Analysis

## Overview

Preform audit of the election data to verify results for the Colorado Board of Elections. Develop code that can be reused across other local, congressional, and senatorial districts. 

## Election Audit Results

How many votes were cast in this congressional election?
   ```
   369,711
   ```
Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
   ```
   Jefferson: 10.5% (38,855)
   Denver: 82.8% (306,055)
   Arapahoe: 6.7% (24,801)
   ```
Which county had the largest number of votes?
   ```
   Denver
   ```
   
Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
   ```
   Charles Casper Stockham: 23.0% (85,213)
   Diana DeGette: 73.8% (272,892)
   Raymon Anthony Doane: 3.1% (11,606)
   ```
   
Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
   ```
   Winner: Diana DeGette
   Winning Vote Count: 272,892
   Winning Percentage: 73.8%
   ```
   
Screenshot of Terminal Output: 

![election_results](https://github.com/krisnagoda/Election_Analysis/blob/eff5bc494ab6f47c7d8c8b8c24d97029c8cf3aa8/resources/election_results_module_3_challenge.png)

Screenshot of election_analysis.txt:

![election_results](https://github.com/krisnagoda/Election_Analysis/blob/27f01909e19283829ea106ff6e473c35b30ca416/resources/election_results_module_3_challenge_notepad.png)

## Election Audit Summary

Our new code is ready to be reused across other local, congressional, and senatorial districts. With the input data format standardization we implemented, we can simply update the file path in PyPoll_Challenge.py and rerun the code to produce a comparable output for any election. 
   
## Resources

Data Source: election_results.csv

Software: Python 3.6.1, Visual Studio Code 1.70.2
