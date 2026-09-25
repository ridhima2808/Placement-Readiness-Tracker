import numpy as np
import csv
py_score = []
ap_score = []
com_score = []
m = float('inf')
with open("placement_readiness.csv","r",encoding = "UTF-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        py_score.append(int(row["Python_Score"]))
        ap_score.append(int(row["Aptitude_Score"]))
        com_score.append(int(row["Communication_Score"]))
        
'''py_score = py_score[:7]
ap_score = ap_score[:7]'''

py_score = np.array(py_score)
ap_score = np.array(ap_score)
com_score = np.array(com_score)
py_average = np.mean(py_score)
py_average = py_average.round(2)
ap_max = ap_score.sum()
ap_min = np.min(ap_score)
print(f"Average Python score across batch : {py_average}")
print(f"Highest Aptitude Score : {ap_max} and Lowest Aptitude Score : {ap_min}")
x = (com_score>70).sum()
print(f"The number of students who scored above 70 in Communication : {x}")