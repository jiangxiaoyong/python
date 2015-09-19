'''
Created on Aug 8, 2015

@author: jxy
'''
def search(nums, target):
    if len(nums) == 1:
        if target == nums[0]:
            return 0
        else:
            return -1
    else:
        i = binarySearch(nums, target, 0, len(nums)-1)
        return i

def binarySearch(nums, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) / 2
    
    if nums[mid] == target:
        return mid
    
    if nums[left] < nums[mid]:
        if target >= nums[left] and target <= nums[mid]:
            return binarySearch(nums, target, left, mid-1) #search left
        else:
            return binarySearch(nums, target, mid+1, right)
    elif nums[left] > nums[mid]:
        if target >= nums[mid] and target <= nums[right]:
            return binarySearch(nums, target, mid +1, right)
        else:
            return binarySearch(nums, target, left, mid-1)
    elif nums[left] == nums[mid]:
        if nums[mid] != nums[right]:
            binarySearch(nums, target, mid+1, right)
            
def main():
    list = [4,5,6,7,0,1,2]
    i = search(list, 6)
    print i
    
if __name__ == '__main__':
    main()