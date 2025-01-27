class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        
        
    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"
    
    
my_time = Time(10, 25, 30)
gym_time = Time(18, 5, 0)

print(my_time)
print(gym_time)
