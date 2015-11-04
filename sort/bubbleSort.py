def bubbleSort(ls):
    counter=0
    while counter<len(ls)-1:
        for i in range(0,len(ls)-1-counter):
            if ls[i+1]<ls[i]:
                swap(ls,i,i+1)
        counter+=1
        print ls
    
def swap(ls, aIndex, bIndex): # why swap(x,y) doesn't work?
    temp = ls[aIndex]
    ls[aIndex] = ls[bIndex]
    ls[bIndex] = temp
    
ls=[4,3,2,1]
bubbleSort(ls)

