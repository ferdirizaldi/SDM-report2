#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        p = re.compile('\d+(?!\.)') #Make it to only accept integer, and no decimal point accepted

        if p.match(ai) and p.match(bi): #changed OR to AND since both have to satisfy the condition
                a=float(ai)
                b=float(bi)
                if 0<a<1000  and 0<b<1000: #no condition need for A to be bigger than B
                        valid=True
                else:
                        valid=False
        else:
                valid=False
                
        if valid:
                ans=a*b
                return ans
        else:
                return -1
        
                
def main ():
        matchstring = ''
        print("Type end to A to end the program")

        while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))
                matchstring = str(A)

if __name__ == '__main__':
	main()
