#from abc import ABC,abstractmethod
class Animal():
    def __init__(self,id,age):
        self.__id=id
        self.__age=age
    

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,new_id):
        self.__id=new_id

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,new_age):
        self.__age=new_age

    def move(self):
        print("moving")



class Cow(Animal):
    def __init__(self,id,age,mass):
        super().__init__(id,age)
        self.__mass=mass


    @property
    def mass(self):
        return self.__mass
    
    @mass.setter
    def mass(self,mass):
        self.__mass=mass

    def make_sound(self):
        print("Moo")
    def move(self):
        super().move()
    def milking(self):
        print("Getting milked.")


class Duck(Animal):
    def __init__(self,id,age):
        super().__init__(id,age)
    def make_sound(self):
        print("Kwak")
    def move(self):
        super().move()
        print("Swim")
        print("Fly")


class Cat(Animal):
    def __init__(self,id,age):
        super().__init__(id,age)
    def make_sound(self):
        print("Meow")
    def move(self):
        super().move()
        print("Jump")
        print("Leap")


class Farm:
    def __init__(self,*args):
        self.__animal_list=list(args)
        self.__animals=dict(zip([i.id for i in self.__animal_list],self.__animal_list))
    
    @property
    def animals(self):
        return self.__animals
    def add_animal(self,animal):
        self.__animals[animal.id]=animal
        print("added successfully")
    def remove_animal(self,id):
        animal=self.__animals.pop(id,None)
        print(animal, "deleted")
    def display(self):
        for i in self.__animals.values():
            print(i.id,i.age)




scrooge=Duck("d001",60)
betty=Cow("a001",5,1000)
matroskin=Cat("c001",12)

animal_farm=Farm(scrooge,betty,matroskin)

print("for scrooge we have:\nID:",scrooge.id,"\nage:",scrooge.age,"\nit can")
scrooge.make_sound()
scrooge.move()


print("for betty we have:\nID:",betty.id,"\nage:",betty.age,"\nmass:",betty.mass,"\nit can")
betty.make_sound()
betty.move()
betty.milking()

print("for matroskin we have:\nID:",matroskin.id,"\nage:",matroskin.age,"\nit can")
matroskin.make_sound()
matroskin.move()

animal_farm.display()