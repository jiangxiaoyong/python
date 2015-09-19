'''
Created on Aug 8, 2015

@author: jxy
'''
def isPalindrome(s):
    list = []
    for char in s:
        if char.isalnum():
            list.append(char)
            
    string = ''.join(list)
    reverse = ''.join(list[::-1])
    print string.lower()
    print reverse.lower()
    
    if string.lower() == reverse.lower():
        return True
    else:
        return False

def main():
   s = "A man, a plan, a canal: Panama"
   bool = isPalindrome(s)
   
   list = ['2','3','4']
   list.reverse()
   print list
   print bool

if __name__ == '__main__':
    main()