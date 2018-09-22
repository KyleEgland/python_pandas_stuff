#! python3
# Video https://youtu.be/lqjy9UqKKuo <- created by user Sentdex
import pandas as pd
import os
from tkinter import filedialog as file


# Create dataframe from csv file
# test = pd.read_csv('NCMB_Trending-ORIS-2017-ALL.csv')

# The below will analyze the data in the frame
# print(test.describe(include='all'))

# Display the beginning of the dataframe - put a number in the parenthesis
# in order to get a specific number of rows; default is 5 rows
# print(test.head(3))

# Display the ending of the data frame - put a number in the parenthesis in
# order to get a specific number of rows; default is 5 rows
# print(test.tail(10))

# Display the column names of the dataframe
# print(test.columns.values)

# Display the contents of a single column
# print(test['Support Case Number'])

##############
# Misc Notes #
##############
# This is for the workflow being created in the 'analyst.py' program
# First, set the users home directory, this can be done inside the file dialog
# line but I prefer to make it a variable...because reasons...

home = os.path.expanduser('~')

filename = file.askopenfile(initialdir=home, title='Just Pick One',
                            filetype=(('CSV File', ('.csv')), ('All Files', '*.*')))

print('[+] Selected:  {}'.format(os.path.basename(filename.name)))

sel_data = pd.read_csv(filename.name)

# Get the column headers of the data frame; note that this produces a numpy
# array object, NOT a list.  Below the .tolist() method is what makes this
# a list
cols = sel_data.columns.values

print('[*] The "cols" varialbe is a {}'.format(type(cols)))

cols = cols.tolist()

print('[*] After using ".tolist()" it is now a {}'.format(type(cols)))

print('[+] Headers:')

col_val = 0

for col in cols:
    print('{} {}'.format(col_val, col))
    col_val += 1

# Selecting specific data from the data frame:
# use '.iloc' method, sel_data.iloc[(start_row):(end_row), (start_col):(end_col)]
# Example 1, select the first 5 rows display the first 3 columns:
# sel_data.iloc[0:5, 0:2]
# Example 2, select the first 5 rows and only the first column:
# sel_data.iloc[0:5, 0]
# Example 3, select the bottom 5 rows and only the second column:
# sel_data.iloc[-5:, 1]
# Returning the selection as a list:
# sel_data.iloc[-5:, 0].values.tolist()

sample_col = input('Please make a column selection: ')

sample_rows = input('How many rows would you like? ')

sample_direction = input('Start at top of file or bottom? (enter top or bot)')

if sample_direction == 'top':
    sample_selection = sel_data.iloc[0:int(sample_rows), int(sample_col)].values.tolist()
    for thing in sample_selection:
        print(thing)












