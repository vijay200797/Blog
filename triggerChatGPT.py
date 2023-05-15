from chatGPT import ChatGPT
import sys
a ="""
Unit Test Case

def sum(a,b):
    return a+b 
"""
# ab =ChatGPT(a)
# print(ab)

if __name__ == "__main__":
    args = sys.argv[1]
    # if args =="":
    #     args = a
    ab =ChatGPT(args)
    print(ab)