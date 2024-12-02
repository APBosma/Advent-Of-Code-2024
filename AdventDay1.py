with open('adventone.txt') as infile:
    raw_data = infile.readlines()
    
#sumOfAll = 0.0
similar = 0
new_list = []
second_list=[]
data_one = []
data_two = []
for piece in range(len(raw_data)):
    element = raw_data[piece].rstrip()
    new_list.append(element)
    #toe = int(element)
    #new_list.append(toe)
    
for part in range(len(new_list)):
    second_list.append(new_list[part].split())
    
for i in range(len(second_list)):
    data_one.append(int(second_list[i][0]))
    data_two.append(int(second_list[i][1]))

for i in range(len(data_one)):
    similar += (data_two[i])*(data_one.count(data_two[i]))
print(similar)
#data_one.sort()
#data_two.sort()

#for i in range(len(data_one)):
    #sumOfAll += abs(data_one[i]-data_two[i])
    #print(sumOfAll)

