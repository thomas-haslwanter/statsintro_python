''' Test routine for source code that generates "F"igures

'''

# author: Thomas Haslwanter, date: Nov-2015

# additional packages
import os
import sys

figDir = os.path.join('..', r'ISP/Figures')
os.chdir(figDir)
startNr = 0     # if you don't want to go through all files

# make sure local imports work
sys.path.append('.')

pyList = [file for file in os.listdir('.') if (file[-3:]=='.py' and file[0]=='F')]
for number, file in enumerate(pyList):
    print( '{0}/{1}: {2}'.format(number+1, len(pyList), file) )
    if number >= startNr:
        exec(open(file).read())
    