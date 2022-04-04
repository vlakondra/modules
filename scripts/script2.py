import sys

from  script1 import print_arg #not OK
import script1 #OK --  as s1 
#импортируем и используем script1

# def print_arg(x):
#     '''
#     qwerty
#     '''
#     print(999)

print(script1.LEARN_MOD)
print_arg(100)

print(sys.path)