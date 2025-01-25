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

print(house1.num_of_room)
print(house2.num_of_room)
print()
print(house1.color)
print(house2.color)
print()
print(house1.area)
print(house2.area)
print()
print(house1.description_of_house())
print(house2.description_of_house())
print()
print(house1.country)
print(house2.country)
