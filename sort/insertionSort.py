def insert(ls,value):
    if ls==[] or value>=ls[-1]:
        ls.append(value)
    else:
        ls.append(value)
        i=len(ls)-2
        while i>=0:
            if ls[i]>value:
                ls[i+1]=ls[i]
                i-=1
            else:
                ls[i+1]=value
                break
        if ls[0]>value:
            ls[0]=value


def insertionSort(ls):
    sortedLS=[]
    for value in ls:
        insert(sortedLS,value)
    return sortedLS
    
def insertionSort2(ls):
    if ls == [] or len(ls) == 1:
        return ls
        
    for i in range(1, len(ls)):
        while i > 0 and ls[i] < ls[i-1]:
            swap(ls, i, i-1)
            i-=1

    return ls

#slightly better/more efficient compared to insertionSort2
def insertionSort3(ls):
    if ls == [] or len(ls) == 1:
        return ls

    for i in range(1, len(ls)):
        temp = ls[i]
        while i > 0 and temp < ls[i-1]:
            ls[i] = ls[i-1]
            i-=1
        ls[i] = temp
    return ls

def swap(ls, aIndex, bIndex):
    temp = ls[aIndex]
    ls[aIndex] = ls[bIndex]
    ls[bIndex] = temp
    
ls=[2, 5, 7, 11, 13, 3, 9, 6,1]
print insertionSort3(ls)
