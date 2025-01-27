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

    def __add__(self, other):
        seconds = self.seconds + other.seconds
        minutes = self.minutes + other.minutes + seconds // 60  
        hours = self.hours + other.hours + minutes // 60
        
        return Time(hours%24, minutes%60, seconds%60)
    
    def __ne__(self, other):
         return( self.hours != other.hours ) or \
            (self.minutes != other.minutes) or \
            (self.seconds != other.seconds)
    
    
my_time = Time(11, 57, 44)
gym_time = Time(10, 57, 44)

print(my_time != gym_time)
