'''
Created on Aug 7, 2015

@author: jxy
'''
def anagrams(strs):
    dic = {}
    result = []
    for str in strs:
        if not str:
            pass
        else:
            val = ''.join(sorted(str))
            
            if val not in dic:
                dic[val] = [str]
            else:
                dic[val].append(str)
    
    
    for v in dic.values():
        for s in v:
            result.append(s)
    print result
    
def main():
    strs = ['anger', 'geran','bill','llib','dog','ogd','pretty','ttypre','preytt']
    s1 = ['']
    anagrams(strs)
    
if __name__ == '__main__':
    main()