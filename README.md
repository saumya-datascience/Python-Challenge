# Python-Challenge
coding time!!!
# Python Homework - Py Me Up, Charlie

## Background
Time to get my hands dirty with some serious Python coding! 
This time I have not one but two Challenges as part of Rutgers DataScience Bootcamp.
PyBank and Pypoll challenges address real world situation and are far from easy.
Hard work and burning some mid night oil is all I needed to Master the challenges. 



### Getting the Github all set!


* Created a new repository for this project called `python-challenge`. 

* Cloned the new repository to my computer.

* Inside my local git repository, created a directory for each Python Challenge. Used folder names corresponding to the challenges: **PyBank** and  **PyPoll**.

* Inside of each folder  added the following:

  * A new file called `main.py`. This will be the main script to run for each analysis.
  * A "Resources" folder that contains the CSV files you used. Made sure my script has the correct path to the CSV file.
  * An "analysis" folder that contains my text file that has the results from the analysis.

* Pushed the above changes to GitHub.

## PyBank

* In this challenge, I was tasked with creating a Python script for analyzing the financial records of the company. A set of financial data called [budget_data.csv](pyBank/Resources/budget_data.csv) was provided. The dataset is composed of two columns: `Date` and `Profit/Losses`. 
* Job done are as follows
*  A Python script that analyzes the records to calculate each of the following:

  *  1) The total number of months included in the dataset

  *  2)The net total amount of "Profit/Losses" over the entire period

  *  3) Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

  *  4) The greatest increase in profits (date and amount) over the entire period

  *  5)The greatest decrease in losses (date and amount) over the entire period


* In addition, a final script  printed  the analysis to the terminal and exported a text file with the results.
* RESULTS!!!!

*  [Python Script](pyBank/main.py)
```text
  Financial Analysis
-----------------------------------------------------------
Total Months 86
-----------------------------------------------------------
Total  $38382578
Average Change $-2315.1176470588234
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest decrease in Profits: Sep-2013 ($-2196167)

```
## PyPoll

* In this challenge, I was tasked with helping a small, rural town modernize its vote counting process.

*  A set of poll data was provided [election_data.csv](pypoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. I created a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* As an example, your analysis should look similar to the one below:

```text
  The Election Results
-----------------------------------------------------------
Total Votes are  3521001
-----------------------------------------------------------
 Mr. Khan got vote percentage: 63.00001050837531 with a total vote_count: 2218231
-----------------------------------------------------------
And the Winner is....DrumRoll.......... Mr.Khan !!!!!!!!
-----------------------------------------------------------```text
 
  ```

* In addition, my final script both printed the analysis to the terminal and exported a text file with the results.)
* Results
[Python script](pypoll/main1.py)

