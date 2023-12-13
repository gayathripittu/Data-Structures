import sys
import time
import os

def merge3(a, p, m1, m2, r):
    global count
    left = a[p-1 : m1]           # copying the array upto mid1-1 into left list
    mid= a[m1: m2 + 1]           # copying the array from mid1 to mid2 into mid list
    right = a[m2 + 1 : r]        # copying the array from mid2+1 to len(array)-1 into mid list

    left.append(100000000000)         # appending large value to left partition to do comparisons in the case when left partition sorting is completed
    mid.append(100000000000)
    right.append(100000000000)
    left_index = 0
    mid_index = 0
    right_index = 0
    for i in range(p-1, r):
        min_value = min([left[left_index], mid[mid_index], right[right_index]])   # finds the minimun value from the comparitive sub array's
        if min_value == left[left_index]:        # comparison to find the min vale is element of left subtree
            a[i] = left[left_index]             
            left_index += 1
        elif min_value == mid[mid_index]:        # comparison to find the min vale is element of mid parition
            a[i] = mid[mid_index]
            mid_index += 1
        else:                                     
            a[i] = right[right_index]
            right_index += 1
        count=count+2
    return a
    

def merge_sort3(a, p, r):
    if len(a[p-1:r])<=1:      # Base checking 
        return a
    else:
        m1 = p + ((r - p) // 3)      # calculating Mid 1
        m2 = p + 2 * ((r-p) // 3)    # calculating Mid 2
        merge_sort3(a, p, m1)         
        merge_sort3(a, m1+1, m2 + 1)   
        merge_sort3(a, m2+2, r)        
        result=merge3(a, p, m1, m2, r)
    return result


if __name__== '__main__':
    tot_list=[]
    data=os.path.join(os.getcwd())
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
        r=merge_sort3(tot_list[i], 1, len(tot_list[i]))
        print(len(tot_list[i]),",",count,",",((time.time()-st)*(10**9)))
        f.close()


