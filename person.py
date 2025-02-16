class Person:
    """
    A class to represent a person with a name and age.
    """

    def __init__(self, name: str, age: int):
        """
        Initialize a Person object.
        Parameters:
        name (str): The name of the person.
        age (int): The age of the person.
        """
        self.name = name
        self.age = age

    def birthday(self):
        """
        Increases the person's age by 1.
        """
        self.age += 1


p = Person("Alice", 25)
p.birthday()
print(p.age)
