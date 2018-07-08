import csv
import os

voter_csv = os.path.join("Resources", "election_data.csv")

total_voters = []
votes_for_Khan = []
votes_for_Correy = []
votes_for_Li = []
votes_for_Otooley = []

with open(voter_csv, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	
	for row in csvreader:
		total_voters.append(row[0])
		if 'Khan' in row:
			votes_for_Khan.append(row[0])
		elif 'Correy' in row:
			votes_for_Correy.append(row[0])
		elif 'Li' in row:
			votes_for_Li.append(row[0])
		else:
			votes_for_Otooley.append(row[0])

total_votes = len(total_voters) - 1 
khan_votes = len(votes_for_Khan)
correy_votes = len(votes_for_Correy)
li_votes = len(votes_for_Li)
otooley_votes = len(votes_for_Otooley) - 1				

percent_khan = round((khan_votes/total_votes) * 100)
percent_correy = round((correy_votes/total_votes) * 100)
percent_li = round((li_votes/total_votes) * 100)
percent_otooley = round((otooley_votes/total_votes) * 100)

# assign percentages to dictionary to pass into winner function
dict_of_percentages = {percent_khan: 'Khan' , percent_correy: 'Correy' , percent_li : 'Li', percent_otooley: "O'tooley"}

#define function to determine winner
def winner(list_of_percentages):
    for percent in list_of_percentages:
        if percent == max(list_of_percentages):
            maxpercent = percent
            winner = list_of_percentages[maxpercent]
    return winner



with open('./pypoll.txt', 'w') as writeFile:
	writefile.writelines("Election Results")
	writefile.writelines('----------------------')
	writefile.writelines("Total Votes" + str(total_votes))  
	writefile.writelines("----------------------")
	writefile.writelines("Khan: " + str(percent_khan) + "% (" + str(khan_votes) + ")")
	writefile.writelines("Correy: " + str(percent_correy) + "% (" + str(correy_votes) + ")")
	writefile.writelines("Li: " + str(percent_li) + '% (' + str(li_votes) + ')')
	writefile.writelines("O'Tooley: " + str(percent_otooley) + '% (' + str(otooley_votes) + ')')
	writefile.writelines('----------------------')
	writefile.writelines("Winner:" + winner(dict_of_percentages))

#with open('pypoll.txt', 'r') as readfile:
    #print(readfile.read())
