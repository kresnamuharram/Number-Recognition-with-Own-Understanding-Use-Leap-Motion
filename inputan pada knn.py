import re
a= '(70.3963, -57.6923, -8.65326)'
b=a.replace('(','')
c=b.replace(')','')
new_listt = c.split(',')
for list in range (0, len(new_listt)):
    new_listt[list] = float(new_listt[list])
new = map(float,new_listt)
list ='58.2675895691,93.4447097778,112.943069458,107.31952667200001,92.7183609009,66.4650497437,71.8667449951,100.71430206299999,90.8048400879,1.8559494019'
new_list = list.split(',')
list_dicari = []
for list in range (0, len(new_list)):
    new_list[list] = float(new_list[list])
results = map(float, new_list)
for list in range (0,len(new_listt)):
    new_list.append(new_listt[list])

print(new_list)


