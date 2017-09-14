'''
Created on Sep 14, 2017

@author: jlearx
'''

if __name__ == '__main__':
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = [e for e in a if (e % 2 == 0)]
    print(b)
    