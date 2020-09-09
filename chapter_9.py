class Dog():
    def __init__(self,name,age):
        self.name = name 
        self.age =  age

    def sit(self):
        print(self.name.title()," is now sitting.")

    def roll_over(self):
        print(self.name.title(),"  rolled over!")


class Sandwich():
    def __init__(self , ingredient):
        self.Ing = ingredient

    def ing_description(self):
        print("customer is ordering sandwich with "+self.Ing)

class Restaurant():
    def __init__(self,name,cuis):
        self.restaurant_name = name
        self.cuisine = cuis

    def describe_restaurant(self):
        print("the restaurant's name is:",self.restaurant_name,"and selling ",self.cuisine," !")

    def open_restaurant(self):
        print("the restaurant ,",self.restaurant_name,"is opening")

