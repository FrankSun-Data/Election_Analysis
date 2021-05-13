#open file
import csv
import os

#Assign variable to load from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign variable to save the file to a path
file_to_save = os.path.join("Analysis","election_analysis.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:

#Read the file
    file_reader = csv.reader(election_data)

#print each row in CSV file
    headers = next(file_reader)
    print(headers)

    


    












