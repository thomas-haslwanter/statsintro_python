""" Solution to Exercise "Data Input" """

# author: Thomas Haslwanter, date: [xxx]-2021

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from urllib.request import urlopen
import io
import zipfile


def getDataDobson(url: str, inFile: str) -> pd.DataFrame:
    """ Extract data from a zipped-archive on the web. """

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
    # 1.1 Numpy --------------------
    # Read in a CSV file, and show the top:
    inFile1 = 'swim100m.csv'
    data = pd.read_csv(inFile1)
    print(data.head())

    # Read in an excel file, and show the bottom
    inFile2 = 'Table 2.8 Waist loss.xls'

    xls = pd.ExcelFile(inFile2)
    data = xls.parse('Sheet1', skiprows=2)
    print(data.tail())

    # Read in a zipped data-file from the WWW
    # Select archive (on the web) and the file in the archive
    url = 'https://s3-eu-west-1.amazonaws.com/s3-euw1-ap-pe-ws4-cws-documents.ri-prod/9781138741515/GLM_data.zip'
    inFile = r'Table 2.8 Waist loss.xls'

    df = getDataDobson(url, inFile)
    print(df.tail())