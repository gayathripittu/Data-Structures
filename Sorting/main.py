import heap
import Merge_Sort
import insertion
import Merge_Sort3
import os
import time
import copy


os.chdir(r"D:\Project 1B\inputfiles")        # changing the current directory to directory where we have input files

tot_list=[]
 
data=os.path.join(os.getcwd())
for root,folder,files in os.walk(data):
    for file in files:
        path=os.path.join(root,file)     # joining the filename with directory path inorder to get filepath
        f=open(path,'r')                  #opening the file
        arr=[]
        count =0
        for line in f:
            a=line.rstrip()#reading the file and appending the data into list
            arr.append(int(a))
        tot_list.append(arr)




if __name__== '__main__':
    tot_list=sorted(tot_list,key=len)
    m_l=copy.deepcopy(tot_list)
    i_l=copy.deepcopy(tot_list)
    m3_l=copy.deepcopy(tot_list)
    print("-------------------------!Heap sort!---------------------------")
    for i in range(len(tot_list)):
        st=time.time()
        heap.count=0
        heap.heap_sort(tot_list[i])
        print(len(tot_list[i]),",",heap.count,",",((time.time()-st)*(10**9)))
        f.close()
        
    print("-------------------------!Merge Sort!-------------------------!")
    for i in range(len(m_l)):
        st=time.time()
        Merge_Sort.count=0
        Merge_Sort.merge_sort(m_l[i],0,len(m_l[i])-1)
        print(len(m_l[i]),",",Merge_Sort.count,",",((time.time()-st)*(10**9)))
        f.close()

    print("---------------------!3 way mergesort!---------------------")

    for i in range(len(tot_list)):
        st=time.time()
        Merge_Sort3.count=0
        sort_a=Merge_Sort3.merge_sort3(m3_l[i],1,len(m3_l[i]))
        print(len(m3_l[i]),",",Merge_Sort3.count,",",((time.time()-st)*(10**9)))
        f.close()
    print("---------------------!Insertion Sort!---------------------")

    for i in range(len(i_l)):
        st=time.time()
        insertion.count=0
        if(len(i_l[i])<170000):
            insertion.insertion_sort(i_l[i])
        print(len(i_l[i]),",",insertion.count,",",((time.time()-st)*(10**9)))
        f.close()







