'''
Created on Aug 7, 2015

@author: jxy
'''
def reverseWords(string):
    s = " ".join(string.strip().split()[::-1])
    print s
    
    
def main():
    s = 'the sky is blue'
    reverseWords(s)
    
if __name__ == '__main__':
    main()
