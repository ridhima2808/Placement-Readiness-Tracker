import pandas as pd
df = pd.read_csv("placement_readiness.csv")
df.head()
df.tail()
df['Python_Score'].describe()
df.shape
print(list(df.columns))
a = df[df['Python_Score']>75]
print(a)
print(df.sort_values(by = 'Aptitude_Score',ascending=True).head(5))
print(df.sort_values(by = 'Python_Score',ascending=True).head(10))
b = df[df['Python_Score']>df['Communication_Score']]
score_col = [col for col in df.columns if col.endswith('_Score')]
df['Total_Score'] = df[score_col].sum(axis=1)

df['Average_Score'] = df['Total_Score']/4

df['Weakest_skill_Score'] = df[score_col].min(axis=1)
score = df['Average_Score'] + (df['Projects_Completed']*2) + df['Mock_Interviews_Attended']
df['readiness_Score'] = score.clip(upper=100)


'''df.loc[df['readiness_Score']>75,df["Readiness_band"]] = 'Ready'''
df['Readiness_band'] = pd.cut(df['readiness_Score'],bins = [-float('inf'),60,75,float('inf')], labels=['Needs Work', 'Almost Ready', 'Ready'],right=False)
print(list(df.columns))

'''m_ready = (df['Readiness_band'] == 'Ready').sum()
m_almostReady = (df['Readiness_band'] == 'Almost Ready').sum()
m_needWork = (df['Readiness_band'] == 'Needs Work').sum()
print(m_ready,m_almostReady,m_needWork)'''

counts = df['Readiness_band'].value_counts()
max_Count_id = counts.idxmax()
max_count = counts.max()
print(counts)
print(max_Count_id," ",max_count)