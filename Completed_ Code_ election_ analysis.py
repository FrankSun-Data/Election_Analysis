#open file
import csv
import os

#Assign variable to load from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign variable to save the file to a path
file_to_save = os.path.join("Analysis","election_analysis.txt")

#initialize a total vote counter
total_vote = 0

#Print the candidate name from each row
candidate_options = []

#Declare empty dictionary for votes
candidate_votes = {}

#Wining candidate and wining count
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:

#Read the file
    file_reader = csv.reader(election_data)

#print each row in CSV file
    headers = next(file_reader)
    for row in file_reader:

#Add to total vote count
        total_vote +=1

#Print the candidate name from each row
        candidate_name = row[2]

#If name doesn't match any existing
        if candidate_name not in candidate_options:

#Add the candidate name to the candidate list
                candidate_options.append(candidate_name)

#Counting candidate's votes
                candidate_votes[candidate_name] = 0

#Add votes to count
        candidate_votes[candidate_name] +=1

#Save the results to our text file
with open(file_to_save,"w") as txt_file:
        election_results = (
                f"\nElection Results\n"
                f"------------------\n"
                f"Total Votes: {total_vote:,}\n"
                f"------------------\n")

        print(election_results, end="")
        txt_file.write(election_results)

#Percentage; Iterate through list
        for candidate_name in candidate_votes:

        # Retrieve vote count and percentage.
                votes = candidate_votes[candidate_name]
                vote_percentage = float(votes) / float(total_vote) * 100

        # Print each candidate, their voter count, and percentage to the terminal.
                #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
                candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
                print(candidate_results, end="")
                txt_file.write(candidate_results)


        # Determine winning vote count, winning percentage, and candidate.
                if (votes > winning_count) and (vote_percentage > winning_percentage):
                        winning_count = votes
                        winning_candidate = candidate_name
                        winning_percentage = vote_percentage

        # Print the winning candidates' results to the terminal.
        winning_candidate_summary = (
                f"-------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"-------------------------\n")

        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)
        












    












