#General imports
from sklearn import datasets
from sklearn import metrics
import pandas as pd #imports Pandas
import numpy as np #imports NumPy
import matplotlib.pyplot as plt #enables plotting
%matplotlib inline

#Methods available include: 
#    .min() - Compute minimum value
#    .max() - Compute maximum value
#    .mean() - Compute mean value
#    .median() - Compute median value
#    .mode() - Compute mode value(s)
#    .count() - Count the number of observations
#    .std() - Compute Standard Deviation
#    .var() - Compute variance

#Reads the examples
df = pd.DataFrame({'example1' : [18, 24, 17, 21, 24, 16, 29, 18], 'example2' : [75, 87, 49, 68, 75, 84, 98, 92], 'example3' : [55, 47, 38, 66, 56, 64, 44, 39] })
print(df)

#Calculates the mean for each column
df.mean(axis=1)

#Calculate median, mode, max, min for each column
df.max(axis=1)
df.min(axis=1)
df.median(axis=1)
df.mode

#Prints the interquartile range
print (df.quantile(.50))
print (df.quantile(0.25))
print (df.quantile(0.75))
print (df.median())

#Plots
df.plot(kind='kde')
df.plot(kind='box')
df.plot(kind='line')

#prints variance for one column
print(df["example1"].var()) 

df.var() #variance
df.std() #standard deviation
df.count() #counts observations
df.describe() #count, mean, std, min, 25%, 50%, 75%, max
df.corr() #correlation

variable = pd.read_csv("filename.csv") #imports dataset using pandas
variable.head() #shows top lines - usually default to 5

#using normal data
norm_data = pd.DataFrame(np.random.normal(size=100000)) #gets data
norm_data.plot(kind="density",figsize=(10,10)) #density plot of data
plt.vlines(norm_data.mean(),ymin=0,ymax=0.4,linewidth=5.0) #line at mean
plt.vlines(norm_data.median(),ymin=0,ymax=0.4,linewidth=2.0,color="red") #line at median

#using skewed data
skewed_data = pd.DataFrame(np.random.exponential(size=100000))
skewed_data.plot(kind="density",figsize=(10,10),xlim=(-1,5))
plt.vlines(skewed_data.mean(),ymin=0,ymax=0.8,linewidth=5.0) #Plot black line at mean
plt.vlines(skewed_data.median(),ymin=0,ymax=0.8,linewidth=2.0,color="red") #Plot red line at median

#normal data with outliers
norm_data = np.random.normal(size=50)
outliers = np.random.normal(15, size=3)
combined_data = pd.DataFrame(np.concatenate((norm_data, outliers), axis=0))
combined_data.plot(kind="density",figsize=(10,10),xlim=(-5,20))
plt.vlines(combined_data.mean(),ymin=0,ymax=0.2,linewidth=5.0) #line at mean
plt.vlines(combined_data.median(),ymin=0,ymax=0.2,linewidth=2.0,color="red") #line at median

# ???
comp1 = np.random.normal(0, 1, size=200) # N(0, 1)
comp2 = np.random.normal(10, 2, size=200) # N(10, 4)
df1 = pd.Series(comp1)
df2 = pd.Series(comp2)


mtcars["mpg"].skew()  # Check skewness
data_df.skew()

mtcars["mpg"].kurt()  # Check kurtosis
data_df.kurt()

#creates dummy data
norm_data = np.random.normal(size=100000)
skewed_data = np.concatenate((np.random.normal(size=35000)+2, 
            np.random.exponential(size=65000)),axis=0)
uniform_data = np.random.uniform(0,2, size=100000)
peaked_data = np.concatenate((np.random.exponential(size=50000),
            np.random.exponential(size=50000)*(-1)),axis=0)
data_df = pd.DataFrame({"norm":norm_data,"skewed":skewed_data,
                        "uniform":uniform_data,"peaked":peaked_data})

#plots
data_df["norm"].plot(kind="density", xlim=(-5,5)) #normal distribution
data_df["peaked"].plot(kind="density", xlim=(-5,5)) #peaked distribution
data_df["skewed"].plot(kind="density", xlim=(-5,5)) #skewed distribution
data_df["uniform"].plot(kind="density", xlim=(-5,5)) #uniform distribution
data_df.plot(kind="density",xlim=(-5,5)) #all plots

#Create three dummy variables using get_dummies, then exclude the first dummy column
my_categorical_var_dummies = pd.get_dummies(my_categorical_var, prefix='Area').iloc[:, 1:]

#Creates dummy variables and shows dummy setitngs
my_categorical_var = ['rural','suburban','urban']
my_categorical_var_dummies = pd.get_dummies(my_categorical_var, prefix='Area').iloc[:, 1:]
my_categorical_var_dummies

#Categorical predictors
np.random.seed(12345) # set a seed for reproducibility
nums = np.random.rand(len(data)) # create a Series of booleans
mask_large = nums > 0.5 # roughly half of booleans are True
data['Size'] = 'small' #set Size to small
data.loc[mask_large, 'Size'] = 'large' #change roughly half to be large
data['IsLarge'] = data.Size.map({'small':0, 'large':1}) # create a new Series called IsLarge
np.random.seed(123456) # set a seed for reproducibility
# assign roughly one third of observations to each group
nums = np.random.rand(len(data))
mask_suburban = (nums > 0.33) & (nums < 0.66)
mask_urban = nums > 0.66
data['Area'] = 'rural' #sets original categorical value to Area_rural
data.loc[mask_suburban, 'Area'] = 'suburban' #sets dummy to Area_suburban
data.loc[mask_urban, 'Area'] = 'urban' #sets dummy to Area_urban
# create three dummy variables using get_dummies, then exclude the first dummy column
area_dummies = pd.get_dummies(data.Area, prefix='Area').iloc[:, 1:]
# concatenate the dummy variable columns onto the original DataFrame (axis=0 means rows, axis=1 means columns)
data = pd.concat([data, area_dummies], axis=1)
data.head() #shows data











#Central Limit Theorem
#Sampling Distributions
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns # for nice looking plots

#create an exponential graph
x = np.arange(0, 5, 0.1)
dist = stats.expon(0)
plt.plot(x, dist.pdf(x), lw=2)

print ("Mean:", dist.mean()) #prints mean
print ("Std Dev:", dist.std()) #prints std dev

# Take a random sample of size 30
sample = dist.rvs(30)
print ("Sample Mean:", np.mean(sample))
print ("Sample Std Dev:", np.std(sample))
plt.hist(sample, bins=10)
plt.show()

# Take the means of 100 samples of size 30
means = []
devs = []
samples = 100
for i in range(samples):
    sample = dist.rvs(30)
    means.append(np.mean(sample))
    devs.append(np.std(sample))
plt.hist(means, bins=20)
plt.title("Sample Means")
plt.show()
print ("Mean of Means:", np.mean(means))
print ("SD of Means:", np.std(means))

# Take the means of 1000 samples of size 30
means = []
devs = []
samples = 1000
for i in range(samples):
    sample = dist.rvs(30)
    means.append(np.mean(sample))
    devs.append(np.std(sample))
plt.hist(means, bins=20)
plt.title("Sample Means")
plt.show()
print ("Mean of Means:", np.mean(means))
print ("SD of Means:", np.std(means))
print ("Dist Mean:", dist.mean())
print ("Dist std / sqrt(30):", dist.std() / np.sqrt(30))

# distribution graphs
import seaborn as sns
sns.distplot(dist.rvs(1000)) # kernel density estimate of sample of 1000
sns.plt.show()
sns.distplot(means) # distribution of means of many samples
sns.plt.show()


#The Central Limit Theorem
#get random distribution
import random
distributions = [stats.lognorm(0.5, 1), stats.chi(1, 0.5), stats.gamma(1, 1)]
dist = random.choice(distributions)

#get random sample
n = 1000
sample = dist.rvs(n)
sns.distplot(sample)
sns.plt.show()
mean = np.mean(sample)
dev = np.std(sample) / np.sqrt(n)
print "True mean:", dist.mean()
print "Sample mean:", mean
print "Confidence interval:", "({}, {})".format(mean - 2*dev, mean + 2*dev)
