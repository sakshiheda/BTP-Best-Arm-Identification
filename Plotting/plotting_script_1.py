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


plt.plot(hardness, ae, '-bo')
plt.plot(hardness, feas_BAI, '-mD')
plt.plot(hardness, CSS_LUCB, '-gX')
# plt.title("Experiment 1")
plt.legend(["Action Elimination", "Feasibility then BAI", "CSS_LUCB"])
plt.xlabel("Hardness")
plt.ylabel("Number of Samples")
plt.grid(True, 'major')
plt.show()