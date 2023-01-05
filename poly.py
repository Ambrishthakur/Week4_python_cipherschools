# special magic methods / dunder methods
# operator overloading
# polymorphism


class phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def phone_name(self):
        return f"{self.brand} {self.model}"

    # str , repr
    def __str__(self):
        return f'{self.brand} {self.model} and price is {self.price}'



    # l = [1,2,3,]
    # print(l)
    phone = phone_name('nokia', '1100', '1000')
    print(str(phone))
