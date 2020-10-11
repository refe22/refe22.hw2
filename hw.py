import json
import matplotlib.pyplot as plt

with open('senator.json') as f:
    senator_data = json.load(f)

#total for each party
party_data = {}
for objects in senator_data['objects']:
    #party = objects['party'] 
    if objects['party'] not in party_data:
        party_data[objects['party']] = 0
    if objects['party'] in party_data:
        party_data[objects['party']] +=1
    #print(objects['party'])
print(party_data)


#print(senator_data['objects'][])
fr_count = 0
fi_count = 0
fd_count = 0
counts =[]

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

fig, ax = plt.subplots() 
"""
ax.set(
    xlabel='Party Association', 
    ylabel= 'Number of Senators'
    )
"""
#name axes
x = party_data.keys()
z = m_counts
y = party_data.values()
plt.xlabel('Party Association')
plt.ylabel('Number of Senators' )
#title plot
plt.title('Senators by Party')
#Adding a Legend
plt.axes()
plt.bar('z', 'y')
plt.show()
#print(plt.style.available) 