class House():
    country = 'iran'
    
    def __init__(self, num_of_room, color, area):
        self.num_of_room = num_of_room
        self.color = color
        self.area = area
        
    def description_of_house(self):
        return (self.num_of_room, self.color, self.area)     

        
house1 = House(4, 'red', '300')
house2 = House(3, 'white', '150')

house1.num_of_room = 1
house2.area = 100

print(house1.num_of_room)
print(house2.area)

house1.country = 'usa'
house2.country = 'germany'

print(house1.country)
print(house2.country)


house1.x = 'xxx'
house2.new_attr = 'attrrr'

print(house1.x)
print(house2.new_attr)

