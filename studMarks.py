import plotly.figure_factory as ff
import csv
import statistics
import random
import pandas as pd
import plotly.graph_objects as go
from scipy import rand

df=pd.read_csv('studentMarks.csv')
data=df["Math_score"].tolist()
#fig=ff.create_distplot([data],["Math Score"],show_hist=False)
#fig.show()

mean=statistics.mean(data)
std_dev=statistics.stdev(data)
#print(mean)
#print(std_dev)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)

    mean=statistics.mean(dataset)
    return mean

mean_list=[]
for i in range(0,1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)

mean_sample=statistics.mean(mean_list)
std_sample=statistics.stdev(mean_list)
print(mean_sample)
print(std_sample)

#fig=ff.create_distplot([mean_list],["Mean of Samples of scores"],show_hist=False)
#fig.add_trace(go.Scatter(x=[mean_sample, mean_sample], y=[0,0.020], mode="lines", name="MEAN"))
#fig.show()

## findig the standard deviation starting and ending values
first_std_deviation_start, first_std_deviation_end = mean_sample-std_sample, mean_sample+std_sample
second_std_deviation_start, second_std_deviation_end = mean_sample-(2*std_sample), mean_sample+(2*std_sample)
third_std_deviation_start, third_std_deviation_end = mean_sample-(3*std_sample), mean_sample+(3*std_sample)

# print("std1",first_std_deviation_start, first_std_deviation_end)
# print("std2",second_std_deviation_start, second_std_deviation_end)
# print("std3",third_std_deviation_start,third_std_deviation_end)

## plotting the graph with traces
# fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
# fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
# fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
# fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
# fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
# fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
# fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 START"))
# fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
# fig.show()

df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()
mean_of_sample1 = statistics.mean(data)
print("Mean of sample1:- ",mean_of_sample1)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN OF SAMPLE"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()