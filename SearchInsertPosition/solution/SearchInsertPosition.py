'''
Created on Aug 7, 2015

@author: jxy
'''
def searchInsert(nums, target):
    return bsearch(nums, target, 0, len(nums)-1)

def bsearch(nums, target, left, right):
    
    if left > right:
        return left
    
    mid = (left + right) / 2
    if nums[mid] == target:
        return mid 
    elif target < nums[mid]:
        return bsearch(nums, target, left, mid-1)
    elif target > nums[mid]:
        return bsearch(nums, target, mid+1, right)

def main():
    list = [1,3,5,6]
    i = searchInsert(list, 4)
    

if __name__ == '__main__':
    main()