
import os
import csv
import operator

#load 
file = os.path.join('..','PyPoll', 'Resources','PyPoll_Resources_election_data.csv')
text = os.path.join('..','PyPoll','Analysis','election.Text')

#open csv path and reader

with open(file) as election_data:
    reader = csv.reader(election_data)

# prints header of file as a check to see if file is opened and read properly
    
    header = next(reader)
    print(header)
    
  
    # make votes a dictionary to store the votes for each candidate sorted from the data
    votes = dict()

    # defines total votes
    votes_tot = 0
   
    for candidate in reader:
        #each time a vote reviewed, the total count of votes goes up by +1
        votes_tot += 1
        
        if candidate[2] in votes:
            votes[candidate[2]] += 1
        else: 
            votes[candidate[2]] = 1


 

   #Find highest amount of votes within dictionary
    winner_votes = max(votes.items(), key=operator.itemgetter(1))[0]

    print("Election Results")

    print("-------------------------")

    #prints the total votes counted
    print(f'Total Votes: {votes_tot}')

    print("-------------------------")

    
    #this is looking for the percentage of votes per candidate          
    for vote in votes:
        candidate_votes = votes[vote]
        #takes the number of votes per candidate and divides by the total votes casted
        percent = candidate_votes/votes_tot

        #this is to format the final percent value to one decimal point    
        percent_format = "{:.1%}".format(percent)  
        #prints the name of the candidate, the number of votes recieved, and percentage of votes received from total votes casted
        print(f"{vote}:{percent_format}% ({candidate_votes})")
    
    print("-------------------------")

    print(f"Winner: {winner_votes}")
 
    print("-------------------------")

    print(f'Congratulations {winner_votes}!')

    


#print(f"winner: {winner}", "Resources", "PyPoll_Resources_election_data.csv")

    


      #  print(len(row[2]))
 #       candidate = row[2]

  #      if candidate not in votes:
         #   votes[candidate]=+1

 #   for candidate in votes:
 #       print(f'candidate votes {candidate, votes[candidate]}')

    #print(f'Total votes {len(votes)}')
    #print(f'All votes {sum(votes.values)}')

   



       
      #  print(votes)

