doors =[]

for i in range(1,101):
    doors.append(0)

for j in range (1,100):
    for k in range (j,100,j):
        doors[k]=doors[k]+1
        
for l in range (1,100):
 if doors[l]%2==0:
            doors[l]=0
 else:
            doors[l]=1 
print (doors)  
print ("az 0-s számmall jelölt ajtók zártak")  