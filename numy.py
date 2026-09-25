import numpy as np
import csv
py_score = []
with open("placement_readiness.csv","r",encoding = "UTF-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        py_score.append(int(row["Python_Score"]))
py_score = py_score[:7]
py_score = np.array(py_score)
average = np.mean(py_score)
print(f"Average Python score across batch : {average}")