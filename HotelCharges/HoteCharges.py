def charge(days,period):
    charge = 0
    if period == "LOW":
        if days >=1 and days <=3:
            charge = days*40
        elif days <=7:
            charge = days*30
        else:
            charge = days*25
    else:
        if days >=1 and days<=3:
            charge = days*70
        elif days<=7:
            charge=days*55
        else:
            charge=days*50
    return charge

SumH=0
SumL=0

for i in range(3):
    days= input("Give days")
    period=raw_input("Give period of staying")
    while period!= "LOW" and period!= "HIGH":
        period = raw_input("Give again")
    Charge=charge(days,period)
    if period=="LOW":
        SumL+=Charge
    else:
        SumH+=Charge

print "Sum of High Period", SumH
print "Sum of Low Period", SumL
