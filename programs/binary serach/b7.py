# Sq root of Number Finder

target = int(input("Enter No: "))
low = 0
high = target

while low <= high:
    mid = low+ (high-low)//2
    if mid*mid == target:
        ans = mid
    elif mid*mid < target:
        ans = mid
        low = mid+1
    else:
        high = mid-1
print(f"Target Nearest sqrt is {ans}")
        
    