import math
def add_time(start,duration,day=None):
    ct = start.split()
    current_time = ct[0].split(":")
    Given_time=duration.split(":")
    #print(current_time,Given_time)
    hour1=int(current_time[0])
    hour2=int(Given_time[0])
    min1=int(current_time[1])
    min2=int(Given_time[1])
    tothour = hour1+hour2
    totmin=min1+min2
    while totmin >= 60:
        totmin -= 60
        tothour += 1
    #print(tothour,totmin)
    totmin = str(totmin)
    if len(totmin)==1:
        totmin="0"+totmin
    later_period = 0
    while tothour >= 12:
        tothour -=12
        later_period=later_period+1
    if tothour==0:
        tothour=tothour+12
    period = ct[1]
    if period == "PM":
        if later_period%2 ==0:
            fina_period = "PM"
        else:
            fina_period = "AM"
    
    if period == "AM":
        if later_period%2 ==0:
            fina_period = "AM"
        else:
            fina_period = "PM"
    
    
    output = str(tothour)+":"+totmin+" "+fina_period
    

    days_later = later_period/2
    x=days_later
    week = {'sunday': 1,'monday':2,'tuesday':3,'wednesday':4,'thursday':5,'friday':6,'saturday':7}
    def get_key(val):
        for i1, i2 in week.items():
            if i2 == val:
                return i1
    if day!=None:
        day=day.lower()
        y=week[day]
        final_day =math.ceil((y+x)%7)
        #print(x,y,final_day)
        #print(get_key(final_day))
        output = output+", "+get_key(final_day).capitalize()

    
    if x == 1:
        days_later="(next day)"
        output=output+" "+days_later
    if x<1 and period=="PM" and (hour1+hour2)<12:
        output=output
    if x<1 and period=="PM" and (hour1+hour2)>12:
        days_later="(next day)"
        output=output+" "+days_later
    
    if x > 1:
        days_later = "("+str(math.ceil(days_later))+" days later)"
        output=output+" "+days_later
    
    print(output)
    return output




add_time("10:06 AM", "2:02")
add_time("11:55 AM", "3:12")
add_time("2:59 AM", "24:00")
add_time("11:59 PM", "24:05")
add_time("8:16 PM", "466:02")
add_time("8:16 PM", "466:02", "tuesday")
add_time("9:15 PM", "5:30")
