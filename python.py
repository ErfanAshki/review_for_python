class Time:
    def __init__(self, hours, minutes, seconds):
        if hours >= 24 : 
            raise ValueError('Hour should be less than 24')
        
        if minutes > 59 : 
            raise ValueError('Minute should be less than 60')
        
        if seconds > 59 :
            raise ValueError('Second should be less than 60')
        
        
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        
        
    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
    
    
my_time = Time(10, 25, 30)
gym_time = Time(18, 5, 0)

print(my_time)
print(gym_time)
