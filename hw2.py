import json
import matplotlib.pyplot as plt

with open('india_gdp.json') as f:
    gdp_data = json.load(f)

with open('india_pop.json') as f:
    pop_data = json.load(f)
#print(pop_data[1])

#print(pop_data[1]['value'])
#population: 
ystart= []
pstart=[]

for i in pop_data[1]:
    for x in i: 
        if x == 'value' and i[x] !=None:
            #print(i[x])
            pstart.append(i[x])
        if x == 'date' and i[x] != '2020':
            print(i[x])
            ystart.append(int(i[x]))
#print(years,pop)
years = list(reversed((ystart)))
pop = list(reversed(pstart))

#name axes
plt.ylabel('Population (in Billions)')
plt.xlabel('Years' )
#title plot 
plt.title("India's Population from 1960-2019")
plt.plot(years,pop)
plt.tight_layout()
plt.show()




