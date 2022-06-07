# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("..", "Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

# 3. Print the total votes.
print(total_votes)
# Candidate Options and candidate votes.
candidate_options = []
# Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

# Print the candidate list.
print(candidate_options)
candidate_votes = {}
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:
          # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0


# Print the candidate vote dictionary.
print(candidate_votes)

# 1: Create a county list and county votes dictionary.
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438


# Track the winning candidate, vote count and percentage
winning_candidate = "Diana DeGette"
winning_count = 272,892
winning_percentage = 73.8%

# 2: Track the largest county and county voter turnout.
counties_dict.get("Denver")



# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
         counties_dict.keys()
         dict_keys(['Arapahoe', 'Denver', 'Jefferson'])

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
            counties = ["Arapahoe","Denver","Jefferson"]
            if counties[0] == 'Arapahoe':
            print(counties[0])
            if counties[1] == 'Denver':
            print(counties[1])
            if counties[2] == 'Jefferson':
            print(counties[2])

            # 4b: Add the existing county to the list of counties.
            counties.append("")

            # 4c: Begin tracking the county's vote count.
            counties_dict
            {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}

        # 5: Add a vote to that county's vote count.
        counties.append("")+=1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.

        # 6b: Retrieve the county vote count.
        counties_dict
        {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
        # 6c: Calculate the percentage of votes for the county.
        for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate_name}: received {vote_percentage}% of the vote.")

         # 6d: Print the county results to the terminal.
        print(counties_dict["Arapahoe"] = 422829
        print(counties_dict["Denver"] = 463353)
        print(counties_dict["Jefferson"] = 432438)

        print(county_vote["Jefferson"])=38855
        print(county_vote["Denver"])=306056
        print(county_vote["Arapahoe"])=24821

        print(county_vote["Jefferson"])=38855/369732*100
        print(county_vote["Denver"])=306056/369732*100
        print(county_vote["Arapahoe"])=24821/369732*100    

        County_results = (
        f"\nCounty Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(County_results, end ="")

    txt_file.write(election_results)    
         # 6e: Save the county votes to a text file.
        with open(file_to_save, "w") as txt_file:
         # 6f: Write an if statement to determine the winning county and get its vote count.
          if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

    # 7: Print the county with the largest turnout to the terminal.
    print(counties_dict["Denver"] = 306056)

    # 8: Save the county with the largest turnout to a text file.
    print(counties_dict["Denver"] = 306056)
    txt_file.write(election_results)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
