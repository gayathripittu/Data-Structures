import time             # importing time to calculate run time
import os               # importing os to change current directory

def merge(arr,p,q,r):        #merge function         
    n1 = q-p+1               
    global count             # defining count as global to access outside of program
    n2 = r-q
    L = [0]*(n1+1)          # creating a left array with size n1+1
    R = [0]*(n2+1)
    for i in range(n1):
        L[i] = arr[p+i]
    for i in range(n2):
        R[i] = arr[q+i+1]
    L[n1] = 1000000000           # assigning an larger value to merge the left over data in rightside
    R[n2] = 1000000000           #assigning an larger value to merge the left over data in leftside
    i,j = 0,0
    for k in range(p,r+1):
        if L[i]<=R[j]:            # checking if left element is less than or equal to right side element
            arr[k]=L[i]
            i+=1            
        else:
            arr[k]=R[j]
            j+=1
        count+=1               # incrementing count
    


def merge_sort(arr,p,r):
    if p<r:
        q = (p+r)//2             # calculating the mid value
        merge_sort(arr,p,q)      # calling the merge_sort function
        merge_sort(arr,q+1,r)
        merge(arr,p,q,r)          # calling the merge function


if __name__== '__main__':
    tot_list=[]
    data=os.path.join(os.getcwd())     # getting the current directory where we have files
    data=data+'\inputfiles'
    for root,folder,files in os.walk(data):
        for file in files:
            path=os.path.join(root,file)     # joining the filename with directory path inorder to get filepath
            f=open(path,'r')                  #opening the file
            arr=[]
            count =0
            for line in f:
                a=line.rstrip()                #reading the file and appending the data into list
                arr.append(int(a))
            tot_list.append(arr)
    tot_list=sorted(tot_list,key=len)



    for i in range(0,len(tot_list)):
        count=0
        st=time.time()                         # start time of algorithm
        merge_sort(tot_list[i],0,len(tot_list[i])-1)
        print(len(tot_list[i]),",",count,",",((time.time()-st)*(10**9)))
        f.close()



