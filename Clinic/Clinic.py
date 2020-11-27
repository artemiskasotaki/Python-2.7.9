A=[]
Clinic=[]

for i in range(10):
    x=raw_input("Give Clinic name:")
    Clinic.append(x)

N=input("Give number of patients:")
while N<=10 and N>=1000:
    N=input("Try again")

for i in range(N):
    x=input("Give clinic number:")
    A.append(x)

SumOfPatients=[]
for i in range(10):
    SumOfPatients.append(0)

for item in A:
    SumOfPatients[item]+=1

for i in range(10):
    print SumOfPatients[i],Clinic[i]

maxi=0

for i in range(10):
    if SumOfPatients[i]>maxi:
        maxi=SumOfPatients[i]
        x=i

print "The clinic",Clinic[x],"was the one where they were hospitalized more patiends:",maxi 
