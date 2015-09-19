'''
Created on Aug 7, 2015

@author: jxy
'''
def lengthOfLastWord(s):
    val = s.strip()

    if not val:
        return 0
    list = s.split()
    print list[len(list)-1]
    print len(list[len(list)-1])

    
def main():
    s = ' '
    i = lengthOfLastWord(s)
    print i
if __name__ == '__main__':
    main()