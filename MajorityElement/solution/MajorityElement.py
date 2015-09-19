'''
Created on Aug 7, 2015

@author: jxy
'''
def majorityElement(nums):
    dic = {}
    while nums:
        val = nums.pop()
        
        if val not in dic:
            dic[val] = 1
        else:
            dic[val] +=1
    maxval = max(dic.values())
    key = [x for x, y in dic.items() if y == maxval]
    i = key[0]
    return i
    
def main():
    list = [1,1,2,2,2,2,3,4,5,5,5,6]
    i = majorityElement(list)
    print i

if __name__ == "__main__":
    main()