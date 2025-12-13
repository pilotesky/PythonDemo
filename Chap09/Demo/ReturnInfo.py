class car():
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def get_info(self):
        full_info = f"{self.year} {self.brand} {self.model}"
        return  full_info
    
my_car = car('audi','A4',2020)
car_info = my_car.get_info()
print(car_info)