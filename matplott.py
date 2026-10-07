import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os
os.makedirs("charts",exist_ok=True)
df = pd.read_csv("placement_readiness.csv")
score_col = [
    'Python_Score',
    'Aptitude_Score',
    'Communication_Score',
    'SQL_Score'
]
#average of each score
avg = df[score_col].mean(axis=0)

# the three types of readiness bands
'''r_bands = df['Readiness_band'].unique()'''
counts = df["Readiness_band"].value_counts()

#total branches names
branches = df['Branch'].unique()
#average readiness score for each branch
avg_bscore = []
for branch in branches:
    avg = df[df['Branch']==branch]['readiness_Score'].mean()
    avg_bscore.append(avg)

##########################################################################################

#Bar chart: average score for each of the four skills

plt.figure(figsize=(12,6))
plt.bar(score_col,avg,color=["#E1306C", "#25D366", "#FF0000", "#0A66C2"])
plt.title("Average Score by Skill")
plt.xlabel("Skill")
plt.ylabel("Average Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('charts/skill_avg.png')
plt.close()
###########################################################################################

#Bar chart: how many students are in each readiness band

plt.figure(figsize=(12,6))
plt.bar(counts.index,counts.values,color = ["#E1306C", "#25D366", "#FF0000", "#0A66C2"])
plt.xlabel("Readiness bands")
plt.ylabel("count")
plt.title("Students by Readiness Band")
plt.tight_layout()
#plt.xticks(rotation=45)
plt.savefig('charts/readiness_bands.png')
plt.close()
###########################################################################################

plt.figure(figsize=(10,6))
plt.plot(branches,avg_bscore,label = 'average score', color = 'blue')

plt.xlabel("Branch")
plt.ylabel("Average Score")
plt.title("average readiness score by branch")
plt.legend()
plt.tight_layout()
plt.savefig('charts/average_readiness_score.png')
plt.close()
###########################################################################################
