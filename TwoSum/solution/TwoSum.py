'''
Created on Aug 7, 2015

@author: jxy
'''
def twoSum(nums, target):
    list = []
    for val1 in nums:
        val2 = target - val1  
        index1 = nums.index(val1)
        
        if val2 in nums and nums.index(val2) > nums.index(val1):
            index2 = nums.index(val2)
            list.insert(0, index1)
            list.insert(1, index2)
            break

    print list
    return list 
            
def main():
    list = [2,7,11,15,17,19,20]
    list2 = [55,66]
    list.extend(list2)
    
    print list
    twoSum(list, 22)

if __name__ == '__main__':
    main()