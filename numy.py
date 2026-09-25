import numpy as np
import csv
py_score = []
ap_score = []
com_score = []
m = float('inf')
all_scores = []
with open("placement_readiness.csv","r",encoding = "UTF-8") as f:
    reader = csv.DictReader(f)
    names = [names for names in reader.fieldnames if names.endswith("_Score")]
    print(f"Skills present in the csv folder: {names}") 
    for row in reader:
        py_score.append(int(row["Python_Score"]))
        ap_score.append(int(row["Aptitude_Score"]))
        com_score.append(int(row["Communication_Score"]))
        y = []
        for name in names:
            y.append(int(row[name]))
        all_scores.append(y)

'''py_score = py_score[:7]
ap_score = ap_score[:7]'''

py_score = np.array(py_score)
ap_score = np.array(ap_score)
com_score = np.array(com_score)
py_average = np.mean(py_score)
py_average = py_average.round(2)
ap_max = ap_score.max()
ap_min = np.min(ap_score)
x = (com_score>70).sum()
print(f"Average Python score across batch : {py_average}")
print(f"Highest Aptitude Score : {ap_max} and Lowest Aptitude Score : {ap_min}")
print(f"The number of students who scored above 70 in Communication : {x}")

#print(all_scores)
all_scores = np.array(all_scores)
max_ = np.max(all_scores,axis = 1)
min_ = np.min(all_scores,axis = 1)
gap = max_-min_
#print(gap)
for i,value in enumerate(gap[:7], start=1):
    print(f"Gap of student {i} : {value}")