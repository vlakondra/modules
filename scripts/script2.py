import os,sys

from  script1 import print_arg #not OK
import script1 #OK --  as s1 

# from utils import alpha
# from ./utils import single

##!!!!!!!!!!!
root =    os.path.dirname(os.path.pardir)
print('root1', root)
absroot = os.path.abspath(root)
print('absroot', absroot)

sys.path.insert(0, absroot)  # os.path.abspath(root))
##!!!!!!!!!!!

from utils import alpha
alpha.is_alpha('!')
# import utils.repeat




#импортируем и используем script1

# def print_arg(x):
#     '''
#     qwerty
#     '''
#     print(999)

# print(single('qw'))
print(script1.LEARN_MOD)
print_arg(100)

print("sys.path",sys.path)