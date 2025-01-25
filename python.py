class Car:
    def __init__(self, car_color, model):
        self.color = car_color
        self.model = model
        
    def turn_on_light(self):
        print('Turn on')
        
    def rahnama_zadan(self, right_or_left):
        return f"{right_or_left} is on"

    def print_detail(self):
        print(f"color is {self.color} - model is {self.model}")
        
        
my_car = Car('blue', 'BMW')
print(my_car.color)
print(my_car.model)
my_car.turn_on_light()
print(my_car.rahnama_zadan('right'))

car1 = Car('black', '207')
car1.print_detail()

car1.print_detail(20)
 