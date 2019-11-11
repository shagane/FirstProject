def AnimalFactory(legs, wings, smell):
    if legs == 4 and smell == 1:
        return Dog()
    elif legs == 4 and smell == 0:
        return Cat()
    elif legs == 2 and wings == 2:
        return Petukh()
    else:
        return Animals(legs, wings, smell)


class Animals(object):

    def __init__(self, legs, wings, smell):
        self.legs_quantity = legs
        self.wings_quantity = wings
        self.sense_of_smell = smell
        self.animal_type = 'Nevedomiy nauke zver'

    def doing(self):
        print("Pitaetsya vizhit' v etom sumashedshem mire")

class Dog(Animals):
    def __init__(self):
        super().__init__(4, 0, 1)
        self.animal_type = "Dog"
            
    def doing(self):
        return "I'm a dog, woof, woof! I have {} legs and I can smell very well".format(self.legs_quantity)
        
class Cat(Animals):
    def __init__(self):
        super().__init__(4, 0, 0)
        self.animal_type = "Cat"
   
    def doing(self):
        return "I'm cat and, meow, meow... I have {} legs and can't do anithing".format(self.legs_quantity)


class Petukh(Animals):
    def __init__(self):
        super().__init__(2,2,0)
        self.animal_type = "Petookh"
            
    def doing(self):
        return "I'm a Petuch kukareku! I have {} legs and {} wings, but I can't fly".format(self.legs_quantity, self.wings_quantity)


def int_input(message):
    while True:
        try:
            a = int(input(message))
            return a
        except:
            print ("Wrong input type, should be number")


if __name__ == "__main__":
   
    print ("Hello children, let\'s guess the animal!")
    while True:    
        a = int_input('How many legs does it have? \n')
        if a != 4 and a != 2:
            print ('Sorry, I only know animals with 2 or 4 legs, try again')
        else:
            break
            
    while True:    
        b = int_input('Ok! It has {} legs. And what about wings? How many wings does it have?(Type 0 if there are no wings)\n'.format(a))
        c = 1
        if a == 4 and b != 0:
            print('Sorry, I don\'t know such an animal, I belive it doesn\'t have any wings if it has {} legs'.format(a))
            b = 0
        elif a == 2 and b == 2:
            print('Ok, so it has {} legs and {} wings '.format(a, b))
            c = 0
        elif a == 2 and b!=2 or b!=0:
            b = 2
            c = 0
            print('Sorry, I don\'t know such an animal. If it has {} legs, it should have {} wings \n'.format(a, b))
        else:
            print('Ok, so it has {} legs and no wings '.format(a))
            break
     
    c = input('And there is the last question! Does it have the best sense of smell of all animals? (Yes or No) \n')
    
    while c != 1 and c != 0:
        if a == 4 and c == 'yes' or c == 'Yes' or c == 'YES':
            c = 1
            break
        elif a == 2 and c == 'yes' or c == 'Yes' or c == 'YES':
            print('Animals with wings don\'t have the best sense of smell')
            c = 0
            break
        elif c == 'no' or c == 'No' or c == 'NO':
            c = 0
            break
        else:
            c = input('Yes or No? Make a dicision \n')
        

    print (a, b, c)

    unknown_animal = AnimalFactory(a, b, c)
    # print(unknown_animal.animal_type)
    print(unknown_animal.doing())
 