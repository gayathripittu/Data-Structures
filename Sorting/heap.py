import os
import time

def heapify(arr,n,i):     
    global count                # defining count as global to access outside of program
    Largest=i 
    l=2*i+1                     # caluculating the left child node index
    r=2*i+2                     # caluculating the right child node index

    if(l<n):                    # checking if we have left child node to root nodes
        count=count+1
        if(arr[i]<arr[l]):      # comparing the root node with left node
            Largest=l

    if(r<n):
        count=count+1
        if(arr[Largest]<arr[r]):           # comparing the root node with right node
            Largest=r


    if(Largest!=i):                      # comparing largest node index with root node index
        (arr[i],arr[Largest])=(arr[Largest],arr[i])           # swapping the nodes
        heapify(arr,n,Largest)             

    


def heap_sort(arr):
    n=len(arr)

    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)               # heapify to build the max heap

    for i in range(n-1,0,-1): 
        (arr[i],arr[0])=(arr[0],arr[i])     # removing the last node of a tree
        heapify(arr,i,0)                   # heapify to build max heap for rest nodes except removed node
     


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
        heap_sort(tot_list[i])
        print(len(tot_list[i]),",",count,",",((time.time()-st)*(10**9)))
        f.close()



    
        
    
