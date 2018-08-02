#Thinking probabilistically-- Discrete variables
#Statistical inference involves taking your data to probabilistic 
#conclusions about what you would expect if you took even more data, 
# and you can make decisions based on these conclusions.

#np.random#

#Bernoulli#
# Seed random number generator
np.random.seed(42)

# Initialize the number of defaults: n_defaults
n_defaults=np.empty(1000)

# Compute the number of defaults
for i in range(1000):
    n_defaults[i] = perform_bernoulli_trials(100,0.05)


# Plot the histogram with default number of bins; label your axes
_ = plt.hist(n_defaults, normed=True)
_ = plt.xlabel('number of defaults out of 100 loans')
_ = plt.ylabel('probability')

# Show the plot
plt.show()