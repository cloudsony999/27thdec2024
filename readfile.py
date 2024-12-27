import os
import sys
file='rupsa-streeja123.txt'
if os.path.isfile(file):
    f=open(file,'r')
    st=f.read()
    print(st)
else:
    print('sorry ....')
    sys.exit()
    print('------------------------')


print('------------------------')

f.close()


