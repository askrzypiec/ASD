import time
from datetime import datetime
# III search algorithm
def basicSearch(S, len, key):
    start_time = time.time()
    index =-1;
    for item in S:
        index += 1
        if item == key:
            end_time = time.time()
            print("found at index: "+ str(index))
            print(f"Total execution time: {end_time - start_time:.6f} seconds")
            return index
    end_time = time.time()
    print(" not found")
    print(f"Total execution time: {end_time - start_time:.6f} seconds")
    return -1



# III bin search algorithm

def binSerach(S, len, key, showtext):
    start_time = time.time()
    l=0
    r=len-1

    while (l<=r):
        m = (l+r)//2
        if S[m] == key:
            end_time = time.time()
            if showtext :
                ("found at index: " + str(m))
                print(f"Total execution time: {end_time - start_time:.6f} seconds")
            return m
        else:
            if S[m]> key:
                r-=1
            else:
                l+=1
    end_time = time.time()
    if showtext:
        print(f"Total execution time: {end_time - start_time:.6f} seconds")
    return -1

# IV bin search algorithm
def min(S,s):
    a = S[s]
    min_index = s
    for i in range(s + 1, len(S)):
        if S[i] < S[min_index]:
            min_index = i
    return min_index
def swap(S,a,b):
    c = S[a]
    S[a] = S[b]
    S[b] = c

def Selection_sort(S, len):
    start_time = time.time()
    i=0
    while i<len:
        min_index = min(S,i)
        swap(S,i,min_index)
        i+=1


    end_time = time.time()
    print(S)
    print(f"Selection_sort _Total execution time: {end_time - start_time:.6f} seconds")
    return S

# IV Insertion_sort

def Insertion_sort(S, len):
    start_time = time.time()

    i=0
    while i<len-1:
        if S[i]>S[i+1]:
            swap(S,i,i+1)
            print(S)
            i-=1
            if i<0: i=0;
        else:
            i+=1



    end_time = time.time()
    print(S)
    print(f"Insertion_sort _Total execution time: {end_time - start_time:.6f} seconds")
    return S