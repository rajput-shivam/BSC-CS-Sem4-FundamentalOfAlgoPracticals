def quickSort(a,low,high):
    if low<high:
        mid=partition(a,low,high)
        quickSort(a,low,mid-1)
        quickSort(a,mid+1,high)

def partition(a,low,high):
    pivot=a[low] 
    i,j=low,high+1
    while i<j:
        while True:
            i=i+1
            print("i",i)
            if a[i]>pivot or i==high:
                break
        while True:
            j=j-1
            print("j",j)
            if a[j]<=pivot:      
                break
        if i<j:
            swap(a,i,j)
    swap(a,low,j)
    print("\n\na:",a,"\npovot:",pivot)
    return j               
            

def swap(a,x,y):
    temp=a[x]
    a[x]=a[y]
    a[y]=temp

a=[51,42,1,56,44,33,37,28,30,14,19,1]
print(a)
quickSort(a,0,len(a)-1)
print(a)
