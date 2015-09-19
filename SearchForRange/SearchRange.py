'''
Created on Aug 8, 2015

@author: jxy
'''
def searchRange(nums, target):
    
    list = []
    binaryS(nums, target, list, 0, len(nums)-1)
    if not list:
        return [-1,-1]
    else:
        return list
    
def binaryS(nums, target, list, left, right):
    if left > right:
        return
    
    mid = (left + right) /2
    
    if nums[mid] == target:
        ll = rr = mid
        while nums[ll] == target:
            ll = ll -1
        index1 = ll + 1
        list.append(index1)
        
        while nums[rr] == target:
            rr = rr + 1
        index2 = rr -1
        list.append(index2)
        
        return
        
    
    if target <= nums[mid]:
        binaryS(nums, target, list, left, mid-1)
    else:
        binaryS(nums, target, list, mid+1, right)
        
def main():
    nums = [5, 7, 8, 8, 8, 8,8,8,8,8,10]
    list = searchRange(nums, 8)
    print list
    
if __name__ == '__main__':
    main()