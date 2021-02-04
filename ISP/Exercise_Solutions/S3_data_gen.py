"""Generation of data for Chapter 'Data Input'

It shows how to generate
- formatted text-strings
- CSV files                      -> 'data.csv'
- otherwise formmated TXT-files  -> 'data_tab.txt', 'data_modified.txt'
- Excel files                    -> 'data.xls'
- Matlab files                   -> 'data.mat'
- Binary data                    -> 'data.raw'

One may have to install the package "xlwt" for this solution to run.
"""

# author:   Thomas Haslwanter
# date:     June-2020

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def save_txt(df: pd.DataFrame, out_file='data.csv') -> None:
    """ Save data to ASCII-format

    Parameters
    ----------
    df : Input data
    out_file : Output file; two other ASCII-files with same stem
               are also generated
    """

    # Saves the data to CSV-format, which means by default
    # - Separated by a comma
    # - With a column name
    # - With a running index on the left side
    df.to_csv(out_file)

    # Always let the user know when you generate a new file!!
    # If you use Python >3.7, you can use the "format-strings"
    print(f'Data have been saved in CSV-format to {out_file}')

    # For earlier versions of Python you have to use
    # print('Data have been saved in CSV-format to {0}'.format(out_file))

    # Simple file, tab-separated, no header, no index
    simple_file = out_file.replace('.csv', '_tab.txt')
    df.to_csv(simple_file, sep='\t', header=False, index=False)
    print(f'Data have been saved to {simple_file}')

    # Show how to add a file-header to an existing text file
    with open(out_file, 'r') as original:
        text = original.read()
        
    modified_file = out_file.replace('.csv', '_modified.txt')
    with open(modified_file, 'w') as modified:
        modified.write('This file was generated on Sept 19\n')
        modified.write(f'Sampling rate: {rate} [Hz]\n')
        modified.write(text)
    print(f'A file header has been added to {out_file}, '+
          f'and the new file saved as {modified_file}')


def save_xls(df: pd.DataFrame, out_file='data.xls') -> None:
    """ Save data to MS Excel-format

    Parameters
    ----------
    df : Input data
    out_file : Name of output file
    """

    # Save data to Excel-format
    df.to_excel(out_file, index=False)
    print(f'Data have been saved in MS-Excel format, to {out_file}')


def save_matlab(t: np.ndarray, data: np.ndarray, out_file='data.mat') -> None:
    """ Save data to Matlab-format

    Parameters
    ----------
    t : Time-values [sec]
    data : sine-wave
    out_file : Name of output file
    """
    # To save data to Matlab-format, we need the package "scipy.io", ...
    from scipy.io import savemat

    # ... and we have to put the data into a Python-dictionary
    # For this example, I add an information-text, and format the data as matrix
    data_mat = np.column_stack( (t, data) )
    data_dict = {'info':'These are demo-data, showing a sine-wave',
                'data': data_mat}

    savemat(out_file, data_dict)
    print(f'Data have been saved in Matlab format, to {out_file}')


def generate_binary(out_file='data.raw') -> None:
    """Generate binary data, with an ASCII-header with 256 byte, and
    three columns of data.

    Parameters
    ----------
    out_file : name of outfile
    """

    # To generate a more interesting signal, I produce a "chirp"
    from scipy.signal import chirp

    # Set the parameters
    length_header = 256     # byte

    # Generate a dummy header text
    txt = """This is the header.

    It has a length of 'length_header' byte. After the text, 
    it is padded with whitespaces."""
    out_txt = txt + ' '*(length_header-len(txt))

    # Write it to the out_file
    fh = open(out_file, 'wb')
    fh.write(out_txt.encode())

    # Generate some data
    t = np.arange(0,20, 0.1)
    x = np.sin(t)
    y = chirp(t, 3, np.max(t), 0.01)
    data = np.column_stack((t, np.sin(t), y*t))

    # Also write them to a file
    fh.write(data.tobytes())
    fh.close()
    print(f'Data have been written in binary form to {out_file}')


if __name__ == '__main__':

    # Set the parameters for a sine wave
    rate = 50
    freq = 2
    duration  = 4
    amp = 5
    noise_amp = 0.8

    # Calculate the sine-values
    delta = np.deg2rad(15)
    dt = 1/rate
    omega = 2*np.pi*freq

    t = np.arange(0, duration, dt)
    data = amp * np.sin(omega*t + delta) + noise_amp * np.random.randn(len(t))

    # Put them in a pandas-DataFrame, for easier text output
    df = pd.DataFrame({'t':t, 'values':data})

    # Show how to generate a formatted string in Python
    print(f'The first time-sample is {t[0]:5.3f}, '+
          f'and the first data-value is {data[0]:5.3f}\n')

    # Generate the output files
    save_txt(df)
    save_xls(df)
    save_matlab(t, data)
    generate_binary()


