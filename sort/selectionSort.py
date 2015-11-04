def swap(ls,firstIndex,secondIndex):
    temp=ls[firstIndex]
    ls[firstIndex]=ls[secondIndex]
    ls[secondIndex]=temp

def indexOfMin(ls,startIndex=0):
        minIndex=startIndex
        for i in range(startIndex+1,len(ls)):
            if ls[i]<ls[minIndex]:
                minIndex=i
        return minIndex
    
    
def selectSort(ls):
    minIndex=0
    for startIndex in range(len(ls)-1):
        minIndex=indexOfMin(ls,startIndex)
        swap(ls,startIndex,minIndex)
        print ls


def selSort2(L):
    for i in range(len(L) - 1):
        minIndx = i 
        minVal= L[i] 
        for j in range(i+1,len(L)):
            if minVal > L[j]:
                minIndx = j
                minVal= L[j]
        temp = L[i]
        L[i] = L[minIndx]
        L[minIndx] = temp   
        print L 
    
ls1=[22, 11, 99, 88, 9, 7, 42]
ls2=[22, 11, 99, 88, 9, 7, 42]
selectSort(ls1)
print 'ls1:',ls1
selSort2(ls2)
print 'ls2:',ls2
    
        
        