"""
name:P.V.S.L.Deepthi
year:2nd year
branch:AIML
program:to calculate measure of central tendency:mean,median and mode
                     measure of dispersion:varience and standard deviations
lab:ML lab
"""
import statistics
#mean defination
def calculate_mean(data):
    return sum(data)/len(data)
#median defination 
def calculate_median(data):
    sorted_data=sorted(data)
    n=len(data)#length or no. of observations
    if(n%2==0):   #n is even
        middle1=sorted_data[n//2]
        middle2=sorted_data[n//2-1]
        return (middle1+middle2)/2
    else:        # n is odd
        return data[n//2]
#mode defination
def calculate_mode(data):
    return statistics.mode(data)
#varience defination 
def calculate_varience(data):
    mean_value=calculate_mean(data)
    squared_value=sum((x-mean_value)**2 for x in data)
    return squared_value/len(data)
#standard deviation
def calculate_standard_deviation(data):
    varience_value=calculate_varience(data)
    return varience_value**0.5
#data sets
data=[4,12,24,25]

#functions calling
mean_value=calculate_mean(data)
median_value=calculate_median(data)
mode_value=calculate_mode(data)
varience_value=calculate_varience(data)
standard_deviation_value=calculate_standard_deviation(data)
#printing results
print("Data=",data)
print("Mean=",mean_value)
print("Median=",median_value)
print("Mode=",mode_value)
print("Varience=",varience_value)
print("Standard deviation=",standard_deviation_value)
"""
output:
Data= [4, 12, 24, 25]
Mean= 16.25
Median= 18.0
Mode= 4
Varience= 76.1875
Standard deviation= 8.728545125048045
"""
