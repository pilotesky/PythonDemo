class Pet():

    # 初始化属性
    def __init__(self,name,age,type):
        self.name = name
        self.age = age
        self.type = type
    

    def describe_pet(pet):
        print(f"{pet.name} is a {pet.age} year old {pet.type}.")
    
    def sit(pet):
        print(f"{pet.name} is now sitting.")
    
    def roll_over(pet):
        print(f"{pet.name} rolled over!")

my_pet = Pet('Willie',6,'dog')
your_pet = Pet('Lucy',3,'cat')

my_pet.describe_pet()
your_pet.describe_pet()

my_pet.sit()
your_pet.sit()
my_pet.roll_over()
your_pet.roll_over()