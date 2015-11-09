'''Get data from MS-Excel files, which are stored zipped on the WWW. '''

# author: Thomas Haslwanter, date: Nov-2015

# Import standard packages
import pandas as pd

# additional packages
import io
import zipfile

# Python 2/3 use different packages for "urlopen"
import sys
if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    from urllib import urlopen
    
def getDataDobson(url, inFile):
    '''Extract data from a zipped-archive on the web'''

    # get the zip-archive
    GLM_archive = urlopen(url).read()

    # make the archive available as a byte-stream
    zipdata = io.BytesIO()
    zipdata.write(GLM_archive)

    # extract the requested file from the archive, as a pandas XLS-file
    myzipfile = zipfile.ZipFile(zipdata)
    xlsfile = myzipfile.open(inFile)

    # read the xls-file into Python, using Pandas, and return the extracted data
    xls = pd.ExcelFile(xlsfile)
    df  = xls.parse('Sheet1', skiprows=2)

    return df

if __name__ == '__main__':
    # Select archive (on the web) and the file in the archive
    url = 'http://cdn.crcpress.com/downloads/C9500/GLM_data.zip'
    inFile = r'GLM_data/Table 2.8 Waist loss.xls'

    df = getDataDobson(url, inFile)
    print(df)

    input('All done!')
