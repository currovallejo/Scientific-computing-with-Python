class time:

    def __init__(self, start:str, duration:str, day:str=""):
        self.start = start
        self.duration = duration
        self.day = day.lower()
        self.day = day.capitalize()
    
    def start_to_total_minutes(self):
        hours = ''
        minutes = ''
        format = ''
        b=0
        for i in self.start:
            if i != ':' and b==0:
                hours += i
            elif i==':' and b==0:
                b=1
            elif i!= ' ' and b==1:
                minutes += i
            elif i== ' ' and b==1:
                b=2
            elif i!= ' ' and b==2:
                format += i

        if format == 'PM':
            hours = int(hours) + 12
        else:
            hours = int(hours)
        
        total_minutes = hours*60 + int(minutes)

        return total_minutes
    
    def duration_to_total_minutes(self):
        hours = ''
        minutes = ''
        b=0
        for i in self.duration:
            if i != ':' and b==0:
                hours += i
            elif i==':' and b==0:
                b=1
            elif i!= ' ' and b==1:
                minutes += i

        total_minutes = int(hours)*60 + int(minutes)

        return total_minutes
    
    def total_time(self):
        start = time.start_to_total_minutes(self)
        duration = time.duration_to_total_minutes(self)

        total_time = start+duration
        minutes = total_time%60
        hours = total_time//60
        days = hours//24
        hours = hours%24
        
        if hours>=12:
            format = 'PM'
            if hours != 12:
                hours = hours-12
        else:
            if hours == 0:
                hours = 12
            format = 'AM'
        
        if minutes <10:
            minutes = '0' + str(minutes)
        
        new_time = str(hours)+':'+str(minutes) + ' ' + format

        if self.day!= "":
            weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
            index = weekdays.index(self.day)
            if index+days>6:
                new_day = weekdays[(days%7 + index)-7]
                
            else:
                new_day = weekdays[days + index]
            
            new_time +=', ' + new_day
        
        if days !=0:    
            if days==1:
                days_later = ' (next day)'
            elif days>1:
                days_later = ' (' + str(days) + ' days later)'
            
            new_time += days_later
        
        print(new_time)
        return new_time

        
def add_time(start, duration,starting_day=""):

    pepe = time(start=start,duration=duration,day=starting_day)
    new_time = pepe.total_time()

    return new_time