''' Test routine for source code that generates "F"igures

'''

# author: Thomas Haslwanter, date: Sept-2015

# additional packages
import os

pyList = [file for file in os.listdir('.') if (file[-3:]=='.py' and file[0]=='F')]
for number, file in enumerate(pyList):
    print( '{0}/{1}: {2}'.format(number+1, len(pyList), file) )
    exec(open(file).read())
    