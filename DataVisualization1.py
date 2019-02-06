#!/usr/bin/python
import matplotlib.pyplot as plt
count = 0
data = open("berkley.txt","r");
#accepted male, accepted female, unaccepted male unaccepted female
frequencies = [0,0,0,0]
n_groups=6


DeptA = [0,0,0,0]
DeptB = [0,0,0,0]
DeptC = [0,0,0,0]
DeptD = [0,0,0,0]
DeptE = [0,0,0,0]
DeptF = [0,0,0,0]
for line in data:
	words = line.split(',')
	print(words[0], words[1], words[2], words[3])

if(words[3]=='A'):
    if (words[0] == "Admitted"):
        if(words[1] == "Male"):
          DeptA[0]=words[4]
        elif(words[1]== "Female")
        DeptA[1]=words[4]

    elif (words[0]== "Rejected")
        if(words[1] == "Male")
            DeptA[3]=words[4]
    elif(words[1]== "Female")
        DeptA[4] =words[4]



if(words[3]=='B'):
    if (words[0] == "Admitted"):
        if(words[1] == "Male"):
          DeptB[0]=words[4]
      elif(words[1]== "Female"):
        DeptB[1]=words[4]

    elif (words[0]== "Rejected"):
        if(words[1] == "Male"):
            DeptB[3]=words[4]
    elif(words[1]== "Female"):
        DeptB[4]=words[4]



if(words[3]=='C'):
    if (words[0] == "Admitted"):
        if(words[1] == "Male"):
            DeptC[0]=words[4]
        elif(words[1]== "Female"):
            DeptC[1]=words[4]

    elif (words[0]== "Rejected"):
        if(words[1] == "Male"):
            DeptC[3]=words[4]
        elif(words[1]== "Female"):
            DeptC[4]=words[4]

if(words[3]=='D'):
    if (words[0] == "Admitted"):
        if(words[1] == "Male"):
            DeptD[0]=words[4]
        elif(words[1]== "Female"):
            DeptD[1]=words[4]

    elif (words[0]== "Rejected"):
        if(words[1] == "Male"):
            DeptD[3]=words[4]
        elif(words[1]== "Female"):
            DeptD[4]=words[4]

if(words[3]=='E'):
    if (words[0] == "Admitted"):
        if(words[1] == "Male"):
            DeptE[0]=words[4]
        elif(words[1]== "Female"):
            DeptE[1]=words[4]

    elif (words[0]== "Rejected"):
        if(words[1] == "Male"):
            DeptE[3]=words[4]
        elif(words[1]== "Female"):
            DeptE[4]=words[4]

if(words[3]=='F'):
    if (words[0] == "Admitted"):
        if(words[1] == "Male"):
            DeptF[0]=words[4]
        elif(words[1]== "Female"):
            DeptF[1]=words[4]

    elif (words[0]== "Rejected"):
        if(words[1] == "Male"):
            DeptF[3]=words[4]
        elif(words[1]== "Female"):
            DeptF[4]=words[4]

acceptedmale =[DeptA[0],DeptB[0],DeptC[0],DeptD[0],DeptE[0],DeptF[0]]
acceptedfemale = [DeptA[1],DeptB[1],DeptC[1],DeptD[1],DeptE[1],DeptF[1]]
rejectedmale= [DeptA[2],DeptB[2],DeptC[2],DeptD[2],DeptE[2],DeptF[2]]
rejectedfemale= [DeptA[3],DeptB[3],DeptC[3],DeptD[3],DeptE[3],DeptF[3]]

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35
opactity=0.4
rects1 = ax.bar(index,acceptedmale,bar_width,alpha=opacity,color='r',label="accepted Males")
rects2 = ax.bar(index,acceptedfemale,bar_width,alpha=opacity, color='b',label = "accepted Females")
rects3 = ax.bar(index,rejectmale,bar_width,alpha=opacity, color='g',label="Reject Male")
rects4 = ax.bar(index,rejectfemale,bar_width,alpha=opacity, color-'y',label= "Reject Female")
ax.set_xlabel('Departments')
ax.set_ylabel('number of studnets')
ax.set_title('departments and Their acceptance based on Gender')
ax.set_xticks(index + bar_width /2)
ax.set_xticklabels(('A','B','C','D','E','F'))
ax.legend

plt.show()
