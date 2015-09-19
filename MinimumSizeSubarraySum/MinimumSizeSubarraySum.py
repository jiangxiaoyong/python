'''
Created on Aug 9, 2015

@author: jxy
'''
def minSubArrayLen(s, target):
    sum = 0
    list = []
    dic = {}
    
    for val in range(0, len(s)-1):
        subArray = s[val:]
        for num in subArray:
            if sum < target:
                sum += num
                list.append(num)
            else:
                break
        if sum >= target: #store value as long as the sum bigger than target
            dic[val] = len(list)
            
        del list[:] #empty list
        sum = 0

            
    for k,v in dic.items():
        print k,v
    print min(dic.values())
    
def main():
    list = [2,3,1,2,4,3]
    i = minSubArrayLen(list, 7)
    print i
    
if __name__ == '__main__':
    main()