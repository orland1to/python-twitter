class Dog:
    species = 'mammal'


    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say_hello(self):
        return f'Hi i am {self.name}'



puppet = Dog('perrito',10)
print('El nombre del perro es {name} y su edad {age}'.format(
	name=puppet.name,
	age=puppet.age
	))
print(puppet.say_hello())




