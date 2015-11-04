def mergeSort(ls):
    while len(ls)>=2:
        mid=int(len(ls)/2)
        left=mergeSort(ls[:mid])
        right=mergeSort(ls[mid:])
        return merge(left,right)
    return ls

def merge(left,right):
    combine=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            combine.append(left[i])
            i+=1
        else:
            combine.append(right[j])
            j+=1
    while i<len(left):
        combine.append(left[i]) 
        i+=1
    while j<len(right):
        combine.append(right[j]) 
        j+=1 
    return combine
        
left=[1,5,7]
right=[2,4,9,10]
#print merge(left,right)

ls=[3,4,5,9,0,1,2]
print mergeSort(ls)