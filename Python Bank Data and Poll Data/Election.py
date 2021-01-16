import pathlib
import csv

election_data = pathlib.Path('Resources/election_data.csv')
pathout = pathlib.Path("Resources/Election Analysis")

votes = 0
total_candidates = 0
vote_count = []
candidate_options = []
candidate_votes = {}

with open(election_data) as elect_data:
    reader = csv.DictReader(elect_data)

    for row in reader:
        votes = votes + 1
        total_candidates = row["Candidate"]

        if row["Candidate"] not in candidate_options:
            candidate_options.append(row["Candidate"])

            candidate_votes[row["Candidate"]] = 1

        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1

    print()
    print()
    print()
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {votes}")
    print("-------------------------")

    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
    
candidate_votes

from operator import itemgetter
winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")

with open(pathout, "w") as txt_file:
    
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write(str(winner))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[0]))
    txt_file.write("\n")
    txt_file.write("Total Votes " + str(votes))