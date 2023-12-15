import sys
import time

def dynamic(amount,d,k):  # function for finding minimu no.of coins for amount n
    c,s=[],[]            # creating empty c and s lists to store results of subproblems and index of minimum coins
    coin=0
    c.append(0)
    s.append(0)
    for i in range(1,amount+1):
        min=float('inf')         # taking greatest value as minimum
        for j in range(0,k):
            if(d[j]<=i):
                if(1+c[i-d[j]]<min):
                    coin=j
                    min=1+c[i-d[j]]     
        c.append(min)                    # appending the minimum no.of coins of 'i' cents to the "c" list    (storing sub problem's result)
        s.append(coin)                   # appending the index of coin in optimal solution
    return c,s


def change_print(s,d,n):       # function to print used coins
    while n>0:
        print(d[s[n]],end=' ')
        n=n-d[s[n]]




if __name__ == "__main__":          # main function
    change=int(sys.argv[1])         # command line argument 1= amount     
    k=int(sys.argv[2])              #  length of denominations
    d=[]                            # an empty array for denominations
    for i in range(3,k+3): 
        d.append(int(sys.argv[i]))              # appending the user input denominations into 'd' list
    st=time.perf_counter_ns()
    c,s=dynamic(change,d,k)            
    print("----------for n=",change,"----------")
    change_print(s,d,change)
    print()
    et=time.perf_counter_ns()
    print(et-st)          


