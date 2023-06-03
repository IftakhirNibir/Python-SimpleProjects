import random
import time
def native_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1
 

def binary_search(l,target):
    low = 0
    high = len(l)-1
    while high>=low:
        mid = (low+high)//2
        print(f"Mid = {mid}")
        if(l[mid]==target):
            return mid
        if target<l[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

if __name__ == '__main__':
#index    0,1,2,3,4,5
    s = 1000
    l = []
    while len(l)<s:
        l.append(random.randint(-5*s,5*s))
    l = sorted(l)
    l.extend([4985,4990,5500,5600])
    target = 5500
    start = time.time()
    print(native_search(l,target))
    end = time.time()
    print(f"For native search, it takes {end-start}s")
    start = time.time()
    print(binary_search(l,target))
    end = time.time()
    print(f"For binary search, it takes {end-start}s")