import os
import csv

#describe the path to find the files needed
csv_file_path = os.path.join("election_data.csv")

#identify variables
total_votes = 0         # count total number of votes
candidates = {}         # dictionary of keys (candidate names) and values (number of votes)
candidates_percent = {} # dictionary of vote percentages for candidates
winner_count = 0        # number of votes for winning candidate
winner_name = ""        #name of the winning candidate in an empty string

#------------------------------------------------------------------------------

#with open(csv_file_path, newLine="") as csv_file:
with open(csv_file_path, newline="") as csv_file:
   reader = csv.reader(csv_file, delimiter = ",")
   next(reader, None) #check the next method
   for row in reader:
       total_votes += 1 # tally total vote count

       # find list of candidates who received votes
       if row[2] in candidates.keys():
           candidates[row[2]] += 1
       else:
           candidates[row[2]] = 1
       #we are counting the candidates and building the dictionary of candidates where the key is the candidate
       #name and the value is the number of votes.
       # calculate percentages for votes won by each candidate (candidates dictionary: key= Name, value= number of votes)
       for key, value in candidates.items():
           candidates_percent[key] = round((value/total_votes) * 100, 1)
            #items is a sequence in the dictionary that returns you key value pairs
       # find winning candidate using candidates dictionary
       #round *100, 1 will make a percentage of the fraction and keep one decimal point

       for key in candidates.keys():
           if candidates[key] > winner_count:
               winner_name = key
               winner_count = candidates[key]

#Format to print out the results
print ("Election Results")
print ("------------------------")
print ("Total Votes: " + str(total_votes))
print("-------------------------")
for key, value in candidates.items():
    print(key + ":" + str(candidates_percent[key]) + "% (" + str(value) + ")")
print("--------------------------")
print("Winner: " + winner_name)
print("-------------------------")

output_file = "results.txt"
with open(output_file, 'w') as outfile:
    outfile.write("Election Results \n")
    outfile.write("--------------------------\n")
    outfile.write("Total Votes: " + str(total_votes) + "\n")
    outfile.write("-------------------------\n")
   
   #for key, value in candidates.items():
for key, value in candidates.items():
       outfile.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")
       outfile.write("--------------------------\n")
       outfile.write("Winner: " + winner_name + "\n")
       outfile.write("-------------------------\n")
