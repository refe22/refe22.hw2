import json
import matplotlib.pyplot as plt
import pandas as pd
with open('senator.json') as f:
    senator_data = json.load(f)

#total for each party
tr = 0
td =0
ti =0 
totals= []
for objects in senator_data['objects']:
    if objects['party'] == 'Republican': 
        tr +=1
    if objects['party'] == 'Democrat': 
        td +=1
    if objects['party'] == 'Independent': 
        ti +=1
    else:
        continue
print(tr,td,ti)
totals.append(tr)
totals.append(td)
totals.append(ti)
print(totals)

counts=[]
fr_count=0
fd_count=0
fi_count =0
#female count 
for objects in senator_data['objects']:
    if objects['party'] == 'Republican': 
        if objects['person']['gender'] == 'female':
            fr_count +=1
    if objects['party'] == 'Democrat': 
        if objects['person']['gender'] == 'female':
            fd_count +=1
    if objects['party'] == 'Independent': 
        if objects['person']['gender'] == 'female':
            fi_count +=1
    else:
        continue
counts.append(fr_count)
counts.append(fd_count)
counts.append(fi_count)
print(counts)


#male count
mr_count = 0
md_count = 0
mi_count = 0
m_counts =[]

for objects in senator_data['objects']:
    if objects['party'] == 'Republican': 
        if objects['person']['gender'] == 'male':
            mr_count +=1
    if objects['party'] == 'Democrat': 
        if objects['person']['gender'] == 'male':
            md_count +=1
    if objects['party'] == 'Independent': 
        if objects['person']['gender'] == 'male':
            mi_count +=1
    else:
        continue
print(mr_count, md_count, mi_count)
m_counts.append(mr_count)
m_counts.append(md_count)
m_counts.append(mi_count)
print(m_counts)

women = counts
men = m_counts
total = totals
index = ['Republican', 'Democrat', 'Independent']
df =pd.DataFrame({'Total count':total,'Men': men,'Women': women}, index=index)
ax= df.plot.bar(rot=0)
plt.title('Senators by Party')
plt.ylabel('Number of Senators')
plt.xlabel('Party Associaton')
plt.show()


