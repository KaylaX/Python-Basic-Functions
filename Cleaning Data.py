# Convert the sex column to type 'category'
tips.sex = tips.sex.astype('category')

# Convert the smoker column to type 'category'
tips.smoker = tips.smoker.astype('category')

# Print the info of tips
print(tips.info())

#pandas will store arbitrary strings in a different way
#can convert to category to save memory

# Convert 'total_bill' to a numeric dtype
tips['total_bill'] =pd.to_numeric(tips['total_bill'], errors='coerce')

# Convert 'tip' to a numeric dtype
tips['tip'] = pd.to_numeric(tips['tip'],errors='coerce')

# Print the info of tips
print(tips.info())

#If you expect the data type of a column to be numeric (int or float), 
# but instead it is of type object, this typically means that there 
# is a non numeric value in the column, which also signifies bad data.

#regular expressions
# Import the regular expression module
import re

# Compile the pattern: prog
prog = re.compile('\d{3}-\d{3}-\d{4}')

# See if the pattern matches
result = prog.match('123-456-7890')
print(bool(result))

# See if the pattern matches
result = prog.match('1123-456-7890')
print(bool(result))

# Import the regular expression module
import re

# Find the numeric values: matches
matches = re.findall('\d+', 'the recipe calls for 10 strawberries and 1 banana')
#+ can help you find all the digits!

# Print the matches
print(matches)

#Write patterns to match:

#A telephone number of the format xxx-xxx-xxxx. You already did this in a previous exercise.
#A string of the format: A dollar sign, an arbitrary number of digits, a decimal point, 2 digits.
#Use \$ to match the dollar sign, \d* to match an arbitrary number of digits, \. to match the decimal point, and \d{x} to match x number of digits.
#A capital letter, followed by an arbitrary number of alphanumeric characters.
#Use [A-Z] to match any capital letter followed by \w* to match an arbitrary number of alphanumeric characters.

# Write the first pattern
pattern1 = bool(re.match(pattern='\d{3}-\d{3}-\d{4}', string='123-456-7890'))
print(pattern1)

# Write the second pattern
pattern2 = bool(re.match(pattern='\$\d*\.\d{2}', string='$123.45'))
print(pattern2)

# Write the third pattern
pattern3 = bool(re.match(pattern='[A-Z]\w*', string='Australia'))
print(pattern3)

#Define functions
# Define recode_sex()
def recode_sex(sex_value):

    # Return 1 if sex_value is 'Male'
    if sex_value == 'Male':
        return 1
    
    # Return 0 if sex_value is 'Female'
    elif sex_value == 'Female':
        return 0
        
    # Return np.nan    
    else:
        return np.nan

# Apply the function to the sex column
tips['sex_recode'] = tips.sex.apply(recode_sex)

# Print the first five rows of tips
print(tips.head())

#Lambda
# Write the lambda function using replace
tips['total_dollar_replace'] = tips['total_dollar'].apply(lambda x: x.replace('$', ''))

# Write the lambda function using regular expressions
tips['total_dollar_re'] = tips['total_dollar'].apply(lambda x:re.findall('\d+\.\d+', x)[0])

# Print the head of tips
print(tips.head())

#Drop duplicates
# Create the new DataFrame: tracks
tracks = billboard[['year','artist','track','time']]

# Print info of tracks
print(tracks.info())

# Drop the duplicates: tracks_no_duplicates
tracks_no_duplicates = tracks.drop_duplicates()

# Print info of tracks
print(tracks_no_duplicates.info())

#filling missing values with the mean
# Calculate the mean of the Ozone column: oz_mean
oz_mean = airquality['Ozone'].mean()

# Replace all the missing values in the Ozone column with the mean
airquality['Ozone'] = airquality['Ozone'].fillna(oz_mean)

# Print the info of airquality
print(airquality.info())

#Testing your data with asserts
# Assert that there are no missing values
assert pd.notnull(ebola).all().all()

#.all().all()). The first .all() method will return a True or False for each column, 
# while the second .all() method will return a single True or False.

# Assert that all values are >= 0
assert (ebola>=0).all().all()

def check_null_or_valid(row_data):
    """Function that takes a row of data,
    drops all missing values,
    and checks if all remaining values are greater than or equal to 0
    """
    no_na = row_data.dropna()[1:-1]
    numeric = pd.to_numeric(no_na)
    ge0 = numeric >= 0
    return ge0

# Check whether the first column is 'Life expectancy'
assert g1800s.columns[0] == 'Life expectancy'

# Check whether the values in the row are valid
assert g1800s.iloc[:, 1:].apply(check_null_or_valid, axis=1).all().all()

# Check that there is only one instance of each country
assert g1800s['Life expectancy'].value_counts()[0] ==1

# Concatenate the DataFrames row-wise
gapminder = pd.concat([g1800s,g1900s,g2000s])

# Print the shape of gapminder
print(gapminder.shape)

# Print the head of gapminder
print(gapminder.head())

# Test if country is of type object
assert gapminder.country.dtypes == np.object