# Read in data onto jupyter notebook
import csv
with open('sat_scores.csv', 'rU') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print row
# 1. Describe the data.
# 2. Does the data look complete? Are there any obvious issues with the observations?

print "The data is describing the average SAT score for the verbal section and math section for each state as well"
print "as the participating rate of each state and the District of Columbia in 2001."

# 3. Create a data dictionary for the dataset

print "A data dictionary for a dataset is collection of descriptions of the data objects or items in a data model"
print "for the benefit of programmers and others who need to refer to them. In describing this dataset, the following"
print "structure can be used as a data dictionary:\n"
print "{[State]:'State Abbreviation', [Rate]:Rate (in float), [Verbal]:Verbal score (int), [Math]:Math score (int)}"

# 4 and #5. load data into a list of list and print list

with open('sat_scores.csv', 'rU') as csvfile:
    reader = csv.reader(csvfile)
    sat_list = []
    for row in reader:
        sat_list.append(row)
print sat_list

# 6. Extract a list of the labels from the data, and remove them from the data.
labels = sat_list[0]
del sat_list[0]
print labels

# 7. Create a list of State names extracted from the data

state_name = []
for i in sat_list:
    state_name.append(i[0])
print state_name

# 8. Print the types of each column

for item in sat_list:
    for i in item:
        print type(i)
    break

# 9. Do any types need to be reassigned? If so, go ahead and do it.

print "Yes, in order to analyze data, the current strings for 'Rate', 'Verbal', and 'Math' need to be converted into"
print "integers and/or floats.\n"

rate = []
for i in sat_list:
    rate.append(float(i[1]))
print rate

verbal = []
for n in sat_list:
    verbal.append(int(n[2]))
print verbal

math = []
for s in sat_list:
    math.append(int(s[3]))
print math

# 10. Create a dictionary for each column mapping the State to its respective value for that column.

state_value = {}
for i in range(len(state_name)):
    state_value[state_name[i]] = [rate[i], verbal[i], math[i]]
print state_value

# 12. print the maximum and minimum of each column

print "The maximum rate of participation is %s" % (max(rate))
print "The maximum verbal score is %s" % (max(verbal))
print "The maximum math score is %s" % (max(math))
print "The minimum rate of participation is %s" % (min(rate))
print "The minimum verbal score is %s" % (min(verbal))
print "The minimum math score is %s" % (min(math))

# 13. compute standard deviation using line comprehension
import numpy as np

def stddev(lst):
    """returns the standard deviation of lst"""
    mean = sum(lst)/len(lst)
    variance = sum([(e-mean)**2 for e in lst])
    return np.sqrt(variance)

stddev(rate)

def stddev(vscore):
    """returns the standard deviation of lst"""
    mean = sum(vscore)/len(vscore)
    variance = sum([(e-mean)**2 for e in vscore])
    return np.sqrt(variance)

stddev(verbal)

def stddev(mscore):
    """returns the standard deviation of lst"""
    mean = sum(mscore)/len(mscore)
    variance = sum([(e-mean)**2 for e in mscore])
    return np.sqrt(variance)

stddev(math)

# 14. Using MatPlotLib and PyPlot, plot the distribution of the Rate using histograms.

import numpy as np
import scipy as sp
import statsmodels as sm
import matplotlib
import matplotlib.pyplot as plt
import normal

import seaborn as sns
sns.set_style('whitegrid')
% matplotlib inline

plt.hist(rate)
plt.title("Rate of Participation for Each State")
plt.xlabel("Rate")
plt.ylabel("Frequency")

# 15. Plot the Math distribution

plt.hist(math)
plt.title("Frequence of Math SAT Score")
plt.xlabel("Score")
plt.ylabel("Frequency")

# 16. Plot the Verbal distribution

plt.hist(verbal)
plt.title("Frequeny of Verbal SAT Score")
plt.xlabel("Score")
plt.ylabel("Frequency")

# 17. What is the typical assumption for data distribution?

print "The typical assumption for data distribution is for the data to have a normal distribution. This means that if"
print "we were to take the average of a sample, record it, did another study and recorded that mean down, and repeat"
print "this procedure an infinite number of times, then the distribution of that mean would always be a perfect bell"
print "curve."

# 18. Does that distribution hold true for our data?

print "According to the graphs above, it does not appear that we have a perfect bell curve for the data--hence we do"
print "not have a normal distribution of the data. If this is true, then we can perhaps assume that this data may not"
print "be representative of the entire population of SAT test-takers. The reasons for this can be varied.\n"
print "Some states or school districts do not emphasize the SAT much as admissions test to college. If there were"
print "colleges that also do no emphasize or accept SAT scores for admissions, this may lower the rate in which"
print "students participate in the test as much as states that do emphasize the SAT. There may also be students who"
print "do not plan on going to college after high school, and therefore opt not to take the SATs. Another reason"
print "could also be that some students missed taking the exam on the day the test was administered and the data collected."

# 19. Plot some scatterplots.

from scipy.stats import linregress
plt.scatter(rate, verbal, color = 'r')
plt.plot(rate, np.poly1d(np.polyfit(rate, verbal, 1))(rate))
fit = np.polyfit(rate,verbal,1)
fit_fn = np.poly1d(fit)
linregress(rate, verbal)
plt.show()

plt.scatter(rate, math, color = 'g')
plt.plot(rate, np.poly1d(np.polyfit(rate, math, 1))(rate))
fit = np.polyfit(rate,math,1)
fit_fn = np.poly1d(fit)
linregress(rate, math)
plt.show()

# 19 BONUS: Use a PyPlot figure to present multiple plots at once.

plt.scatter(rate, verbal, color = 'y')
plt.scatter(rate, math, color = 'g')
plt.plot(rate, np.poly1d(np.polyfit(rate, math, 1))(rate))
plt.plot(rate, np.poly1d(np.polyfit(rate, verbal, 1))(rate))
fit = np.polyfit(rate,math,1)
fit_fn = np.poly1d(fit)
linregress(rate, math)
plt.show()
plt.show()

# 20. Are there any interesting relationships to note?

print "The scatterplot comparing rate of participation vs verbal appears to have a negative correlation--that is as"
print "participation rate increases the mean SAT verbal score decreases. This means that of the states that have a low"
print "participation rate, it seems that those students score higher than states that have a higher participation rate.\n"
print "Likewise, in the rate of participation vs math score scatter plot, we are seeing a nearly identical scenario"
print "except with a slope that isn't as steep. The verbal score graph's best fit line would fit a linear regression"
print "model more while the scatter plot showing the math score appears to take the shape of a polynomial regression"
print "although a linear model will adequately describe the data points."

# 21. Create box plots for each variable.

print "Box plot of Rate of participation"
plt.boxplot(rate)
plt.show()
print "Box plot of Verbal Score"
plt.boxplot(verbal)
plt.show()
print "Box plot of Math Score"
plt.boxplot(math)
plt.show()

#22 Bonus Using Tableau, create a heat map for each variable using a map of the US.

print "Please see attachment file for the Tableau heat map."
