import sys                 # importing the required packages sys for command line arguments and time for calculating time
import time


def naive(change,d,k):
    count=float('inf')              # assigning the largest value (infinity) into count, count is the variable, we are storing minimum no.of required coins for given amount
    if(change<=0):              
        return 0
    for i in range(0,k):               # for loop from 0 index to k index
        if(d[i]<=change):        
            count=min(count,naive(change-d[i],d,k)+1)       # finding the minimum between prev count and current index count
    return count


if __name__ == "__main__":                  # main function
    change=int(sys.argv[1])                 # command line argument 1= amount
    k=int(sys.argv[2])                      # length of denominations
    d=[]                                    # an empty array for denominations
    for i in range(3,k+3):
        d.append(int(sys.argv[i]))          # appending the user input denominations into 'd' list
    st=time.time()                          # start time
    print("------------for amount n=",change,"------------")
    res=naive(change,d,k)                   # function call
    print("-----------------------naive recursive solution-------------------")
    print(change,res)                       # result printing
    print(((time.time()-st)*(10**9)))
                
    
    
