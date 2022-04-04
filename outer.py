import os, sys
from os import path 
import utils


# sys.path[0]=''

print("dirname",os.pardir, __name__,__file__,path.abspath(__file__))

ROOT = os.path.abspath(os.path.join( 
                  os.path.dirname(__file__), 
                  os.pardir) 
)
print('ROOT',ROOT)
print('file',os.path.abspath(__file__))
sr= os.path.join(os.path.dirname(os.path.abspath(__file__)),'scripts')
print('sr',sr)
upath = os.path.join(os.path.dirname(os.path.abspath(__file__)),'utils')
print ("upath",upath)
sys.path.append(upath)
sys.path.insert(0,sr)

import script2
script2.alpha.is_alpha('?')

print(sys.path)

r=utils.alpha.is_alpha('s') # not work!!
utils.alpha.tt()
print(utils.script1.LEARN_MOD)


# import utils.repeat
# import repeat,alpha,single

# def letter():
#     while True:
#         l = input("VVOD ")
#         if repeat.is_repeat(l, ['a','b','c']):
#             return l

# print(letter())