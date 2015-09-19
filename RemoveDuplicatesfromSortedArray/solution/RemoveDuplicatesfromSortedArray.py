'''
Created on Aug 7, 2015

@author: jxy
'''
def removeDuplicates(nums):
    newlist = list(set(nums))
    print newlist

def removeDuplicatesII(nums):
    dic = {}
    list = []   
    
    while nums:
        val = nums.pop()
       
        if val not in dic:
            dic[val] = 1
            list.append(val)
            
        elif val in dic and dic[val] <2:
            dic[val] +=1
            list.append(val)

    list.reverse()
    print len(list)
    
def main():
    list = [1,1,1,2,2,3]
    removeDuplicates(list)
    removeDuplicatesII(list)

if __name__ == '__main__':
    main()