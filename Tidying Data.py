#For data to be tidy, it must have:
#Each variable as a separate column.
#Each row as a separate observation.

# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(airquality, id_vars=['Month', 'Day'])

# Print the head of airquality_melt
print(airquality_melt.head())

#pd.melt()
#The id_vars represent the columns of the data you do not want to 
#melt (i.e., keep it in its current shape), while the value_vars 
#represent the columns you do wish to melt into rows. 
#By default, if no value_vars are provided, all columns not set 
#in the id_vars will be melted. 

# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(airquality, id_vars=['Month', 'Day'])

# Print the head of airquality_melt
print(airquality_melt.head())

#You can rename the variable column by specifying an argument 
#to the var_name parameter, and the value column by specifying 
#an argument to the value_name parameter. 

# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(airquality,id_vars=['Month', 'Day'], var_name='measurement', value_name='reading')

# Print the head of airquality_melt
print(airquality_melt.head())

#.pivot_table
#.pivot_table() has an index parameter which you can use to 
#specify the columns that you don't want pivoted: It is similar 
#to the id_vars parameter of pd.melt(). Two other parameters 
#that you have to specify are columns (the name of the column 
#you want to pivot), and values (the values to be used when the 
#column is pivoted).

# Print the head of airquality_melt
print(airquality_melt.head())

# Pivot airquality_melt: airquality_pivot
airquality_pivot = airquality_melt.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading')

# Print the head of airquality_pivot
print(airquality_pivot.head())

#Resetting the index
#After pivoting airquality_melt in the previous exercise, 
# you didn't quite get back the original DataFrame.
# What you got back instead was a pandas DataFrame with a 
# hierarchical index (also known as a MultiIndex).
# Hierarchical indexes are covered in depth in Manipulating DataFrames with pandas. In essence, they allow you to group columns or rows by another variable - in this case, by 'Month' as well as 'Day'.
# There's a very simple method you can use to get back the original DataFrame from the pivoted DataFrame: .reset_index().

# Print the index of airquality_pivot
print(airquality_pivot.index)

# Reset the index of airquality_pivot: airquality_pivot
airquality_pivot = airquality_pivot.reset_index()

# Print the new index of airquality_pivot
print(airquality_pivot.index)

#Pivoting duplicate values with aggfunc
# Pivot airquality_dup: airquality_pivot
airquality_pivot = airquality_dup.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading', aggfunc=np.mean)

# Reset the index of airquality_pivot
airquality_pivot = airquality_pivot.reset_index()

#Splitting a column with .str
# Melt tb: tb_melt
tb_melt = pd.melt(tb, id_vars=['country', 'year'])

# Create the 'gender' column
tb_melt['gender'] = tb_melt.variable.str[0]

# Create the 'age_group' column
tb_melt['age_group'] = tb_melt.variable.str[1:]

# Print the head of tb_melt
print(tb_melt.head())

#Splitting a column with .split() and .get()
# Melt ebola: ebola_melt
ebola_melt = pd.melt(ebola, id_vars=['Date', 'Day'], var_name='type_country', value_name='counts')

# Create the 'str_split' column
ebola_melt['str_split'] = ebola_melt['type_country'].str.split('_')

#You can accomplish this by accessing the str attribute of the 
# column and using the .get() method to retrieve the 0 or 1 index
# Create the 'type' column
ebola_melt['type'] = ebola_melt['str_split'].str.get(0)

# Create the 'country' column
ebola_melt['country'] = ebola_melt['str_split'].str.get(1)

# Print the head of ebola_melt
print(ebola_melt.head())