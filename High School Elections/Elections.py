NAMES=CLASS=VOTES=[]

for i in range(40):
    name=raw_input("Name of candidate: ")
    classroom=raw_input("Candidate's class:")
    #while classroom !="A" and classroom != "B" and classroom != "C":
     #   classroom=raw_input("Class must be A,B or C. Give again: ")
    votes=input("How many votes: ")
    while votes<0 or votes>200:
        votes=input("The number of votes must be from 0 to 200. Give votes again:")
    
    NAMES.append(name)
    CLASS.append(classroom)
    VOTES.append(votes)

sumA=0
sumB=0
sumC=0

for i in range(40):
    if CLASS[i]=="A":
        sumA=+VOTES[i]
    elif CLASS[i]=="B":
        sumB+=VOTES[i]
    else:
        sumC+=VOTES[i]

max_votes=sumA
max_class="A"

if sumB>max_votes:
    max_votes=sumB
    max_class="B"
if sumC>max_votes:
    max_votes=sumC
    max_class="C"
print "The classroom with the most votes is ", max_class

for i in range(1,39):
    for j in range(5,i-1,-1):
        if VOTES[j]>VOTES[j-1]:
            VOTES[j],VOTES[j-1]=VOTES[j-1],VOTES[j]
            NAMES[j],NAMES[j-1]=NAMES[j-1],NAMES[j]
            CLASS[j],CLASS[j-1]=CLASS[j-1],CLASS[j]
 
 
print "The final 15 members: "
for i in range(15):
     print NAMES[i]
    
i=39
found=False
while i>=0 and not found:
    if CLASS[i]=="A":
        found=True
    else:
        i-=1
print "The student from class A with the least votes is: ", NAMES[i] 