'''
Created on Aug 7, 2015

@author: jxy
'''
def removeElement(nums, val):
    while val in nums:
        nums.remove(val)

    print nums
    
def main():
    list = [3,3]
    removeElement(list, 3)

if __name__ == '__main__':
    main()