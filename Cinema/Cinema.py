maxi=0 
sum=0 
t1=t2=80
name = raw_input("Whats your name: ")

while name!="CLOSED" and (t1!=0 or t2!=0):
    last = name 
    num=input("Are you going to watch movie 1 or 2? ")
    tickets = input("How many tickets? ")

    if num==1:
        if tickets<=t1:
            cost=tickets*7
            print "You have to pay: ",cost
            t1-=tickets
        else:
            print "Availabe: ",t1
    else:
        if tickets <=t2:
            cost=tickets*7
            print "You have to pay: ",cost
            t2-=tickets
        else:
            print "Available: ",t2

    sum+=cost
    if tickets>maxi:
        maxi=tickets
        max_n=name
    name=raw_input("Whats your name? ")

print "The last peerson who got a ticket was ",last
print "The person who booked the most tickets was ",max_n
print "the cinema's income is ",sum 