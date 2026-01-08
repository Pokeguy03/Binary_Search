def lower(arr,target,n):
    low=0
    high=n-1
    while low<=high:
        mid=(high+low)//2
        if arr[mid]>=target:
            ans=mid
            high=mid-1
        else:
            low=mid+1 
    return ans
    
arr=[1,2,4,5,6,7,7,8]
target=6
n=len(arr)
sol=lower(arr,target,n)
print(sol)


#formula:
#arr[index]>=target
