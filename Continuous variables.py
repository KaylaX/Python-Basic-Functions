#Poisson#

#The means are all about the same, which can be shown to be true 
# by doing some pen-and-paper work. The standard deviation of the 
# Binomial distribution gets closer and closer to that of the Poisson 
# distribution as the probability p gets lower and lower.

#given a Binomial distribution with some n,p, if you let n→∞ and p→0 
# in such a way that np→λ, then that distribution approaches a Poisson 
# distribution with parameter λ.

#the Binomial is based on discrete events, while the Poisson is based on 
# continuous events

samples_poisson=np.random.poisson(10,size=10000)

#normal distribution
# Draw 100000 samples from Normal distribution with stds of interest: samples_std1, samples_std3, samples_std10
samples_std1=np.random.normal(20,1,size=100000)
samples_std3=np.random.normal(20,3,size=100000)
samples_std10=np.random.normal(20,10,size=100000)

# Make histograms
plt.hist(samples_std1,normed=True,histtype='step',bins=100)
plt.hist(samples_std3,normed=True,histtype='step',bins=100)
plt.hist(samples_std10,normed=True,histtype='step',bins=100)

# Make a legend, set limits and show plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'))
plt.ylim(-0.01, 0.42)
plt.show()

# Compute mean and standard deviation: mu, sigma
mu=np.mean(belmont_no_outliers)
sigma=np.std(belmont_no_outliers)

# Sample out of a normal distribution with this mu and sigma: samples
samples=np.random.normal(mu,sigma,size=10000)

# Get the CDF of the samples and of the data
x_theor, y_theor=ecdf(samples)
x, y=ecdf(belmont_no_outliers)

# Plot the CDFs and show the plot
_ = plt.plot(x_theor, y_theor)
_ = plt.plot(x, y, marker='.', linestyle='none')
_ = plt.xlabel('Belmont winning time (sec.)')
_ = plt.ylabel('CDF')
plt.show()

#exponential
np.random.exponential(tau1,size=size)