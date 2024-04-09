class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def fullname(self):
        fullname = self.first + " " + self.last
        return fullname

#u1 = User('Hassan', 'Munene')
#print(u1.fullname())

class Hassan(User):
    def __init__(self, first, last, age):
        super().__init__(first, last)
        self.age = age

    def calc(self):
        return int(self.age) + 1

h = Hassan('Hassan', 'Munene', 23)
print(h.calc())
