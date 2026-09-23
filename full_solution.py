import csv
pyscore = []
apscore = []
with open("placement_readiness.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        pyscore.append(int(row[2]))
        apscore.append(int(row[4]))
#pyscore = pyscore[:7]
total_python = sum(pyscore)
average_python = total_python //len(pyscore)
max_apscore = max(apscore)
min_apscore = min(apscore)
cnt = 0
for value in pyscore:
    if value > average_python:
        cnt += 1
print(f"Average python score:{average_python}")
print(f"No. of people with python score more than average : {cnt}")
print(f"max and min aptitude score are:{max_apscore}, {min_apscore}")
