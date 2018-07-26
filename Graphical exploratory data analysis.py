# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#histogram#

# Set default Seaborn style
sns.set()

# Compute number of data points: n_data
n_data=len(versicolor_petal_length)

# Number of bins is the square root of number of data points: n_bins
n_bins=np.sqrt(n_data)

# Convert number of bins to integer: n_bins
n_bins=int(n_bins)

# Plot the histogram
_ = plt.hist(versicolor_petal_length,bins=n_bins)

# Label axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count')

# Show histogram
plt.show()

#swarmplot#

# Create bee swarm plot with Seaborn's default settings
_ = sns.swarmplot(x='species',y='petal length (cm)',data=df)

# Label the axes
_ = plt.xlabel('species')
_ = plt.ylabel('petal length (cm)')
# Show the plot
plt.show()