'''Get data from MS-Excel files, which are stored zipped on the WWW

Note that Python 2.x is no longer supported!
'''

# author:   Thomas Haslwanter
# date:     April-2020

# Import standard packages
import pandas as pd

# additional packages
import io
import zipfile
from urllib.request import urlopen
    
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
    url = 'https://www.routledge.com/downloads/K32369/GLM.dobson.data.zip'
    inFile = r'Table 2.8 Waist loss.xls'

    df = getDataDobson(url, inFile)
    print(df)

    input('All done!')
