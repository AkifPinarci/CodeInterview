import queue as q
class Animal:
    id = 0
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.idd = Animal.id
        Animal.id += 1

class Shelter:
    def __init__(self):
        self.dog = q.Queue()
        self.cat = q.Queue()

    def enqueue(self, animal):
        if animal.type == "dog":
            self.dog.add(animal)
        if animal.type == "cat":
            self.cat.add(animal)


    def dequeueAny(self):
        if (self.dog.getSize() != 0 and self.cat.getSize() != 0) and self.dog.peek().idd < self.cat.peek().idd:
            return self.dog.remove().name
        else:
            return self.cat.remove().name
    def dequeueDog(self):
        return self.dog.remove().name
    
    def dequeueCat(self):
        return self.cat.remove().name

    def peek(self):
        print(self.dog.peek().idd)

shelter = Shelter()
dog1 = Animal("dog", "Dogo")
shelter.enqueue(dog1)
cat1 = Animal("cat", "Cata")
shelter.enqueue(cat1)
dog2 = Animal("dog", "Dogo2")
shelter.enqueue(dog2)
cat2 = Animal("cat", "Cata2")
shelter.enqueue(cat2)
print(shelter.dequeueAny())
print(shelter.dequeueAny())
print(shelter.dequeueAny())
print(shelter.dequeueAny())