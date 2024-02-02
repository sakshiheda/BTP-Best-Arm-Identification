import matplotlib.pyplot as plt
import numpy as np
import csv

data = []

with open('Data.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        # print(lines)
        data1 = [float(i) for i in lines]
        data.append(data1)

hardness = data[0]
ae = data[1]
feas_BAI = data[2]
CSS_LUCB = data[3]


size = 27
line = 4
marker = 13
plt.plot(hardness, ae, '-o', color = 'purple', linewidth = line, markersize = marker)
plt.plot(hardness, feas_BAI, '-D', color = 'peru', linewidth = line, markersize = marker)
plt.plot(hardness, CSS_LUCB, '-X', color = 'darkolivegreen', linewidth = line, markersize = marker)
# plt.title("Experiment 1")
plt.xticks(fontsize = size)
plt.yticks(fontsize = size)
plt.legend(["Action Elimination", "Feasibility then BAI", "CSS_LUCB"], fontsize = size, loc = 'upper left')
plt.xlabel("Hardness", fontsize = size)
plt.ylabel("Number of Samples", fontsize = size)
plt.grid(True, 'major', c = '#E3E3E3')
# plt.ylim(20000, 50000)
# plt.rcParams.update({'font.size': 35})
# plt.rc('font', size = 50)
plt.show()