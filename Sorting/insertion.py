import time                              # importing time to caluculate execution time of program
import os                                # importing OS to change directory and to get path of input file


def insertion_sort(elements_arr):# function to perform insertion sort
    global count
    for i in range(1, len(elements_arr)):        # outer loop 
        key=elements_arr[i]
        for j in range(i-1,-1,-1):               # inner loop to sort elements left side of the 'i'th element
            count=count+1
            if(elements_arr[j]>key):             
                elements_arr[j+1]=elements_arr[j]
            else:
                break
            elements_arr[j]=key

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
        insertion_sort(tot_list[i])
        print(len(tot_list[i]),",",count,",",((time.time()-st)*(10**9)))
        f.close()

    




