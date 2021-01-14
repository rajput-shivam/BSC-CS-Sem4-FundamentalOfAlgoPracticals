def search(a,low,high,n):
    if low==high==n:
        return a[low]    
    else:
        mid=partition(a,low,high)
        if mid==n:
            return a[mid]
        elif n<mid:
            return search(a,low,mid-1,n)
        else:
            return search(a,mid+1,high,n)
                
            
def partition(a,low,high):
    pivot=a[low] 
    i=low
    j=high+1
    while i<j:
        
        while True:
            i=i+1
            if a[i]>pivot or i==high:
                break
        while True:
            j=j-1
            if a[j]<=pivot or j==low:   
                break
        if i<j:
            swap(a,i,j)
    swap(a,low,j)
    return j     

def swap(a,x,y):
    temp=a[x]
    a[x]=a[y]
    a[y]=temp


n=int(input("enter n:"))
a=[2, 5, 3, 4, 1, 20,9]
ans=search(a,0,len(a)-1,n-1)
print("ANS=",ans)




