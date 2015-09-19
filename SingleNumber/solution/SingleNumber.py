'''
Created on Aug 8, 2015

@author: jxy
'''
def singleNumber(nums):
    dic = {}
    for val in nums:
        if val not in dic:
            dic[val] = 1
        else:
            dic[val] += 1
    minval = min(dic.values())
    key = [x for x, y in dic.items() if y == minval]
    result = key[0]
    print result
    return result
    
    
def main():
    list =  [1,2,1,2,3,3,4,5,5,6,6,7,7]
    i = singleNumber(list)
    print i
    
if __name__ == '__main__':
    main()