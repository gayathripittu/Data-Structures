import time        #importing required packages sys for command line arguments and time for calculating time
import sys

def greedy(change,d,k):
    n=change
    coins_usedlist=[]        # taking another empty list to store the coins used for giving change
    for i in range(0,k):          # checking the denominations list from 0 index to k index
        if(change/d[i]>=1):         # if amount is dividing with current index value(d[i]) then d[i] is the one of the coin used for solution
            s=d[i]
            coins_usedlist.extend([s]*int((change/d[i]))) # we are appending the d[i] values into list
            change=change-((change//d[i])*d[i])           # and subtracting the d[i] from change

    print(n,coins_usedlist)
    et=time.perf_counter_ns()
    print(et-st)



if __name__ == "__main__":          # main function
    change=int(sys.argv[1])         # command line argument 1= amount     
    k=int(sys.argv[2])              #  length of denominations
    d=[]                            # an empty array for denominations
    for i in range(3,k+3): 
        d.append(int(sys.argv[i]))              # appending the user input denominations into 'd' list

    d.sort(reverse=True)               # sorting the denominations list into descending order
    st=time.perf_counter_ns()                    # start time
    greedy(change,d,k)          # function call

        
    
