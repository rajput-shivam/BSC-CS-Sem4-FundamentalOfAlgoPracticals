def mergeSort(a):
    if len(a)>1:
        mid = len(a)//2
        left= a[:mid]
        right= a[mid:]
        print("before left and right: ",left,right)
        mergeSort(left)
        mergeSort(right)
        print("after left and right: ",left,right)
        
        i=j=k=0
        print("\nbefore a:",a)
        while i<len(left) and j<len(right):   
            if left[i] < right[j]:
                a[k] = left[i]
                i=i+1
            else:
                a[k] = right[j]
                j=j+1
            k=k+1
        print("after 1st loop a:",a)
        while i<len(left):
            a[k]=left[i]
            i=i+1
            k=k+1
        print("after 2nd loop a:",a)
        while j<len(right):
            a[k]=right[j]
            j=j+1
            k=k+1
        print("after last loop a:",a,"\n")
        
    

a = [534,246,933,933,127,277,321,454,565,2201] 
mergeSort(a)
print("\n\n\nANSWER",a)
