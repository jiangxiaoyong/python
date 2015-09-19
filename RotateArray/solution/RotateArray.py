'''
Created on Aug 6, 2015

@author: jxy
'''
import collections

def rotate(nums, k):

    if k == 0:
        pass

    else:   
        d = k % len(nums)
        nums = nums[-d:] + nums[:-d]
        print nums
    
def main():
    list = [1,2,3,4]
    rotate(list, 2)

if __name__ == '__main__':
    main()