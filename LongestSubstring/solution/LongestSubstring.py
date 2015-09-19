'''
Created on Aug 7, 2015

@author: jxy
'''
def lengthOfLongestSubstring(s):
    list = []
    max = 0
    result = 0
    for i in range(0, len(s) -1):
        str = s[i:]
        for subchar in str:
            if subchar not in list:
                list.append(subchar)
            else:
                if len(list) > max:
                    result = len(list)
                    max = result
                del list[:]
                break
                
    print result
    return result
    
def main():
    s = 'abcabcbefgdb'
    i = lengthOfLongestSubstring(s)
    print i
    
if __name__ == '__main__':
    main()