#Combined first and last occurance of array search

def first(a,target):
    target = target
    start = 0
    end = len(a)-1
    while start <= end:
        mid = start + (end-start)//2
        
        if a[mid]==target:
            ans = mid
            end = end-1
        elif a[mid]> target:
            end = mid-1
        else:
            start = mid+1
    return ans
#last Occurance Finder
def last(b,target):
    target = target
    start = 0
    end = len(b)-1
    while start <= end:
        mid = start + (end-start)//2
        
        if b[mid]==target:
            ans = mid
            start=mid+1
        elif b[mid]> target:
            end = mid-1
        else:
            start = mid+1
    return ans

one = first([2,4,6,6,6,7,7,7,8,8,8,9],7)
print(f"first occurance of target 7 is {one}")
print()
en = last([2,4,6,6,6,7,7,7,8,8,8,9],7)
print(f"last occurance of target 7 is {en}")